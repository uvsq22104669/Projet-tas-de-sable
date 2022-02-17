#####
# Groupe  LDDBI 5
# Laurédane COUSTILLAS
# Alexandre SCHOUMSKY
# Hippolyte LEFER
# Tilly SEASSAU
#https://github.com/uvsq22104669/Projet-tas-de-sable
#######

import tkinter as tk
import random

racine = tk.Tk()
racine.title("Tas de sable")

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
canvas.grid(column=0, row=1)
# creation de la matrice qui va servir pour la configuration courante (on peut l'inserer dans la fonction si besoin)
dimension = 5
matrice = []
for j in range(dimension) : 
  listej = []
  for i in range(dimension) : 
    listej.append(random.randint(0,3))
  matrice.append(listej)
print(np.array(matrice))

#fonction qui initialise la configuration courante
def configurationCourante() : 
  taillecarre = 10
  for y in range(dimension): #creation des cases 
    for x in range(dimension):
        x1 = x*taillecarre 
        y1 = y*taillecarre
        x2 = x1 + taillecarre
        y2 = y1 + taillecarre
        couleur = matrice[y][x] #determination de la couleur de chaque case
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
