from threading import Thread
import networkx as nx
import matplotlib.pyplot as plt


class TaskSystem:

    def __init__(self, tasks, dependencies):
        self.tasks = tasks
        self.dependencies = dependencies
        self.completed_tasks = []
    
    def getDependencies(self, task_name):
        return self.dependencies[task_name]
    
    def runSeq(self):
        for task in self.tasks:
            self.run_task(task)
            print("Exécution de la tache:", task.name)

    def run_task(self, task):
        for dependence in self.dependencies[task.name]:
            self.run_task(self.get_task_by_name(dependence)) 
        task.run()
        

    def get_task_by_name(self, task_name):
        # Find the task with the given name
        for task in self.tasks:
            if task.name == task_name:
                return task
            
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


    def run(self):
        G = nx.DiGraph()
        G.add_nodes_from(self.tasks)
        
        for task in self.tasks:
            dependencies = self.getDependencies(task)
            for dependency in dependencies:
                G.add_edge(dependency, task)
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        plt.show()
    
