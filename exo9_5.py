class Auteur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def __eq__(self, other):
        if isinstance(other, Auteur):
            return self.nom == other.nom and self.prenom == other.prenom
        return False

    def __hash__(self):
        return (hash(self.nom) * 7) + hash(self.prenom)


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def get_titre(self):
        return self.titre

    def get_auteur(self):
        return self.auteur

    def __str__(self):
        return f"{self.titre} de {self.auteur}"

    def __eq__(self, other):
        if isinstance(other, Livre):
            return self.titre == other.titre and self.auteur == other.auteur
        return False

    def __hash__(self):
        return (hash(self.titre) * 7) + hash(self.auteur)


class BD(Livre):  # BD hérite de Livre
    def __init__(self, titre, auteur, dessinateur):
        super().__init__(titre, auteur)
        self.dessinateur = dessinateur  # Nouveau champ

    def __str__(self):
        return f"{self.titre} de {self.auteur} (dessiné par {self.dessinateur})"

    def __eq__(self, other):
        if isinstance(other, BD):
            return super().__eq__(other) and self.dessinateur == other.dessinateur
        return False

    def __hash__(self):
        return super().__hash__() + hash(self.dessinateur)


class Bibliotheque:
    def __init__(self):
        self.livres = set()

    def ajouter(self, livre):
        self.livres.add(livre)

    def getNbLivres(self):
        return len(self.livres)

    def rechercherTitre(self, titre):
        for livre in self.livres:
            if livre.get_titre().lower() == titre.lower():
                return str(livre)  # Retourne la représentation en chaîne de caractères
        return None

    def rechercherMot(self, mot):
        mot = mot.lower()
        return {livre.get_titre() for livre in self.livres if mot in livre.get_titre().lower()}

    def rechercherAuteur(self, nom, prenom):
        return {livre for livre in self.livres if livre.get_auteur() == Auteur(nom, prenom)}

    def rechercherDessinateur(self, nom):
        return {livre for livre in self.livres if isinstance(livre, BD) and livre.dessinateur.lower() == nom.lower()}

    def __str__(self):
        if not self.livres:
            return "La bibliothèque est vide."
        return "Livres dans la bibliothèque :\n" + "\n".join(str(livre) for livre in self.livres)


# --- TEST DU PROGRAMME ---

# Création des auteurs
# --- Création des auteurs ---
auteur1 = Auteur("Hugo", "Victor")
auteur2 = Auteur("Camus", "Albert")
auteur3 = Auteur("Zola", "Émile")
auteur4 = Auteur("Süskind", "Patrick")
auteur5 = Auteur("Goscinny", "René")

# --- Création des livres ---
livre1 = Livre("Les Misérables", auteur1)
livre2 = Livre("L'Étranger", auteur2)
livre3 = Livre("Germinal", auteur3)
livre4 = Livre("Le Parfum", auteur4)
livre5 = Livre("Notre-Dame de Paris", auteur1)

# --- Création des bandes dessinées ---
bd1 = BD("Astérix et Obélix", auteur5, "Uderzo")
bd2 = BD("Lucky Luke", auteur5, "Morris")
bd3 = BD("Tintin au Tibet", Auteur("Hergé", ""), "Hergé")
bd4 = BD("Astérix et Obélix", auteur5, "Uderzo")  # Doublon

# --- Création de la bibliothèque et ajout des livres/BD ---
biblio = Bibliotheque()
biblio.ajouter(livre1)
biblio.ajouter(livre2)
biblio.ajouter(livre3)
biblio.ajouter(livre4)
biblio.ajouter(livre5)
biblio.ajouter(bd1)
biblio.ajouter(bd2)
biblio.ajouter(bd3)
biblio.ajouter(bd4)  # Ne sera pas ajouté car c'est un doublon
