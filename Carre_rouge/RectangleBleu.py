import random
from helper import Helper as hp
class RectangleBleu():
    def __init__(self, modele, largeur, hauteur, posX, posY, angle, vitesse):
        self.parent = modele
        self.largeur = largeur;
        self.hauteur = hauteur
        # self.taille = taille
        self.posX = posX
        self.posY = posY
        self.vitesse = vitesse
        self.acceleration = 0.1
        self.couleur="blue"
        self.angle = 0.785398
        self.destinationX = None
        self.destinationY = None
        print("New rect")


    def deplacer(self):
        self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
        # print("new pos: ",self.posX, ", ",self.posY)

    # def trouver_destination(self):
    #     # profs:
    #     self.destinationX = random.randrange(self.parent.largeur)
    #     self.destinationY = random.randrange(self.parent.hauteur)
    #     self.angle = Helper.calcAngle(self.posX, self.posY, self.destinationX, self.destinationY)
