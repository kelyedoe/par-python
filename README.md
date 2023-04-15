 ![Projet Système](/images/LibImage.png)

 
# 🔭 Projet: Librairie python de parallélisation maximale des tâches.
## ⏫ Description du projet:
Développer une libraire en Python pour automatiser la parallélisation maximale de systèmes de tâches. L’utilisateur doit pouvoir spécifier des tâches quelconques, interagissant
à travers un ensemble arbitraire de variables, et pouvoir :
1. obtenir le système de tâches de parallélisme maximal réunissant les tâches en entrées.
2. exécuter le système de tâches de façon séquentielle, tout en respectant les contraintes
de précédence.
3. exécuter le système de tâches en parallèle, tout en respectant les contraintes de
précédence.

# ⏫ Description

* **Task.py**: La class Task permet la création de tâches.

* **TaskSystemClass.py** : Le fichier TaskSystemClass.py regroupe l'ensemble des méthodes qui vont être exécutés pour réaliser le parallélisme maximal.

* **Test.py** : Le fichier test.py permet de tester les différentes fonctionnalitées que propose la librairie de parallélisation maximale.

* **Bonus.py** : contient le code python pour réaliser la partie bonus du projet.

# ⏫ Installation et Exécution du projet

## Dépendances
🔄 La librairie NetworkX
> $ pip install networkx

🔄 La librairie Matplotlib
>python -m pip install -U pip
>
>python -m pip install -U matplotlib
>

## Exécution du projet

**🔄La méthode getDependencies()**: permet de retourner la liste des tâches précédentes.

**🔄La méthode runSeq()**: permet de faire une exécution séquentielle des tâches à partir d'une tâche définie.

**🔄La méthode run_par()**: permet l'exécution parallèle des tâches en tenant compte du parallélisme maximal des tâches. Elle utilise **la méthode topological_sort()** pour gérer l'ordonancement des tâches.

**🔄La méthode verifier_entrees(self,tasks, dependencies)**: Elle prend en paramètre la liste des tâches et les contraintes de précédence sur le système de tâches. 
Cette méthode sera utilisée pour vérifier:
> - l'unicité des noms des tâches dans le système
> - vérifier si toutes les tâches citées dans les contraintes sont bien existentes
> - vérifier si toutes les tâches ont une tâche précédente
> - Vérifier si le système des tâches est déterminé c-à-d: pour toute tâche t1, t2 du système il n'y a pas d'interférence.

**🔄La méthode draw()**:
Cette méthode permet de tracer le graphe d'éxécution des tâches. Nous utilisons la librairie **networkx** et aussi la librairie **matplotlib** qui fourni un certain nombre de fonctions pour faire les représentations graphiques de notre système de tâches.

**🔄La méthode detTestRnd()**: Cette méthode permet de montrer si le système est déterminimé.
# ⏫ Exemple d'exécution du projet
L'exécution et les tests de la librairie se font dans le fichier **test.py**.

⚡1. **Création de 5 tâches t1, t2, t3, t4, t5**:
 ![Projet Système](/images/img1.png)


⚡2. **Créer un système de tâches**:
 ![système des tâches](/images/img2.png)

⚡3. **Vérification des contraintes sur le système des tâches**
 ![Projet Système](/images/img3.png)
> 😄Output
> - Les tâches sont uniques
> - Tous les noms des tâches existent
> - Le système des tâches est déterminé
>

⚡4.  **Application de la fonction getDependencies()**:
![Projet Système](/images/img4.png)

> 😄Output
> -  ['T2', 'T3']
>

⚡5. **Exécution de runSeq()**:
![Projet Système](/images/image4.png)
> 😄Output:
>
> - Finished task T1
> - Starting task T2
> - Finished task T2
> - Starting task T3
> - Finished task T3
>Starting task T4
> - Finished task T4
> - Starting task T5
> - Finished task T5

⚡6. **Exécution de la méthode run_par()**
![Projet Système](/images/img5.png)

> 😄 Output:
>
> - Starting task T1
> - Finished task T1
> - Starting task T2
> - Finished task T2
> - Starting task T3
> - Finished task T3
> - Starting task T4
> - Finished task T4
> - Starting task T5
> - Finished task T5
>

⚡7. **Exécution de la fonction de draw_no()**
![Projet Système](/images/img6.png)

⚡8. **Exécution de la fonction de draw_no()**
![Projet Système](/images/graphe2.png)

⚡9. **Test Randomisé de déterminisme**
![Projet Système](/images/testRand.png)

⚡10. **Coût du parallélisme**
![Projet Système](/images/parcost.png)

> 😄 Output
>
> - Finished task T4
> - Starting task T5
> - Finished task T5
> - Starting task T1
> - Starting task T2
> - Starting task T3
> - Starting task T4
> - Starting task T5
> - Finished task T5
> - Finished task T3
> - Finished task T4
> - Starting task T3
> - Finished task T3
> - Starting task T4
> - Finished task T4
> - Starting task T5
> - Finished task T5
> - Starting task T1
> - Starting task T2
> - Starting task T3
> - Starting task T4
> - Starting task T5
> - Finished task T3
> - Finished task T5
> - Finished task T4
> - Finished task T1
> - Finished task T2
> - Temps d'exécution moyen en séquentiel :  9.04371 secondes
> - Temps d'exécution moyen en parallèle :  9.04117 secondes
> - La différence de temps d'exécution est de :  0.00253 secondes
>

⚡11. **Bonus**

> **NB:** Une exécution du graphe 3 du TD. Après avoir appliqué les différentes méthodes de la librairie sur les systèmes S2 et S3 créés grâce aux graphes du TD, on peut déduire que le programme a bien pris en compte les nouveaux systèmes.

> Les tests des méthodes **runSeq()** et **run()** génèrent des erreurs ce qui prouvent que les graphes 2 et 3 ne sont pas exprimables en terme d'opérations de composition parallèle et séquentielle.

![Bonus](/images/bonus.png)
# ⏫ Crédits: