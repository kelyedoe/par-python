from TaskClass import *
from TaskSystemClass import *


# Initialisation de 5 taches à partir de la classe TaskClass
t1 = Task('T1', dependencies=[], duration= 2)
t2 = Task('T2', dependencies=['T1'], duration= 3)
t3 = Task('T3', dependencies=["T1"], duration =1)
t4 = Task('T4', dependencies=["T1"], duration= 2)
t5 = Task('T5', dependencies=["T2", "T3"], duration = 1)
t6 = Task('T5', dependencies=["T4", "T2"], duration = 2)
t7 = Task('T5', dependencies=['T4', 'T3'], duration = 1)
t8 = Task('T5', dependencies=["T5", "T6", "T7"], duration = 3)


# * La liste de dépendance entre les tâches
dependenciesGraphe2 = {"T1": [], "T2": ["T1"], "T3": ["T1"], "T4":["T1"], "T5":["T2", "T3"], "T6":["T4", "T2"], "T7":["T3", "T4"], "T8":["T5", "T6", "T7"]}

dependenciesGraphe4 = {"T1": [], "T2": ["T1"], "T3": ["T1"], "T4":["T1"], "T5":["T2", "T3"], "T6":["T3", "T4"], "T7":["T4"], "T8":["T5", "T6", "T7"]}

s2 = TaskSystem([t1, t2, t3, t4, t5, t6, t7, t8], dependenciesGraphe2)
s2.runSeq()

#s2.draw()
#s3 = TaskSystem([t1, t2, t3, t4, t5, t6, t7, t8], dependenciesGraphe4)

#print(s2.tasks)

#print(s3.tasks)

#s2.runSeq()
#s2.verifier_entrees([t1, t2, t3, t4, t5, t6, t7, t8], dependenciesGraphe2)

#s3.verifier_entrees([t1, t2, t3, t4, t5, t6, t7, t8], dependenciesGraphe4)



#s3.runSeq()
