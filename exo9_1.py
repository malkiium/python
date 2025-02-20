"""On souhaite dans cet exercice créer une classe Chien ayant deux attributs :
• un nom nom de type str,
• un poids poids de type float.
Cette classe possède aussi différentes méthodes décrites ci-dessous (chien est un objet de type
Chien) :
• chien.donne_nom() qui renvoie la valeur de l'attribut nom ;
• chien.donne_poids() qui renvoie la valeur de l'attribut poids ;
• chien.machouille(jouet) qui renvoie son argument, la chaîne de caractères
jouet, privé de son dernier caractère ;
• chien.aboie(nb_fois) qui renvoie la chaîne 'Ouaf' * nb_fois, où nb_fois
est un entier passé en argument ;
• chien.mange(ration) qui modifie l'attribut poids en lui ajoutant la valeur de
l'argument ration (de type float).
On ajoute les contraintes suivantes concernant la méthode mange :
• on vérifiera que la valeur de ration est comprise entre 0 (exclu) et un dixième du poids du
chien (inclus),
• la méthode renverra True si ration satisfait ces conditions et que l'attribut poids est
bien modifié, False dans le cas contraire. """


class Chien:
    def __init__(self, nom:str, poids:float):
        self.nom = nom
        self.poids = poids

    def donne_nom(self):
        return self.nom
    
    def donne_poids(self):
        return self.poids
    
    def machouille(self, mot:str):
        return mot[:-1]
    
    def aboie(self, nb_fois:int):
        return "Ouaf " * nb_fois
    
    def mange(self, ration:float):
        if 0 < ration <= self.poids/10:
            self.poids += ration
            return True