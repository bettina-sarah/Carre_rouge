from tkinter import *
from Modele import *
from Controleur import *

class Vue():
    def __init__(self, controleur, modele):
        self.controleur = controleur
        self.modele = modele
        self.root = Tk()
        self.canvas = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur, borderwidth=50,  bg="black")
        self.canvas.pack()

        self.canvas2 = Canvas(self.canvas, height=self.modele.hauteur-200, width=self.modele.hauteur-200, borderwidth=50,
                             bg="red")
        self.canvas2.pack()
            # 50 epaisseur
        # frame = Frame(self.root, height=self.modele.hauteur, width=self.modele.hauteur, bg="seashell2")
        # frame.pack()
        # frame1 = Frame(frame, height=200, width=200, bg="red")
        # frame1.pack()
