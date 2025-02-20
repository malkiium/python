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

class Wagon:
    def __init__(self, contenu):
        self.contenu = contenu
        self.suivant = None
    def __str__(self):
        return self.contenu
    def __repr__(self):
        return self.contenu


class Train:
    def __init__(self):
        self.premier = None
        self.nb_wagons = 0
    def est_vide(self):
        return self.premier is None
    def donne_nb_wagons(self):
        return self.nb_wagons
    def transporte_du(self, contenu):
        wagon = self.premier
        while wagon is not None:
            if wagon.contenu == contenu:
                return True
            wagon = wagon.suivant
        return False
    def ajoute_wagon(self, wagon):
        if self.premier is None:
            self.premier = wagon
        else:
            dernier = self.premier
            while dernier.suivant is not None:
                dernier = dernier.suivant
            dernier.suivant = wagon
        self.nb_wagons += 1
    def supprime_wagon_de(self, contenu):
        if self.premier is None:
            return False
        if self.premier.contenu == contenu:
            self.premier = self.premier.suivant
            self.nb_wagons -= 1
            return True
        precedent = self.premier
        wagon = precedent.suivant
        while wagon is not None:
            if wagon.contenu == contenu:
                precedent.suivant = wagon.suivant
                self.nb_wagons -= 1
                return True
            precedent = wagon
            wagon = wagon.suivant
        return False
    def __str__(self):
        if self.premier is None:
            return "Train vide"
        wagon = self.premier
        chaine = "Locomotive - " + str(wagon)
        wagon = wagon.suivant
        while wagon is not None:
            chaine += " - " + str(wagon)
            wagon = wagon.suivant
        return chaine
    def __repr__(self):
        return str(self)