import Vue as v
import Modele as mod

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = v.Vue(self, self.modele)
        self.commencer_partie()
        self.vue.root.mainloop()


    def commencer_partie(self):
        self.animer_jeu()

    def terminer_partie(self):
        pass

    def creer_session(self):
        # self.nom_session?
        # self.difficulte ? menu choix
        pass

    def creer_partie(self):
        # temps debut
        self.modele.reset_position()
        pass

    def animer_jeu(self):
        self.vue.afficher_blocs()
        self.vue.root.after(50, self.animer_jeu)

    def changer_position(self, new_position):
        self.modele.changer_position(new_position)

if __name__ == "__main__":
    c = Controleur()