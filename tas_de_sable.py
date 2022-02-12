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

#fonction qui initialise la configuration courante
def configurationCourante() : 
  taillecarre = 10
  for y in range(25): #creation des cases 
    for x in range(25):
        x1 = x*taillecarre 
        y1 = y*taillecarre
        x2 = x1 + taillecarre
        y2 = y1 + taillecarre
        couleur = random.randint(0,3) #determination de la couleur de chaque case
        if couleur == 0: 
          couleur = "white"
        elif couleur == 1 : 
          couleur = "black"
        elif couleur == 2 : 
          couleur = "blue"
        elif couleur == 3 : 
          couleur= "purple"
        canvas.create_rectangle((x1, y1, x2, y2), fill=couleur)
    print("Une case blanche signifie qu'il y a un aucun grain de sable, une case noire 1 grain, une case bleue 2 grains et une case violete 3 grains")
  return 

#création des widgets
bouton = tk.Button(racine, text="Configuration courante", bg ="white", command = configurationCourante)
bouton.grid(column=0, row=2)

racine.mainloop()
