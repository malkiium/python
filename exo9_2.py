"""On souhaite dans cet exercice créer une classe Train permettant de relier des objets de type
Wagon.
Un objet de type Wagon possède deux attributs :
• un contenu contenu de type str,
• un attribut suivant de type Wagon contenant une référence vers le wagon suivant.
On inclut aussi deux méthodes permettant d'afficher le wagon sous forme d'une chaîne de caractère.
Un objet de la classe Train possède deux attributs :
• premier contient son premier wagon (de type Wagon) ou None si le train est vide (il n'y a
que la locomotive),
• nb_wagons (de type int) contient le nombre de wagons attachés à la locomotive.
Lors de sa création, un objet de type Train n’a aucun wagon.
Les méthodes de la classe Train sont présentées ci-dessous (train est un objet de type Train) :
• train.est_vide() renvoie True si train est vide (ne comporte aucun wagon),
False sinon ;
• train.donne_nb_wagons() renvoie le nombre de wagons de train ;
• train.transporte_du(contenu) détermine si train transporte du contenu (une
chaine de caractères). Renvoie True si c'est le cas, False sinon ;
• train.ajoute_wagon(wagon) ajoute un wagon à la fin du train. On passe en
argument le wagon à ajouter ;
• train.supprime_wagon_de(contenu) prend en argument une chaîne de caractères
contenu et supprime le premier wagon de contenu du train. Si le train est vide ou ne
comporte aucun wagon de contenu, la méthode renvoie False. S'il en contient un et que
celui-ci est effectivement supprimé, la méthode renvoie True.
On inclut là-aussi aussi deux méthodes permettant d'afficher le train dans la console ou sous forme
d'une chaîne de caractères. """

