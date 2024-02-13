from CarreRouge import *
from RectangleBleu import *
from datetime import datetime


class Modele:
    def __init__(self, controleur):
        self.controleur = controleur
        self.border_width = 50
        self.hauteur = 450
        self.largeur = 450
        self.rectangles = []
        self.carre = None
        self.jeu_en_cours = False
        self.temps_debut = None

    def changer_position(self, new_position):
        self.carre.changer_position(new_position)

    def obtenir_leaderboard(self):
        # return tab results [] - fichier.csv (nom de session)
        # Trier?
        pass

    def creer_pions(self):
        self.carre = CarreRouge(self)
        self.rectangles.append(RectangleBleu(self, 60, 60, 100, 100,  0.785398, 5))
        self.rectangles.append(RectangleBleu(self, 60, 50, 300, 85, 0.785398, -5))
        self.rectangles.append(RectangleBleu(self, 100, 20, 355, 340, 0.785398, 5))
        self.rectangles.append(RectangleBleu(self, 30, 60, 85, 350, 0.785398, -5))
        # self.pions.append()
        pass

    def deplacer_rectangles(self):
        # dans les pions a place?
        for pion in self.rectangles:
            pion.deplacer()
        pass

    def reset_position(self):
        # position initiale
        pass

    def verifier_collision(self):
        pass

    def commencer_partie(self):
        self.jeu_en_cours = True
        self.temps_debut = datetime.now().time()
        # minute = self.temps_debut.minute
        # seconde = self.temps_debut.second
        # micro = self.temps_debut.microsecond




