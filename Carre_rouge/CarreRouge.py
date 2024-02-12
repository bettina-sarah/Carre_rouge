class CarreRouge():
    def __init__(self, modele):
        self.parent = modele
        self.taille = 30 # ? a modifier
        self.posX = 225
        self.posY = 225
        pass

    def deplacer(self, evt):
        # binder au canvas de l'aire de jeu,
        # utilise l'event pour déterminer la position du curseur et si
        # le joueur déplace le carré
        pass