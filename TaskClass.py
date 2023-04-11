# La classe Task permet la création des tâches T1 T2 T3
class Task:
    name =""
    reads = []
    writes = []
    #run = None
    is_finished = False
    
    def run(self):
        pass

    def isFinished(self):
        return self.is_finished
