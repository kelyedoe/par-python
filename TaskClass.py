# La classe Task permet la création des tâches T1 T2 T3
class Task:
    def __init__(self, name, dependencies, duration):
        self.name = name
        self.dependencies = dependencies
        self.duration = duration
        self.vars = []
        #run = None
        is_finished = False
        
    def addVar(self, var):
        self.vars.append(var)
    
    def run(self):
        is_finished = True
        import time
        print(f"Starting task {self.name}")
        self.start_time = time.time()
        time.sleep(self.duration)
        self.end_time = time.time()
        print(f"Finished task {self.name}")

    def isFinished(self):
        # Here we would check if the task has finished executing
        # For demonstration purposes, we will just return True after sleeping for the duration of the task
        import time
        time.sleep(self.duration)
        return True
