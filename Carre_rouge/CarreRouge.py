class CarreRouge():
    def __init__(self, modele):
        self.parent = modele
        self.taille = 40 # ? a modifier
        self.posX = self.parent.largeur/2
        self.posY = self.parent.hauteur/2
        self.couleur = "red"
        self.dictio_coins = {"haut-gauche": [self.posX, self.posY],
                             "haut-droit": [self.posX+self.taille, self.posY],
                             "bas-gauche": [self.posX, self.posY+self.taille],
                             "bas-droit": [self.posX+self.taille, self.posY+self.taille],
                             }

    def deplacer(self, new_position):
        x, y = new_position
        self.posX, self.posY = x-self.taille/2, y-self.taille/2
        #print("nouvelle:", self.posX, self.posY)

