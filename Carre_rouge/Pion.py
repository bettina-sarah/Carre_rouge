import random
from helper import Helper
class Pion():
    def __init__(self, modele, taille, posX, posY):
        self.parent = modele
        self.taille = taille
        self.posX = posX
        self.posY = posY
        self.vitesse = 2
        self.acceleration = 0.1
        self.angle = None
        self.destinationX = None
        self.destinationY = None
        pass

    def deplacer(self):
        pass

    def trouver_destination(self):
        # profs:
        self.destinationX = random.randrange(self.parent.largeur)
        self.destinationY = random.randrange(self.parent.hauteur)
        self.angle = Helper.calcAngle(self.posX, self.posY, self.destinationX, self.destinationY)
        pass