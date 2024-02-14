import random
from helper import Helper as hp
class RectangleBleu():
    def __init__(self, modele, largeur, hauteur, posX, posY, vitesseX, vitesseY, couleur="blue"):
        self.parent = modele
        self.largeur = largeur
        self.hauteur = hauteur
        self.posX = posX
        self.posY = posY
        self.vitesseX = vitesseX
        self.vitesseY = vitesseY
        self.acceleration = 0.1
        self.couleur = couleur
        self.angle = None
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


# def deplacer_angle(self):
        # self.angle = hp.calcAngle(self.posX, self.posY,self.parent.largeur/2, self.parent.largeur/2)
        # self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
        # print("new pos: ",self.posX, ", ",self.posY)

    def deplacer(self):

        if self.vitesseX < 0:
            self.vitesseX += self.acceleration*-1
        else:
            self.vitesseX += self.acceleration*1

        if self.vitesseY < 0:
            self.vitesseY += self.acceleration*-1
        else:
            self.vitesseY += self.acceleration*1
        self.posX += self.vitesseX
        self.posY += self.vitesseY



    # def trouver_destination(self):
    #     # profs:
    #     self.destinationX = random.randrange(self.parent.largeur)
    #     self.destinationY = random.randrange(self.parent.hauteur)
    #     self.angle = Helper.calcAngle(self.posX, self.posY, self.destinationX, self.destinationY)
