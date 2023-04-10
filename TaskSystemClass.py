from threading import Thread
import networkx as nx
import matplotlib.pyplot as plt

# Définition de la class TaskSystem()
class TaskSystem:
    # Constructeur de la class
    def __init__(self, tasks, dependencies):
        self.tasks = tasks
        self.dependencies = dependencies
        self.completed_tasks = []

    # La fonction getDependencies(taskName) retourne la liste des taches précédentes à la tache taskName en paramètre
    def getDependencies(self, task_name):
        return self.dependencies[task_name]
    
    # La fonction runSeq() pour une éxécution séquentielle des taches
    def runSeq(self):
        for task in self.tasks:
            self.run_task(task)
            print("Exécution de la tache:", task.name)

    # La fonction run_task() éxécute une tache définie
    def run_task(self, task):
        for dependence in self.dependencies[task.name]:
            self.run_task(self.get_task_by_name(dependence)) 
        task.run()
        
    # Défition de la fonction get_task_by_name() qui renvoie l'objet tache en se basant sur le nomTache
    def get_task_by_name(self, task_name):
        # Find the task with the given name
        for task in self.tasks:
            if task.name == task_name:
                return task
            
    # run() permet l'éxécution parallèle des taches en tenant compte du parallélisme maximal des taches en utilisant un tri toptologique sur la liste des taches     
    def run(self):
        # Faire un tri topologique sur les taches
        order = self.topological_sort()
        # Execute each task in parallel if possible
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
                self.completed_tasks.append(task)

    # Définition de la fonction de tri topologique
    def topological_sort(self):
        # Le tri topologique  permet ici de determiner l'ordre d'execution des taches
        order = []
        ready = [task for task in self.tasks if not self.dependencies[task.name]]
        while ready:
            # Ajouter les taches pretes dans ordre
            order.append(ready)
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


    # * La fonction verifier_entrees permet de faire des analyses sur le systeme de tcahes task && contraintes
    def verifier_entrees(self,tasks, dependencies):
        # Vérifier l'unicité des noms des taches dans le systeme
        tasks_names = [task.name for task in tasks]
        if len(set(tasks_names)) != len(tasks_names):
            raise ValueError("Les noms des taches doivent etre uniques")
        else:
            print("Les taches sont uniques")

        #Vérifier si toutes les taches citées dans les contraintes sont bien existentes
        tasks_names_dep = set(dependencies.keys()).union(set([task for dep in dependencies.values() for task in dep]))
        if not tasks_names_dep.issubset(set(tasks_names)):
            raise ValueError("Le dictionnaire de précédence contient des nom de taches inexistentes")
        else:
            print("Toutes les noms des taches existent")

        # Vérification si toutes les tâches ont une précédente
        for task in tasks:
            if task.name not in dependencies and not task.precedentes:
                raise ValueError(f"La tâche {task.name} n'a pas de précédente")

        # Vérifier le déterminisme du système de taches
        tasks_names_orphelines = set(tasks_names).difference(tasks_names_dep)
        if len(tasks_names_orphelines) > 1:
            raise ValueError("Le système de tâches est indéterminé")
        else:
            print("Le sytème des taches est déterminé")

    # La fonction draw() permet de tracer le graphe d'éxécution des taches
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

    # Une fonction detRun() pour le determinisme
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
                    
        # Randomized test of determinism
        result1 = {}
        for task in self.tasks:
            result1[task.name] = task.result
        result2 = {}
        for task in self.tasks:
            task.reset()
            result2[task.name] = task.runRnd()
        if result1 != result2:
            print("The system is not deterministic")

    # Test de randomisation déterminé
    def detTestRnd(self, n=10):
        for i in range(n):
            self.detRun()
    
