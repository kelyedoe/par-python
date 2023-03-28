# todo: verification sur les entrées

def verifier_entrées(taches, contraintes):
    # Vérification si les noms des tâches sont uniques
    noms_taches = [tache.nom for tache in taches]
    if len(set(noms_taches)) != len(noms_taches):
        raise ValueError("Les noms des tâches doivent être uniques")

    # Vérification si toutes les tâches citées dans les contraintes existent
    noms_taches_contraintes = set(contraintes.keys()).union(set([tache for prec in contraintes.values() for tache in prec]))
    if not noms_taches_contraintes.issubset(set(noms_taches)):
        raise ValueError("Le dictionnaire de précédence contient des noms de tâches inexistantes")

    # Vérification si toutes les tâches ont une précédente
    for tache in taches:
        if tache.nom not in contraintes and not tache.precedentes:
            raise ValueError(f"La tâche {tache.nom} n'a pas de précédente")

    # Vérification si le système de tâches est déterminé
    noms_taches_orphelines = set(noms_taches).difference(noms_taches_contraintes)
    if len(noms_taches_orphelines) > 1:
        raise ValueError("Le système de tâches est indéterminé")



    

