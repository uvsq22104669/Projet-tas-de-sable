# Groupe  LDDBI 5
# Laurédane COUSTILLAS
# Alexandre SCHOUMSKY
# Hippolyte LEFER
# Tilly SEASSAU
#https://github.com/uvsq22104669/Projet-tas-de-sable
#######

# Import des librairies
import tkinter as tk
import random
import numpy as np

racine = tk.Tk()
racine.title("Tas de sable")

# Définition des constantes
CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
NB_CASES_GRILLE = 50

canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
canvas.grid(column=0, row=1)

# creation de la matrice qui va servir pour la configuration courante (on peut l'inserer dans la fonction si besoin)

dimension = 50
matrice = []
for j in range(dimension) : 
  listej = []
  for i in range(dimension) : 
    listej.append(random.randint(0,3))
  matrice.append(listej)
  print(np.array(matrice))

#fonction qui initialise la configuration courante
def configurationCourante() : 
  """Fonction qui associe chaque case à un nombre de grains de sable aléatoire entre 0 et 3 inclus ainsi qu'une couleur selon le 
  nombre de grains de sable"""
  global configurationCourante
  taillecarre = 10
  for y in range(dimension): #creation des cases 
    for x in range(dimension):
        x1 = x*taillecarre 
        y1 = y*taillecarre
        x2 = x1 + taillecarre
        y2 = y1 + taillecarre

        couleur = matrice[y][x] #détermination de la couleur de chaque case
        if couleur == 0: 
          couleur = "white"
        elif couleur == 1 : 
          couleur = "black"
        elif couleur == 2 : 
          couleur = "blue"
        elif couleur == 3 : 
          couleur= "purple"
        canvas.create_rectangle((x1, y1, x2, y2), fill=couleur)
  return 

#création des widgets
bouton = tk.Button(racine, text="Configuration courante", bg ="white", command = configurationCourante)
bouton.grid(column=0, row=2)

racine.mainloop()   
