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

        self.menu_principal = None
        self.aire_jeu = None
        self.leaderboard = None
        self.quitter = None
        self.session = None

        self.nouvelle_partie_btn = None
        self.leaderboard_btn = None
        self.quitter_btn = None

        self.activeCanvas = None

        # self.isActive = False
        self.creer_canvas()
        self.creer_boutons()

    def creer_canvas(self):

        # menu principal
        self.menu_principal = Canvas(self.root, height=100, width=self.modele.largeur + (self.modele.border_width * 2),
                                     bg="pink", )
        # aire de jeu
        self.aire_jeu = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
                             bg="white", highlightbackground='black', highlightthickness=self.modele.border_width)

        # leaderboard
        self.leaderboard = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
                                  bg="blue", highlightbackground='black', highlightthickness=self.modele.border_width)
        # session
        self.session = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
                                  bg="green", highlightbackground='black', highlightthickness=self.modele.border_width)
        # canvas quitter
        self.quitter = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
                                  bg="purple", highlightbackground='black', highlightthickness=self.modele.border_width)

        self.menu_principal.pack()
        self.aire_jeu.pack()


    def creer_boutons(self):
        # bouton leaderBoard
        self.leaderboard_btn = Button(self.menu_principal, text="Leaderboard", command=self.toggle_leaderboard)
        self.leaderboard_btn.pack()
        # bouton quitter
        self.quitter_btn = Button(self.menu_principal, text="Quitter", command=self.activer_menu_quitter)
        self.quitter_btn.pack()
        # bouton nouvelle partie
        self.nouvelle_partie_btn = Button(self.menu_principal, text="Nouvelle Partie", command=self.controleur.commencer_partie)
        self.nouvelle_partie_btn.pack()

    def active_menu_demarrage(self):
        if self.isActive:
            # affiche la fenetre démarrage
            # self.frame = ... ??
            # active la saisie du nom de session, boutons de difficulté
            pass
        pass

    def toggle_leaderboard(self):
        # toggle le canevas du leaderboard
        if not self.leaderboard.winfo_ismapped():
            self.aire_jeu.pack_forget()
            self.leaderboard.pack()
            self.leaderboard_btn["text"] = "Retour"
        else:
            self.aire_jeu.pack()
            self.leaderboard.pack_forget()
            self.leaderboard_btn["text"] = "Leaderboard"

    # def toggle_session(self):
    #     # toggle le canevas du leaderboard
    #     if not self.leaderboard.winfo_ismapped():
    #         self.activeCanvas.pack_forget()
    #         self.leaderboard.pack()
    #         self.leaderboard_btn["text"] = "Retour"
    #     else:
    #         self.aire_jeu.pack()
    #         self.leaderboard.pack_forget()
    #         self.leaderboard_btn["text"] = "Leaderboard"





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
