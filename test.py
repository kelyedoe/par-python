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

# Définition d'une nouvelle tâche t1
t1 = Task()
t1.name = "T1"
t1.writes = ["X"]
t1.run = runT1

# Définition d'une nouvelle tâche t2
t2 = Task()
t2.name = "T2"
t2.writes = ["Y"]
t2.run = runT2

# Définition d'une nouvelle tâche t3
tSomme = Task()
tSomme.name = "somme"
tSomme.reads = ["X", "Y"]
tSomme.writes = ["Z"]
tSomme.run = runTsomme

t1.run()
t2.run()
tSomme.run()
""" print(X)
print(Y)
print(Z) """

# * La liste de dépendance entre les tâches
dependencies = {"T1": [], "T2": ["T1"], "somme": ["T1", "T2"]}
s1 = TaskSystem([t1, t2, tSomme], dependencies)
print(s1.tasks)

# * Cette méthode permet de vérifier les contraintes sur le système des taches
#s1.verifier_entrees([t1, t2, tSomme], dependencies)

# * Retourner la liste des dépendances en prenant nomTache en paramètre
#print(s1.getDependencies("somme"))

# * Exécution de la fonctionn runSeq() pour l'éxécution séquentielle des taches
#s1.runSeq()

#print(s1.run())

# * Cette méthode permet de générer le graphe du système de parallélisme maximal
# s1.draw()

s1.detTestRnd()





