from tkinter import *
from Modele import *
from Controleur import *

class Vue():
    def __init__(self, parentcontroleur):
        self.parent = parentcontroleur
        self.root = Tk()