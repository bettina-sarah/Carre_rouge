from CarreRouge import *
from RectangleBleu import *
from datetime import datetime, timedelta
import csv


class Modele:
    def __init__(self, controleur):
        self.controleur = controleur
        self.border_width = 50
        self.hauteur = 450
        self.largeur = 450
        self.rectangles = []
        self.carre = None
        self.jeu_en_cours = False
        self.temps_debut = None
        self.joueur = "Frank"
        self.difficulte = "facile"
        self.leaderboard = []
        self.csv_file_path = "scores.csv"

    def commencer_partie(self):
        self.jeu_en_cours = True
        self.temps_debut = datetime.now()
        # self.temps_debut.strftime("%M:%S.%f")[:-3]

    def nouvelle_partie(self):
        self.jeu_en_cours = False
        self.creer_pions()

    def creer_pions(self):
        self.carre = CarreRouge(self)
        self.rectangles.append(RectangleBleu(self, 60, 60, 100, 100, 4, 4, "red"))
        self.rectangles.append(RectangleBleu(self, 60, 50, 300, 85, -4, 4, "green"))
        self.rectangles.append(RectangleBleu(self, 100, 20, 355, 340, -4, -4, "yellow"))
        self.rectangles.append(RectangleBleu(self, 30, 60, 85, 350, 4, -4))

    def deplacer_rectangles(self):
        # dans les pions a place?
        for rectangle in self.rectangles:
            rectangle.deplacer()

    def changer_position(self, new_position):
        self.carre.deplacer(new_position)

    def verifier_collisions(self):
        return self.collision_bordure() or self.collision_rectangle()

    def collision_bordure(self):
        if self.carre.posX < self.border_width or self.carre.posX + self.carre.taille > self.largeur + self.border_width:
            return True

        if self.carre.posY < self.border_width or self.carre.posY + self.carre.taille > self.hauteur + self.border_width:
            return True
        return False

    def collision_rectangle(self):
        carre_x1 = self.carre.posX
        carre_x2 = self.carre.posX + self.carre.taille
        carre_y1 = self.carre.posY
        carre_y2 = self.carre.posY + self.carre.taille
        compteur_collision = 0

        for rectangle in self.rectangles:
            rect_x3 = rectangle.posX
            rect_x4 = rectangle.posX + rectangle.largeur
            rect_y3 = rectangle.posY
            rect_y4 = rectangle.posY + rectangle.hauteur
            if carre_x2 < rect_x3 or rect_x4 < carre_x1 or carre_y2 < rect_y3 or rect_y4 < carre_y1:
                compteur_collision += 1

        if compteur_collision == 4:
            return False
        return True

    def terminer_partie(self):
        #self.jeu_en_cours = False
        self.temps_fin = datetime.now()
        temps_ecoule = self.temps_fin - self.temps_debut
        self.update_fichier(temps_ecoule)
        # retire les rectangles de la liste
        self.rectangles.clear();

    def update_fichier(self, temps_ecoule):

        new_row = [self.joueur, temps_ecoule.total_seconds(), datetime.now().date(), self.difficulte]
        # string = self.joueur + "," + str(temps_ecoule.total_seconds())+","+str(datetime.now().date()) + "," + self.difficulte
        # print(string)

        with open(self.csv_file_path, mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write the new row
            csv_writer.writerow(new_row)

    def obtenir_leaderboard(self):
        # with open(self.csv_file_path, mode='r') as csv_file:
        #     csv_reader = csv.DictReader(csv_file)
        #
        #     for row in csv_reader:
        #         #if row[0] == self.joueur:
        #         self.leaderboard.append({
        #             'Nom': row[0],
        #             'Score': (row[1]),
        #             'Date': (row[2]),
        #             'Difficulté': row[3]
        #         })
        # # Sort the leaderboard_data list based on the 'Score' in descending order
        # self.leaderboard.sort(key=lambda x: x['Score'], reverse=True)
        pass