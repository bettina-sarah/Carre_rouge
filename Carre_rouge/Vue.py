import tkinter
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
        self.menu_principal = Canvas(self.root, height=100, width=self.modele.largeur + (self.modele.border_width * 2),
                                     bg="pink", )



        # aire de jeu
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
        self.nouvelle_partie_btn = Button(self.menu_principal, text="Nouvelle Partie", command=self.nouvelle_partie)
        self.nouvelle_partie_btn.pack()

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
            self.nouvelle_partie_btn.config(state=tkinter.DISABLED)

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
