class CarreRouge():
    def __init__(self, modele):
        self.parent = modele
        self.taille = 40 # ? a modifier
        self.posX = self.parent.largeur/2
        self.posY = self.parent.hauteur/2
        self.couleur = "red"


    def changer_position(self, new_position):
        self.posX, self.posY = new_position
        print("nouvelle:", self.posX, self.posY)

