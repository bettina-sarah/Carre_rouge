from CarreRouge import *
from Pion import *


class Modele:
    def __init__(self, controleur):
        self.controleur = controleur
        self.border_width = 50
        self.hauteur = 450
        self.largeur = 450
        self.pions = []
        self.carre = CarreRouge(self)

    def obtenir_leaderboard(self):
        # return tab results [] - fichier.csv (nom de session)
        # Trier?
        pass

    def creer_pions(self):
        # 4 pions
        # self.pions.append()
        pass

    def deplacer_pions(self):
        # dans les pions a place?
        for pion in self.pions:
            pion.deplacer()
        pass

    def reset_position(self):
        # position initiale
        pass

    def verifier_collision(self):
        pass




