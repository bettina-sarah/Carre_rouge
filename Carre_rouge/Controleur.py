from Modele import Modele as modele
from Vue import *

class Controleur():
    def __init__(self):
        self.vue = Vue(self)
        self.modele = modele(self)
        self.vue.root.mainloop()

