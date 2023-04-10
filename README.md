 ![Projet Système](/images/LibImage.png)

 
# Projet: Librairie python de parallélisation maximale des tâches. 

## Description du projet:
Développer une libraire en Python pour automatiser la parallélisation maximale de systèmes de tâches. L’utilisateur doit pouvoir spécifier des tâches quelconques, interagissant
à travers un ensemble arbitraire de variables, et pouvoir :
1. obtenir le système de tâches de parallélisme maximal réunissant les tâches en entrée,
2. exécuter le système de tâches de façon séquentielle, tout en respectant les contraintes
de précédence,
3. exécuter le système de tâches en parallèle, tout en respectant les contraintes de
précédence.

# Description 

* **Task.py**: La class Task permet la création de tâches.

* **TaskSystemClass.py** : Le fichier TaskSystemClass.py regroupe l'ensemble de fonction qui vont être exécutés pour réaliser le parallélisme maximal. 

* **Test.py** : Le fichier test.py permet de tester les différentes fonctionnalitées que propose la librairie de parallélisation maximale.
# Installation et Exécution du projet

**La méthode getDependencies()**: permet de retourner la liste des tâches précédentes.

**La méthode runSeq()**: permet de faire une exécution séquentielle des tâches à partir d'une tâche définie.

**La méthode run()**: permet l'exécution parallèle des tâches en tenant compte du parallélisme maximal des tâches. Elle utilise **la méthode topological_sort()** pour gérer l'ordonancement des tâches.

**La méthode verifier_entrees(self,tasks, dependencies)**: Elle prend en paramètre la liste des tâches et les contraintes de précédence sur le système de tâches. 
Cette méthode sera utilisée pour vérifier:
> - l'unicité des noms des tâches dans le système
> - Vérifier si toutes les tâches citées dans les contraintes sont bien existentes
> - vérifier si toutes les tâches ont une tâche précédente
> - Vérifier si le système des tâches est déterminé c-à-d: pour toute tâche t1, t2 du système il n'y a pas d'interférence.

**La méthode draw()**:
Cette méthode permet de tracer le graphe d'éxécution des tâches. Nous utilisons la librairie **networkx** et aussi la librairie **matplotlib** qui fourni un certain nombre de fonctions pour faire les représentation graphique de notre système de tâches.

**La méthode detRun()**: Cette méthode permet de montrer si le système est déterminimé.
# Exemple d'exécution du projet
L'éxécution et les test de la librarie se font dans le fichier **test.py**.

1. **Création des tâches t1, t2, t3**:
 ![Projet Système](/images/tasks.png)

2. **Créer un système de tâches**:
 ![système des tâches](/images/syst%C3%A8me%20des%20taches.png)

3. **Vérification des contraintes sur le système des taches**
 ![Projet Système](/images/verification.png)
> Output
> - Les tâches sont uniques
> - Toutes les noms des tâches existent
> - Le système des tâches est déterminé
>

 4.  **Application de la fonction getDependencies()**:
![Projet Système](/images/image3.png)

5. **Exécution de runSeq()**:
![Projet Système](/images/image4.png)
> Output:
> - Exécution de la tâche: T1
> - Exécution de la tâche: T2
> - Exécution de la tâche: somme

6. **Exécution de la méthode run()**

7. **Exécution de la fonction de draw()**
![Projet Système](/images/Figure_1.png)


# Crédits: