import datetime

import Vue as v
import Modele as mod


class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = v.Vue(self, self.modele)
        self.vue.root.mainloop()
        self.temps_fin = None

    def nouvelle_partie(self):
        self.modele.nouvelle_partie()
        self.vue.afficher_pions()


    def commencer_partie(self):
        self.modele.commencer_partie()
        self.animer_jeu()

    def terminer_partie(self):
        self.modele.terminer_partie()
        self.vue.terminer_partie()
    #  self.vue.afficher_fenetre_duree()

    def creer_session(self):
        # self.nom_session?
        # self.difficulte ? menu choix
        pass

    def creer_partie(self):
        self.modele.reset_position()

    def animer_jeu(self):
        self.modele.deplacer_rectangles()
        self.vue.afficher_pions()
        if not self.modele.verifier_collisions():
            self.vue.root.after(50, self.animer_jeu)
        else:
            self.terminer_partie()

    def changer_position(self, new_position):
        self.modele.changer_position(new_position)

    def submit_session(self, diff, nom):
        self.modele.submit_session(diff, nom)


if __name__ == "__main__":
    c = Controleur()
