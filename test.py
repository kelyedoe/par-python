from TaskClass import *
from TaskSystemClass import *

# Initialisation de 5 taches à partir de la classe TaskClass
t1 = Task('T1', dependencies=[], duration= 2)
t2 = Task('T2', dependencies=['T1'], duration= 3)
t3 = Task('T3', dependencies=['T2'], duration =1)
t4 = Task('T4', dependencies=['T1'], duration= 2)
t5 = Task('T5', dependencies=['T4', 'T3'], duration = 1)


# * La liste de dépendance entre les tâches 
dependencies = {"T1": [], "T2": ["T1"], "T3": ["T2"],"T4": ["T2", "T3"],"T5": ["T4"]}
dep = {"T1": [], "T2": ["T1"], "T3": ["T2"],"T4": ["T2", "T3"],"T5": ["T4"]}

# * la liste des taches
tasks = [t1, t2, t3, t4, t5]

# * Créer un système des taches
s1 = TaskSystem(tasks=tasks, dependencies=dependencies)

# * Cette méthode permet de vérifier les contraintes sur le système des tâches
#s1.verifier_entrees([t1, t2, t3, t4, t5], dependencies)

# * Retourner la liste des dépendances en prenant nomTache en paramètre
dependances =  s1.getDependencies("T4")
#print(dependances)

# * Exécution de la fonctionn runSeq() pour l'exécution séquentielle des tâches
#s1.runSeq()

# * Exécution de la fonction run_par() pour l'exécution parallèle des tâches
#s1.run_par()

# * Cette méthode permet de générer le graphe du système 
#s1.draw_no()

# * Cette méthode permet de générer le graphe du système de parallélisme maximal
#s1.draw()

# * Test  randomisé de déterminisme  (Valide)
#s1.detTestRnd(2)

# * Coût du parallélisme
s1.parCost()






