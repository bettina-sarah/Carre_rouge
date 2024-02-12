from tkinter import *
from Modele import *
# from Controleur import *
from CarreRouge import *
from Pion import *


class Vue():
    def __init__(self, controleur, modele):
        self.controleur = controleur
        self.modele = modele
        self.root = Tk()
        self.canvas = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur, borderwidth=50,
                             bg="black")
        self.canvas.pack()
        self.isActive = False
        # 50 epaisseur
        # frame = Frame(self.root, height=self.modele.hauteur, width=self.modele.hauteur, bg="seashell2")
        # frame.pack()
        # frame1 = Frame(frame, height=200, width=200, bg="red")
        # frame1.pack()

    def active_menu_demarrage(self):
        if self.isActive:
            # affiche la fenetre démarrage
            # self.frame = ... ??
            # active la saisie du nom de session, boutons de difficulté
            pass
        pass

    def activer_leaderboard(self):
        # + bouton effacer, retour
        if self.isActive:
            pass
        pass

    def afficher_fenetre_principale(self):

        # affiche l'aire de jeu'
        # active le boutons 'nouvelle partie', bleaderboard, quitter
        # bind le clic sur le carré au rouge à la commande pour commencer la partie
        pass

    def activer_menu_quitter(self):
        if self.isActive:
            # affiche fenetre quitter, active bouton quitter, changement session, annuler
            pass
        pass

    def activer_fenetre_duree(self):
        if self.isActive:
            # affiche fenetre avec duree de partie (terminé)
            pass
        pass

    def activer_bouton_fenetre_principale(self):
        if self.isActive:
            pass
        pass
