class CarreRouge():
    def __init__(self, modele):
        self.parent = modele
        self.taille = 40 # ? a modifier
        self.posX = self.parent.largeur/2
        self.posY = self.parent.hauteur/2
        self.couleur = "red"


    def changer_position(self, new_position):
        x, y = new_position
        self.posX, self.posY = x-self.taille/2, y-self.taille/2
        print("nouvelle:", self.posX, self.posY)

