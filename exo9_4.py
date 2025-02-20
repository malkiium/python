class Velo:
    def __init__(self, modele: str, genre: str):
        if modele not in ['VILLE', 'VTT', 'VTC']:
            raise ValueError("Modèle invalide. Choisissez parmi 'VILLE', 'VTT', 'VTC'.")
        if genre not in ['HOMME', 'FEMME']:
            raise ValueError("Genre invalide. Choisissez entre 'HOMME' et 'FEMME'.")
        
        self.modele = modele
        self.genre = genre

    def isFeminin(self) -> bool:
        return self.genre == 'FEMME'

    def __str__(self) -> str:
        return f"Modèle : {self.modele}, Genre : {self.genre}"

class VeloElectrique(Velo):
    def __init__(self, modele: str, genre: str, autonomie: int):
        super().__init__(modele, genre)
        if autonomie < 0:
            raise ValueError("L'autonomie doit être un nombre positif.")
        self.autonomie = autonomie
    
    def isLongueDistance(self) -> bool:
        return self.autonomie > 100
    
    def __str__(self) -> str:
        return f"{super().__str__()}, Autonomie : {self.autonomie} km"