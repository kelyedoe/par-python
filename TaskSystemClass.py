import multiprocessing
if __name__ == '__main__':
    multiprocessing.freeze_support()

from multiprocessing import Pool
from threading import Thread
import networkx as nx
import matplotlib.pyplot as plt
import graphviz
import time
import concurrent.futures
import threading


    
# Définition de la class TaskSystem()
class TaskSystem:
    # Constructeur de la class
    def __init__(self, tasks, dependencies):
        self.tasks = tasks
        self.dependencies = dependencies
        self.completed_tasks = []
        self.taches_executees = []

    # La fonction getDependencies(taskName) retourne la liste des tâches précédentes à la tâche taskName en paramètre
    def getDependencies(self, task_name):
        return self.dependencies[task_name]
    
    # La fonction runSeq() pour une exécution séquentielle des tâches
    def runSeq(self):
        for task in self.topological_sort():
            task.run()

    # La fonction run_task() exécute une tâche définie
    def run_task(self, task):
        for dependence in self.dependencies[task.name]:
            self.run_task(self.get_task_by_name(dependence)) 
        task.run()
        
    # Définition de la fonction get_task_by_name() qui renvoie l'objet tâche en se basant sur le nomTache
    def get_task_by_name(self, task_name):
        # Find the task with the given name
        for task in self.tasks:
            if task.name == task_name:
                return task
     
    # run() permet l'exécution parallèle des tâches en tenant compte du parallélisme maximal des tâches en utilisant un tri topologique sur la liste des tâches     
    def run(self):
        # L'ensemble des taches éxécutées
        finished = set()
        while len(finished) < len(self.tasks):
            for task in self.topological_sort():
                if task not in finished:
                    if all(dep in finished for dep in self.dependencies[task.name]):
                        task.run()
                        finished.add(task)            

    # Définition de la fonction de tri topologique (relation de précédences entre les taches)
    def topological_sort(self):
        ready = [task for task in self.tasks if not self.dependencies[task.name]]
        while ready:
            task = ready.pop(0)
            yield task
            for t in self.tasks:
                if task.name in self.dependencies[t.name]:
                    self.dependencies[t.name].remove(task.name)
                    if not self.dependencies[t.name]:
                        ready.append(t)


    # * La fonction verifier_entrees permet de faire des analyses sur le système de tâches task && contraintes
    def verifier_entrees(self,tasks, dependencies):
        # Vérifier l'unicité des noms des tâches dans le système
        tasks_names = [task.name for task in tasks]
        if len(set(tasks_names)) != len(tasks_names):
            raise ValueError("Les noms des tâches doivent être uniques")
        else:
            print("Les tâches sont uniques")

        # Vérifier si toutes les tâches citées dans les contraintes sont bien existentes
        tasks_names_dep = set(dependencies.keys()).union(set([task for dep in dependencies.values() for task in dep]))
        if not tasks_names_dep.issubset(set(tasks_names)):
            raise ValueError("Le dictionnaire de précédence contient des nom de tâches inexistentes")
        else:
            print("Toutes les noms des tâches existent")

        # Vérification si toutes les tâches ont une précédente
        for task in tasks:
            if task.name not in dependencies and not task.precedentes:
                raise ValueError(f"La tâche {task.name} n'a pas de précédente")

        # Vérifier le déterminisme du système de tâches
        tasks_names_orphelines = set(tasks_names).difference(tasks_names_dep)
        if len(tasks_names_orphelines) > 1:
            raise ValueError("Le système de tâches est indéterminé")
        else:
            print("Le système des tâches est déterminé")

    # La fonction draw_no() permet de tracer le graphe d'exécution des tâches simple
    def draw_no(self):
        G = nx.DiGraph()
        G.add_nodes_from(self.tasks)
        
        for task in self.tasks:
            dependencies = self.getDependencies(task.name)
            for dependency in dependencies:
                G.add_edge(dependency, task.name)
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        plt.show()

    # Une fonction detRun() pour le déterminisme
    def detRun(self):
        ready = set(self.tasks)
        running = set()
        finished = set()
        while ready or running:
            for task in running.copy():
                if task.isFinished():
                    finished.add(task)
                    running.remove(task)
                    for t in ready.copy():
                        if task in self.getDependencies(t.name):
                            self.tasks.remove(t)
                            ready.remove(t)
                            running.add(t)
            for task in ready.copy():
                if not set(self.getDependencies(task.name)) - finished:
                    ready.remove(task)
                    running.add(task)
            if running and not ready:
                for task in running:
                    task.run()
                    
        # Test randomisé de déterminisme
        result1 = {}
        for task in self.tasks:
            result1[task.name] = task.result
        result2 = {}
        for task in self.tasks:
            task.reset()
            result2[task.name] = task.runRnd()
        if result1 != result2:
            print("Le système de taches n'est pas déterminé")
        #else:
            #print("le système des taches est déterminé")

    # Test de randomisation déterminé
    def detTestRnd(self, n):
        for i in range(n):
            self.detRun()

    def parCost(self, num_exec = 1):
        duree_total_sequentielle = 0
        duree_total_parallele = 0

        for i in range(num_exec):
            # Faire une exécution séquentielle sur le système de tâches
            debut_exec_sequentielle = time.time()
            self.runSeq()
            fin_exec_sequentielle = time.time()
            temps_sequentielle = fin_exec_sequentielle - debut_exec_sequentielle
            duree_total_sequentielle += temps_sequentielle

            # Faire une exécution parallèle sur le système de tâches
            debut_exec_parallele = time.time()
            self.run_par()
            fin_exec_parallele = time.time()
            temps_parallele = fin_exec_parallele - debut_exec_parallele
            duree_total_parallele += temps_parallele

        # Calcul du temps moyen des exécutions
        temps_moyen_seq = duree_total_sequentielle / num_exec
        temps_moyen_par = duree_total_parallele / num_exec

        print(f"Temps d'exécution moyen en séquentiel : {temps_moyen_seq: .5f} secondes")
        print(f"Temps d'exécution moyen en parallèle : {temps_moyen_par: .5f} secondes")
        print(f"La différence de temps d'exécution est de : {temps_moyen_seq - temps_moyen_par: .5f} secondes")
  
    # Fonction pour exécuter une tâche
    def executer_tache(tache):
        print(f"Exécution de la tâche {tache}")
            
    # Fonction pour exécuter un groupe de tâches en parallèle
    def executer_groupe_taches(self,groupe):
        with Pool() as pool:
            pool.map(self.executer_tache, groupe)


    def run_par(self):
        finished = set()
        running = {}
        executed = set()
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.tasks)) as executor:
            while len(finished) < len(self.tasks):
                ready = [task for task in self.tasks if not set(self.dependencies[task.name]) - finished]
                for task in ready:
                    if task.name not in executed:
                        if task not in running.values():
                            running[task.name] = task
                            executor.submit(task.run)
                for name, task in running.copy().items():
                    if task.isFinished():
                        finished.add(task)
                        executed.add(task.name)
                        del running[name]
                        for t in self.tasks:
                            if task.name in self.dependencies[t.name]:
                                self.dependencies[t.name].remove(task.name)



    def topological_sorty(self):
        ready = [task for task in self.tasks if not self.dependencies[task.name]]
        while ready:
            task = ready.pop(0)
            yield task
            for t in self.tasks:
                if task.name in self.dependencies[t.name]:
                    self.dependencies[t.name].remove(task.name)
                    if not self.dependencies[t.name]:
                        ready.append(t)
        print(ready.count())
             

    def draw(self):
        # Create a new graph
        dot = graphviz.Digraph()
        
        # Add nodes for all tasks
        for task in self.tasks:
            dot.node(task.name)
        
        # Add edges for all dependencies
        for task in self.tasks:
            for dep in self.dependencies[task.name]:
                dot.edge(dep, task.name)
        
        # Compute levels of parallelism for each task
        levels = {}
        for task in self.tasks:
            level = 0
            for dep in self.dependencies[task.name]:
                dep_level = levels[dep] + 1
                if dep_level > level:
                    level = dep_level
            levels[task.name] = level
        
        # Assign colors to nodes based on their level of parallelism
        colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
        for task, level in levels.items():
            color = colors[level % len(colors)]
            dot.node(task, style='filled', fillcolor=color)
        
        # Display the graph
        dot.render('graph')

        