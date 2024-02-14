import Vue as v
import Modele as mod

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = v.Vue(self, self.modele)
        # self.commencer_partie()
        # self.nouvelle_partie()
        self.vue.root.mainloop()

    def nouvelle_partie(self):
        # self.animer_jeu()
        self.modele.creer_pions()
        self.vue.afficher_blocs()
        pass

    def commencer_partie(self):
        print("COOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMENCER")
        self.modele.commencer_partie()
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

    def animer_jeu(self):
        self.modele.deplacer_rectangles()
        self.vue.afficher_blocs()
        #if self.modele.verifier_collisions():
        self.vue.root.after(50, self.animer_jeu)
        #else:
        #timer stop
        #game over ...

    def changer_position(self, new_position):
        self.modele.changer_position(new_position)

if __name__ == "__main__":
    c = Controleur()