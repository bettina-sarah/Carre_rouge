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

        self.dictio_coins = {"haut-gauche": [self.posX, self.posY],
                             "haut-droit": [self.posX+self.largeur, self.posY],
                             "bas-gauche": [self.posX, self.posY+self.hauteur],
                             "bas-droit": [self.posX+self.largeur, self.posX+self.hauteur],
                             }
        print("Coin haut-gauche", self.dictio_coins["haut-gauche"])
        print("Coin haut-droit", self.dictio_coins["haut-droit"])
        print("Coin bas-gauche", self.dictio_coins["bas-gauche"])
        print("Coin bas-droit", self.dictio_coins["bas-droit"])


    def deplacer(self):
        self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
        # print("new pos: ",self.posX, ", ",self.posY)

    # def trouver_destination(self):
    #     # profs:
    #     self.destinationX = random.randrange(self.parent.largeur)
    #     self.destinationY = random.randrange(self.parent.hauteur)
    #     self.angle = Helper.calcAngle(self.posX, self.posY, self.destinationX, self.destinationY)
