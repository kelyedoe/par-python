from TaskClass import *
from TaskSystemClass import *

# Définition de variables selon l'énoncé du projet
X = None
Y = None
Z = None

# Comportement de T1
def runT1():
    global X
    X = 1
# Comportement de T2
def runT2():
    global Y
    Y = 2
# Comportement de T3
def runTsomme():
    global X, Y, Z
    Z = X + Y

t1 = Task('T1',dependencies=[], duration= 2)
t2 = Task('T2', dependencies=['T1'], duration= 3)
t3 = Task('T3', duration =1, dependencies=['T2'])
t4 = Task('T4', duration= 2, dependencies=['T1'])
t5 = Task('T5', duration = 1, dependencies=['T4', 'T3'])


# * La liste de dépendance entre les tâches
dependencies = {"T1": [], "T2": ["T1"], "T3": ["T2"],"T4": ["T2", "T3"],"T5": ["T4"]}

# * Créer un système des taches
s1 = TaskSystem([t1, t2, t3, t4, t5], dependencies)

#print(s1.tasks)

#print(s1.get_task_by_name("T1"))

# * Cette méthode permet de vérifier les contraintes sur le système des tâches
#s1.verifier_entrees([t1, t2, t3, t4, t5], dependencies)
#s2.verifier_entrees([t1, t2, tSomme], depend)

# * Retourner la liste des dépendances en prenant nomTache en paramètre
#print(s1.getDependencies("T4"))
#print(s2.getDependencies("somme"))

# * Exécution de la fonctionn runSeq() pour l'exécution séquentielle des tâches
# s1.runSeq()
# s2.runSeq()

# * Exécution de la fonctionn run() pour l'exécution parallèle des tâches
# s1.run()
#s2.run()

# * Cette méthode permet de générer le graphe du système de parallélisme maximal
#s1.draw()

# * Test  randomisé de déterminisme  (Valide)
#s1.detTestRnd(2)

# * Coût du parallélisme
#s1.parCost()

# * retourner l'ordre d'éxécution suivant le tri topologique
#s1.runSeq()
#s1.run_par()
s1.parCost()

#s1.topological_sorty()
#s1.run()

s1.parCost()





