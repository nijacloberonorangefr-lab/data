import csv
from math import floor
import tkinter as tk

pays = []

with open('C:/Users/sknx/OneDrive/Bureau/data meama/data/output (1).nmea', newline='') as csvfile: #veuillier changer cette ligne c'est mon à moi donc sa ne marchera pas merci de votre compresion eplexemple c:/Users/jalras/...
    pays_csv = csv.reader(csvfile, delimiter=';')
    for row in pays_csv:
        pays.append(row)


def calculer():
    # Maintenant, entree_utilisateur existe, on peut faire .get()
    num = int(entree_utilisateur.get())
    trames = pays[num][0]
    trame=trames
    
    # On fait tes calculs (latitude/longitude)
    res_lat = latitude(trame)
    
    # On affiche le résultat dans l'interface
    label_affichage.config(text=f"Trame lue : {trame[:20]}... \n Latitude : {res_lat}")

# 3. Création de l'interface graphique
root = tk.Tk()
root.title("Lecteur de Trame NMEA")

tk.Label(root, text="Entrez le numéro de ligne :").pack()

# C'est ici qu'on définit enfin 'entree_utilisateur' !
entree_utilisateur = tk.Entry(root) 
entree_utilisateur.pack()

tk.Button(root, text="Extraire la latitude", command=calculer).pack()

label_affichage = tk.Label(root, text="Résultat ici")
label_affichage.pack()

# Garder tes fonctions latitude/longitude en dessous ou au dessus
def latitude(trame):
    liste_information = trame.split(",")
    # ... la suite de ton code actuel ...
    return resultat

root.mainloop() # Très important pour que la fenêtre reste ouverte
print(trames)
    

"""fonction qui renvoie la latitude du lieu en degré décimal
(sans prise en compte du signe)
à partir de la trame NMEA 0183 entrée comme paramètre"""

#découpage de la trame suivant les virgules
liste_information=trame.split(",")  # liste des éléments composants la trame


#Extraction de la latitude à partir du troisème élément de la liste ;
# il se nomme liste_information[2] car la numérotation commence à 0.

minute = floor(float(liste_information[2])) % 100
degre = int(floor(float(liste_information[2]) - minute) / 100)
seconde = (float(liste_information[2])-floor(float(liste_information[2])))*60

decimales_degre = (float(liste_information[2]) - degre*100)/60
resultat = degre+decimales_degre
    

return resultat



def longitude(trame):
    
    """fonction qui renvoie la latitude du lieu en degré décimal
(sans prise en compte du signe)
à partir de la trame NMEA 0183 entrée comme paramètre"""

#découpage de la trame suivant les virgules
liste_information=trame.split(",")  # liste des éléments composants la trame


#Extraction de la latitude à partir du troisème élément de la liste ;
# il se nomme liste_information[2] car la numérotation commence à 0.

        minute = floor(float(liste_information[4])) % 100
        degre = int(floor(float(liste_information[4]) - minute) / 100)
        seconde = (float(liste_information[4])-floor(float(liste_information[4])))*60

        decimales_degre = (float(liste_information[4]) - degre*100)/60
        resultat = degre+decimales_degre
    

            return resultat

trame =trames
print(latitude(trame),longitude(trame))


# l'entrée trame sera une trame MNEA 0183, par exemple :
# trame = "$GPGGA,194701.45,2612.3990,S,2802.6016,E,1,06,2.35,1,M,,,,0000*0E"
# contenu de la trame entre guillemets en tant que chaînes de caractères.
def signe_latitude(trame):
    """fonction qui renvoie la latitude du lieu avec son signe en degré décimal
    (positive si dans l'hémisphère Nord, négative sinon)
    à partir de la trame NMEA 0183 entrée comme paramètre"""

    liste_information=trame.split(",")  # liste des éléments composants la trame

    if liste_information[3]=='N':
        return(latitude(trame))
    else:
        return(-latitude(trame))

def signe_longitude(trame):
    """fonction qui renvoie la latitude du lieu avec son signe en degré décimal
    (positive si dans l'hémisphère Nord, négative sinon)
    à partir de la trame NMEA 0183 entrée comme paramètre"""

    liste_information=trame.split(",")  # liste des éléments composants la trame

    if liste_information[5]=='O':
        return(longitude(trame))
    else:
        return(-longitude(trame))

    trame =trames
    print(signe_latitude(trame))
    print(signe_longitude(trame))
