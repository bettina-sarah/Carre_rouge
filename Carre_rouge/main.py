import Vue as vue
import Modele as mod

class Controleur():
    def __init__(self):
        self.modele = mod.Modele(self)
        self.vue = vue.Vue(self, self.modele)
        self.vue.root.mainloop()
        self.commencer_partie()


    def commencer_partie(self):
        #pions & carré position initiale, reset infos
        pass

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
        self.modele.deplacer_pions()
        # self.vue.afficher_pions()
        self.vue.root.after(50, self.animer_jeu)  # recurser overflow si on met ()
        pass

if __name__ == "__main__":
    c = Controleur()