import tkinter as tk
from tkinter import *
from Modele import *
# from Controleur import *
from CarreRouge import *
from RectangleBleu import *

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
        self.creer_canvas()
        self.creer_boutons()

    def creer_canvas(self):

        # menu principal
        self.menu_principal = Canvas(self.root, height=200, width=self.modele.largeur + (self.modele.border_width * 2),
                                     bg="aquamarine2")

        titre = Label(self.menu_principal, text="Carré rouge", font="Courier 17 bold", fg="red4", bg="aquamarine2")
        titre.pack()
        credits = Label(self.menu_principal, text="Francois Bouchard\nBettina-Sarah Janesch", font="Courier 13",
                        bg="aquamarine2")
        credits.pack(side=tk.RIGHT)

        self.aire_boutons = tk.Frame(self.root, height=300, bg="aquamarine2")

        # self.aire_boutons = Canvas(self.root, height=200, width=self.modele.largeur + (self.modele.border_width * 2),
        #                             bg="aquamarine2")

        self.aire_jeu = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
                             bg="white", highlightbackground='black', highlightthickness=self.modele.border_width)
        self.aire_jeu.bind("<Button>", self.activer)

        # self.nom_session = Label(self.aire_jeu, height=50, width=50, bg="green")
        # self.nom_session.grid()

        # leaderboard
        self.leaderboard = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
                                  bg="blue", highlightbackground='black', highlightthickness=self.modele.border_width)
        # session
        self.session = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
                                  bg="green", highlightbackground='black', highlightthickness=self.modele.border_width)
        # canvas quitter
        self.quitter = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
                                  bg="purple", highlightbackground='black', highlightthickness=self.modele.border_width)

        self.menu_principal.pack(side=tk.TOP, fill=tk.X)
        #self.aire_boutons.pack(fill=tk.X, side=tk.TOP, expand=True)
        self.aire_boutons.pack(fill=tk.X)
        self.aire_jeu.pack()

    def creer_boutons(self):
        # 1. bouton leaderBoard
        self.leaderboard_btn = Button(self.aire_boutons, text="Leaderboard", font="Courier 10", command=self.toggle_leaderboard)
        self.leaderboard_btn.pack(side=tk.LEFT, padx=10, pady=(20, 20), anchor='n')  # Align buttons to the left with some padding
        #pady=(0, 30) = 30 hauteur du bouton
        # 2. bouton nouvelle partie
        self.nouvelle_partie_btn = Button(self.aire_boutons, text="Nouvelle Partie", font="Courier 10", command=self.nouvelle_partie)
        self.nouvelle_partie_btn.pack(side=tk.LEFT, padx=100, pady=(20, 20), anchor='n')  # Align buttons to the left with some padding

        # 3. bouton quitter
        self.quitter_btn = Button(self.aire_boutons, text="Quitter", font="Courier 10", command=self.activer_menu_quitter)
        self.quitter_btn.pack(side=tk.RIGHT, padx=10, pady=(20, 20), anchor='n')  # Align buttons to the left with some padding


    def creer_carre_rouge(self):
        self.aire_jeu.create_rectangle(self.modele.carre.posX, self.modele.carre.posY, self.modele.carre.posX+self.modele.carre.taille,
                                       self.modele.carre.posY+self.modele.carre.taille, fill=self.modele.carre.couleur,
                                       tags=("carre_rouge",))

    def activer(self, evt):
        mestags = self.aire_jeu.gettags("current")
        if "carre_rouge" in mestags:
            self.aire_jeu.bind("<Motion>", self.bouger_carre_rouge)
            self.aire_jeu.bind("<ButtonRelease>", self.desactiver)

        if not self.modele.jeu_en_cours:
            self.controleur.commencer_partie()
            self.nouvelle_partie_btn.config(state=tk.DISABLED)

    def desactiver(self, evt):
        self.aire_jeu.unbind("<Motion>")
        self.aire_jeu.unbind("<ButtonRelease>")

    def bouger_carre_rouge(self, evt):
        self.controleur.changer_position((evt.x, evt.y))

    def animer(self):
        self.controleur.animer_jeu()
        print("animer-vue")

    def afficher_blocs(self):
        self.aire_jeu.delete("all")
        for i in self.modele.rectangles:
            self.aire_jeu.create_rectangle(i.posX, i.posY,
                                         i.posX + i.largeur, i.posY + i.hauteur, fill=i.couleur,
                                         tags=("bloc",)) #tuple
            print("new pos: ", i.posX, ", ", i.posY)

        self.creer_carre_rouge()


    def nouvelle_partie(self):
        self.aire_jeu.delete("all")
        self.controleur.nouvelle_partie()

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
