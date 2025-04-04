**Rapport détaillé : Algorithme glouton pour la minimisation des coûts de stockage**

### 1. Introduction
Ce projet implémente un algorithme glouton pour résoudre un problème de dimensionnement de lots multi-produits avec une capacité de production limitée à une unité par période. L’objectif est de minimiser les coûts de stockage en affectant les productions de manière optimale.

### 2. Problématique
Le problème se pose dans le cadre d’un environnement où chaque article a une demande spécifiée sur plusieurs périodes. Le coût de stockage est proportionnel au nombre de périodes entre la date de production et la date d’échéance. L’algorithme doit donc organiser la production de manière à réduire ces coûts.

### 3. Approche utilisée
Nous avons adopté une approche **gloutonne**, qui consiste à toujours prendre la décision la plus avantageuse à chaque étape, sans garantie d’optimalité globale mais avec une efficacité computationnelle élevée. L’algorithme fonctionne en :
- Identifiant les demandes pour chaque période.
- Planifiant la production en commençant par la dernière demande enregistrée et en remontant dans le temps.
- Réduisant le coût de stockage en minimisant le décalage entre production et échéance.

### 4. Implémentation détaillée

#### 4.1 Vérification de la faisabilité (`isFeasible`)
Avant d’exécuter l’algorithme, on s’assure que le problème est bien défini, c’est-à-dire qu’aucune période ne dépasse la capacité de production d’une unité par période.

**Pseudo-code :**
```
fonction isFeasible(n, d):
    pour chaque période k:
        somme_demandes = somme(d[i][k] pour i dans [0, n-1])
        si somme_demandes > 1:
            retourner Faux
    retourner Vrai
```

#### 4.2 Calcul du coût de stockage optimal (`optStockingCost`)
Cette fonction :
- Vérifie la faisabilité.
- Identifie toutes les demandes et les ordonne par priorité.
- Applique l’algorithme glouton pour minimiser le coût en remontant la timeline de production.
- Retourne le coût total et le plan de production optimal.

**Pseudo-code :**
```
fonction optStockingCost(n, d):
    si isFeasible(n, d) est Faux:
        lever une exception
    
    Initialiser liste des demandes
    Pour chaque période k:
        Pour chaque item i:
            Si item i a une demande à période k:
                Ajouter k à la liste des demandes
    
    Initialiser le coût h = 0
    Définir t comme dernière période de demande
    Tant que la liste des demandes n’est pas vide:
        deadline = dernier élément de la liste des demandes
        Si deadline >= t:
            h += (deadline - t)
        t -= 1
    
    Retourner h
```

#### 4.3 Prise en compte de coûts variables (`optStockingCost_IDS`)
Une extension permet d’intégrer des coûts de stockage différents par article. L’algorithme prend en compte ces coûts pour prioriser les productions de manière plus réaliste.

**Pseudo-code :**
```
fonction optStockingCost_IDS(n, d, stockingCostByItem):
    si isFeasible(n, d) est Faux:
        lever une exception
    
    Initialiser liste des demandes
    Pour chaque item i:
        Pour chaque période k:
            Si item i a une demande à période k:
                Ajouter (i, k) à la liste des demandes
    
    Trier la liste des demandes par ordre décroissant des périodes
    Initialiser le coût h = 0
    Définir t comme la dernière période de demande
    Tant que la liste des demandes n’est pas vide:
        (item, deadline) = dernier élément de la liste des demandes
        Si deadline >= t:
            h += (deadline - t) * stockingCostByItem[item]
        t -= 1
    
    Retourner h
```

### 5. Résultats et analyse
Les tests montrent que l’algorithme est efficace pour des petites instances et offre un bon compromis entre simplicité et performance. Toutefois, une extension utilisant des approches d’optimisation plus avancées pourrait être envisagée pour des cas complexes.

### 6. Perspectives d’amélioration
- Intégrer un solveur d’optimisation pour valider l’optimalité des résultats.
- Tester l’algorithme sur de grandes instances.

### 7. Conclusion
L’algorithme glouton proposé offre une solution rapide et efficace pour le problème de minimisation des coûts de stockage. Son implémentation modulaire permet une extension future vers des versions plus complexes avec des contraintes additionnelles.

