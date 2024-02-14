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

        self.coins = {"haut-gauche": [self.posX, self.posY],
                             "haut-droit": [self.posX + self.largeur, self.posY],
                             "bas-gauche": [self.posX, self.posY + self.hauteur],
                             "bas-droit": [self.posX + self.largeur, self.posY+ self.hauteur],
                             }

    # def deplacer_angle(self):
    # self.angle = hp.calcAngle(self.posX, self.posY,self.parent.largeur/2, self.parent.largeur/2)
    # self.posX, self.posY = hp.getAngledPoint(self.angle, self.vitesse, self.posX, self.posY)
    # print("new pos: ",self.posX, ", ",self.posY)

    def deplacer(self):

        self.collision_mur()
        if self.vitesseX < 0:
            self.vitesseX += self.acceleration * -1
        else:
            self.vitesseX += self.acceleration

        if self.vitesseY < 0:
            self.vitesseY += self.acceleration * -1
        else:
            self.vitesseY += self.acceleration

        self.posX += self.vitesseX
        self.posY += self.vitesseY

    def collision_mur(self):

        if self.posX < 0 or self.posX + self.largeur > self.parent.largeur + self.parent.border_width*2:

            self.vitesseX*=-1

        if self.posY < 0 or self.posY + self.hauteur > self.parent.hauteur+self.parent.border_width*2:
            self.vitesseY*=-1


    def acceleration(self):
        pass


    # def trouver_destination(self):
    #     # profs:
    #     self.destinationX = random.randrange(self.parent.largeur)
    #     self.destinationY = random.randrange(self.parent.hauteur)
    #     self.angle = Helper.calcAngle(self.posX, self.posY, self.destinationX, self.destinationY)
