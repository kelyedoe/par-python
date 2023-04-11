from TaskClass import *
from TaskSystemClass import *

t1 = Task()
t1.name = "T1"

t2 = Task()
t2.name = "T2"

t3 = Task()
t3.name = "T3"

t4 = Task()
t4.name = "T4"

t5 = Task()
t5.name = "T5"


t6 = Task()
t6.name = "T6"


t7 = Task()
t7.name = "T7"


t8 = Task()
t8.name = "T8"

# * La liste de dépendance entre les tâches
dependenciesGraphe2 = {"T1": [], "T2": ["T1"], "T3": ["T1"], "T4":["T1"], "T5":["T2", "T3"], "T6":["T4", "T2"], "T7":["T3", "T4"], "T8":["T5", "T6", "T7"]}

dependenciesGraphe4 = {"T1": [], "T2": ["T1"], "T3": ["T1"], "T4":["T1"], "T5":["T2", "T3"], "T6":["T3", "T4"], "T7":["T4"], "T8":["T5", "T6", "T7"]}

s2 = TaskSystem([t1, t2, t3, t4, t5, t6, t7, t8], dependenciesGraphe2)

s3 = TaskSystem([t1, t2, t3, t4, t5, t6, t7, t8], dependenciesGraphe4)

print(s2.tasks)

print(s3.tasks)

s2.verifier_entrees([t1, t2, t3, t4, t5, t6, t7, t8], dependenciesGraphe2)

s3.verifier_entrees([t1, t2, t3, t4, t5, t6, t7, t8], dependenciesGraphe4)

s2.runSeq()

s3.runSeq()