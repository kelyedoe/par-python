from threading import Thread
import networkx as nx
import matplotlib.pyplot as plt
import time

# Définition de la class TaskSystem()
class TaskSystem:
    # Constructeur de la class
    def __init__(self, tasks, dependencies):
        self.tasks = tasks
        self.dependencies = dependencies
        self.completed_tasks = []

    # La fonction getDependencies(taskName) retourne la liste des tâches précédentes à la tâche taskName en paramètre
    def getDependencies(self, task_name):
        return self.dependencies[task_name]
    
    # La fonction runSeq() pour une exécution séquentielle des tâches
    def runSeq(self):
        for task in self.tasks:
            self.run_task(task)
            print("Exécution de la tâche:", task.name)

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
        # Faire un tri topologique sur les tâches
        order = self.topological_sort()
        # Exécute each task in parallel if possible
        for task_group in order:
            if len(task_group) == 1:
                task_group[0].run()
            else:
                # Create a separate thread for each task in the group
                threads = [Thread(target=task.run) for task in task_group]
                # Start all threads simultaneously
                for thread in threads:
                    thread.start()
                # Wait for all threads to finish before continuing
                for thread in threads:
                    thread.join()
            # Mark each task in the group as completed
            for task in task_group:
                #if all(dep in self.completed_tasks for dep  in self.dependencies):
                    task.run()
                    self.completed_tasks.append(task)
                    print("tache éxécutée en paralléle:", task.name)

    # Définition de la fonction de tri topologique
    def topological_sort(self):
        # Le tri topologique  permet ici de determiner l'ordre d'exécution des tâches
        order = []
        ready = [task for task in self.tasks if not self.dependencies[task.name]]
        while ready:
            # Ajouter les tâches prêtes dans ordre
            order.append(ready)
            # Une nouvelle liste de tâches qui sera prêtes après l'exécution de la liste de tâches actuelle
            # Create a new list of tasks that will be ready after executing the current set of tasks
            new_ready = []
            for task in ready:
                # Mark the task as completed
                self.completed_tasks.append(task)
                # Add any tasks that are now ready to the new_ready list
                for dependent_task_name in self.dependencies[task.name]:
                    dependent_task = self.get_task_by_name(dependent_task_name)
                    if dependent_task not in new_ready and dependent_task not in self.completed_tasks:
                        dependencies_satisfied = all([dep_task in self.completed_tasks for dep_task in self.dependencies[dependent_task_name]])
                        if dependencies_satisfied:
                            new_ready.append(dependent_task)
            ready = new_ready
        return order


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

    # La fonction draw() permet de tracer le graphe d'exécution des tâches
    def draw(self):
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
        else:
            print("le système des taches est déterminé")

    # Test de randomisation déterminé
    def detTestRnd(self, n):
        for i in range(n):
            self.detRun()

    def parCost(self, num_exec = 5):
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
            self.run()
            fin_exec_parallele = time.time()
            temps_parallele = fin_exec_parallele - debut_exec_parallele
            duree_total_parallele += temps_parallele

        # Calcul du temps moyen des exécutions
        temps_moyen_seq = duree_total_sequentielle / num_exec
        temps_moyen_par = duree_total_parallele / num_exec

        print(f"Temps d'exécution moyen en séquentiel : {temps_moyen_seq: .5f} secondes")
        print(f"Temps d'exécution moyen en parallèle : {temps_moyen_par: .5f} secondes")
        print(f"La différence de temps d'exécution est de : {temps_moyen_seq - temps_moyen_par: .5f} secondes")
