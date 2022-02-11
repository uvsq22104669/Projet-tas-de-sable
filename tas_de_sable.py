#####
# Groupe  LDDBI 5
# Laurédane COUSTILLAS
# Alexandre SCHOUMSKY
# Hippolyte LEFER
# Tilly SEASSAU
#https://github.com/uvsq22104669/Projet-tas-de-sable
#######

import tkinter as tk

racine = tk.Tk()
racine.title("Tas de sable")

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
canvas.grid(column=0, row=1)



#création des widgets
bouton = tk.Button(racine, text="Configuration courante", bg ="white")
bouton.grid(column=0, row=2)

racine.mainloop()
