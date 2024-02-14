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

    def commencer_partie(self):
        self.jeu_en_cours = True
        self.temps_debut = datetime.now().time()
        # minute = self.temps_debut.minute
        # seconde = self.temps_debut.second
        # micro = self.temps_debut.microsecond

    def obtenir_leaderboard(self):
        # return tab results [] - fichier.csv (nom de session)
        # Trier?
        pass

    def creer_pions(self):
        self.carre = CarreRouge(self)
        self.rectangles.append(RectangleBleu(self, 60, 60, 100, 100, 4, 4, "red"))
        self.rectangles.append(RectangleBleu(self, 60, 50, 300, 85, -4, 4, "green"))
        self.rectangles.append(RectangleBleu(self, 100, 20, 355, 340, -4,-4, "yellow"))
        self.rectangles.append(RectangleBleu(self, 30, 60, 85, 350, 4,-4))

    def deplacer_rectangles(self):
        # dans les pions a place?
        for rectangle in self.rectangles:
            rectangle.deplacer()

    def changer_position(self, new_position):
        self.carre.changer_position(new_position)

    def verifier_collisions(self):
        return self.collision_bordure() or self.collision_rectangle()


    def collision_bordure(self):
        if self.carre.posX < self.border_width or self.carre.posX + self.carre.taille > self.largeur + self.border_width:
            return True

        if self.carre.posY < self.border_width or self.carre.posY + self.carre.taille > self.hauteur + self.border_width:
            return True
        return False

    def collision_rectangle(self):
        carre_x1 = self.carre.posX
        carre_x2 = self.carre.posX + self.carre.taille
        carre_y1 = self.carre.posY
        carre_y2 = self.carre.posY + self.carre.taille
        compteur_collision = 0

        for rectangle in self.rectangles:
            rect_x3 = rectangle.posX
            rect_x4 = rectangle.posX + rectangle.largeur
            rect_y3 = rectangle.posY
            rect_y4 = rectangle.posY + rectangle.hauteur
            if carre_x2 < rect_x3 or rect_x4 < carre_x1 or carre_y2 < rect_y3 or rect_y4 < carre_y1:
                compteur_collision+=1

        if compteur_collision == 4:
            return False
        return True


