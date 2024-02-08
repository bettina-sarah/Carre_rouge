from tkinter import *
from Modele import *
from Controleur import *

class Vue():
    def __init__(self, controleur, modele):
        self.controleur = controleur
        self.modele = modele
        self.root = Tk()