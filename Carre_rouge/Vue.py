import tkinter
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
        self.current_frame = None
        # self.creer_canvas()
        # self.creer_boutons()
        self.dict_frames = {}
        self.initialiser_frames()

    def initialiser_frames(self):
        self.window = tk.Frame(self.root, bg="aquamarine2")

        self.creer_frame_boutons_principals()
        self.creer_frame_jeu()
        self.creer_frame_leaderboard()
        self.window.pack()
        self.afficher_frame("jeu")
        print(self.dict_frames)

    def creer_frame_boutons_principals(self):
        self.frame_boutons = tk.Frame(self.window, height=300, bg="aquamarine2")

        # 1. bouton leaderBoard
        self.leaderboard_btn = Button(self.frame_boutons, text="Leaderboard", font="Courier 10",
                                      command=self.afficher_leaderboard)
        self.leaderboard_btn.pack(side=tk.LEFT, padx=10, pady=(20, 20),
                                  anchor='n')  # Align buttons to the left with some padding

        # 2. bouton nouvelle partie
        self.nouvelle_partie_btn = Button(self.frame_boutons, text="Nouvelle Partie", font="Courier 10",
                                          command=self.nouvelle_partie)
        self.nouvelle_partie_btn.pack(side=tk.LEFT, padx=100, pady=(20, 20),
                                      anchor='n')  # Align buttons to the left with some padding

        # 3. bouton quitter
        self.quitter_btn = Button(self.frame_boutons, text="Quitter", font="Courier 10",
                                  command=self.activer_menu_quitter)
        self.quitter_btn.pack(side=tk.RIGHT, padx=10, pady=(20, 20),
                              anchor='n')  # Align buttons to the left with some padding
        self.frame_boutons.pack()
        new_frame = {"boutons": self.frame_boutons}
        self.dict_frames.update(new_frame)

    def creer_frame_jeu(self):
        self.frame_jeu = tk.Frame(self.window, bg="aquamarine2")
        self.aire_jeu = Canvas(self.frame_jeu, height=self.modele.hauteur, width=self.modele.hauteur,
                               bg="white", highlightbackground='black', highlightthickness=self.modele.border_width)
        self.aire_jeu.bind("<Button>", self.activer)

        self.aire_jeu.pack()
        new_frame = {"jeu": self.frame_jeu}
        self.dict_frames.update(new_frame)

    def creer_frame_leaderboard(self):
        self.frame_leaderboard = tk.Frame(self.window, bg="aquamarine2")
        self.leaderboard = Canvas(self.frame_leaderboard, height=self.modele.hauteur,
                                  width=self.modele.largeur + self.modele.border_width * 2,
                                  bg="blue")

        self.leaderboard.pack()
        new_frame = {"leaderboard": self.frame_leaderboard}
        self.dict_frames.update(new_frame)

    def creer_frame_nouvelle_session(self):
        pass

    def creer_frame_fenetre_quitter(self):
        pass

    def afficher_frame(self, frame):
        print(frame)
        if self.current_frame is not None:
            self.current_frame.pack_forget()

        self.dict_frames[frame].pack()
        self.current_frame = self.dict_frames[frame]
        pass

    def creer_canvas(self):
        pass
        # menu principal
        # self.window = tk.Frame(self.root, bg="aquamarine2")

        # self.menu_principal = Canvas(self.window, height=200, width=self.modele.largeur + (self.modele.border_width * 2),
        #                              bg="red")

        # titre = Label(self.menu_principal, text="Carré rouge", font="Courier 17 bold", fg="red4", bg="aquamarine2")
        # titre.pack()
        # credits = Label(self.menu_principal, text="Francois Bouchard\nBettina-Sarah Janesch", font="Courier 13",
        #                 bg="aquamarine2")
        # credits.pack(side=tk.RIGHT)

        # self.aire_boutons = tk.Frame(self.root, height=300, bg="aquamarine2")

        # self.aire_boutons = Canvas(self.root, height=200, width=self.modele.largeur + (self.modele.border_width * 2),
        #                             bg="aquamarine2")

        # self.frame_jeu = tk.Frame(self.root, height=self.modele.hauteur, width=self.modele.hauteur, bg="aquamarine2")

        # self.aire_jeu = Canvas(self.frame_jeu, height=self.modele.hauteur, width=self.modele.hauteur,
        #                     bg="white", highlightbackground='black', highlightthickness=self.modele.border_width)
        # self.aire_jeu.bind("<Button>", self.activer)

        # self.nom_session = Label(self.aire_jeu, height=50, width=50, bg="green")
        # self.nom_session.grid()

        # leaderboard
        # self.leaderboard = Canvas(self.window, height=self.modele.hauteur, width=self.modele.largeur+self.modele.border_width*2,
        #                           bg="blue")
        # # session
        # self.session = Canvas(self.root, height=self.modele.hauteur, width=self.modele.largeur+self.modele.border_width*2,
        #                           bg="green", highlightbackground='black', highlightthickness=self.modele.border_width)
        # # canvas quitter
        # self.quitter = Canvas(self.root, height=self.modele.hauteur, width=self.modele.hauteur,
        #                           bg="purple", highlightbackground='black', highlightthickness=self.modele.border_width)
        #
        # self.menu_principal.pack(side=tk.TOP, fill=tk.X)
        # self.aire_boutons.pack(fill=tk.X, side=tk.TOP, expand=True)
        # self.window.pack()
        # self.aire_boutons.pack(fill=tk.X)
        # self.aire_jeu.pack()
        # self.frame_jeu.pack()

    # def creer_boutons(self):
    #     # 1. bouton leaderBoard
    #     self.leaderboard_btn = Button(self.frame_boutons, text="Leaderboard", font="Courier 10",
    #                                   command=self.toggle_leaderboard)
    #     self.leaderboard_btn.pack(side=tk.LEFT, padx=10, pady=(20, 20),
    #                               anchor='n')  # Align buttons to the left with some padding
    #     # pady=(0, 30) = 30 hauteur du bouton
    #     # 2. bouton nouvelle partie
    #     self.nouvelle_partie_btn = Button(self.frame_boutons, text="Nouvelle Partie", font="Courier 10",
    #                                       command=self.nouvelle_partie)
    #     self.nouvelle_partie_btn.pack(side=tk.LEFT, padx=100, pady=(20, 20),
    #                                   anchor='n')  # Align buttons to the left with some padding
    #
    #     # 3. bouton quitter
    #     self.quitter_btn = Button(self.frame_boutons, text="Quitter", font="Courier 10",
    #                               command=self.activer_menu_quitter)
    #     self.quitter_btn.pack(side=tk.RIGHT, padx=10, pady=(20, 20),
    #                           anchor='n')  # Align buttons to the left with some padding

    def creer_carre_rouge(self):
        self.aire_jeu.create_rectangle(self.modele.carre.posX, self.modele.carre.posY,
                                       self.modele.carre.posX + self.modele.carre.taille,
                                       self.modele.carre.posY + self.modele.carre.taille,
                                       fill=self.modele.carre.couleur,
                                       tags=("carre_rouge",))

    def activer(self, evt):
        mestags = self.aire_jeu.gettags("current")
        print("jeu en cours: ", self.modele.jeu_en_cours)
        if "carre_rouge" in mestags:
            self.aire_jeu.bind("<Motion>", self.deplacer_carre)
            self.aire_jeu.bind("<ButtonRelease>", self.desactiver)

        if not self.modele.jeu_en_cours:
            self.controleur.commencer_partie()

    def desactiver(self, evt):
        self.aire_jeu.unbind("<Motion>")
        self.aire_jeu.unbind("<ButtonRelease>")

    def deplacer_carre(self, evt):
        self.controleur.changer_position((evt.x, evt.y))

    def animer(self):
        self.controleur.animer_jeu()
        print("animer-vue")

    def afficher_pions(self):
        self.aire_jeu.delete("all")
        for i in self.modele.rectangles:
            self.aire_jeu.create_rectangle(i.posX, i.posY,
                                           i.posX + i.largeur, i.posY + i.hauteur, fill=i.couleur,
                                           tags=("bloc",))  # tuple
            # print("new pos: ", i.posX, ", ", i.posY)

        self.creer_carre_rouge()

    def nouvelle_partie(self):
        self.aire_jeu.delete("all")
        self.afficher_frame("jeu")
        self.controleur.nouvelle_partie()
        self.nouvelle_partie_btn.config(state=tkinter.DISABLED)
        self.leaderboard_btn.config(state=tkinter.DISABLED)
        # self.nouvelle_partie_btn.config(state=tkinter.DISABLED)

    def terminer_partie(self):
        self.desactiver(None)
        self.nouvelle_partie_btn.config(state=tkinter.ACTIVE)
        self.leaderboard_btn.config(state=tkinter.ACTIVE)
        self.activer_fenetre_duree()
        print("fin du jeu")

    # def toggle_leaderboard(self):
    #     # toggle le canevas du leaderboard
    #     if not self.leaderboard.winfo_ismapped():
    #         self.aire_jeu.pack_forget()
    #         self.leaderboard.pack()
    #         self.leaderboard_btn["text"] = "Retour"
    #         self.afficher_leaderboard()
    #     else:
    #         self.aire_jeu.pack()
    #         self.leaderboard.pack_forget()
    #         self.leaderboard_btn["text"] = "Leaderboard"

    def afficher_leaderboard(self):
        self.leaderboard.delete("all")
        self.afficher_frame("leaderboard")
        leaderboard_tab = self.modele.get_leaderboard()
        for row in range(len(leaderboard_tab)):
            print(row)
            self.leaderboard.create_text(self.modele.largeur / 2 + self.modele.border_width,
                                         self.modele.border_width + (row * 30) + 30,
                                         text=leaderboard_tab[row],
                                         font=("Helvetica", 12,))

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
        self.aire_jeu.create_text(self.modele.largeur / 2 + self.modele.border_width,
                                  self.modele.hauteur / 2 + self.modele.border_width,
                                  text="Votre temps: " + self.modele.get_duree_partie(),
                                  font=("Helvetica", 20,))
