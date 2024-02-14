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

        print("Coin haut-gauche", self.dictio_coins["haut-gauche"])
        print("Coin haut-droit", self.dictio_coins["haut-droit"])
        print("Coin bas-gauche", self.dictio_coins["bas-gauche"])
        print("Coin bas-droit", self.dictio_coins["bas-droit"])

    def changer_position(self, new_position):
        x, y = new_position
        self.posX, self.posY = x-self.taille/2, y-self.taille/2
        #print("nouvelle:", self.posX, self.posY)

