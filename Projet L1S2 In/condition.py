# Créé par ys000, le 20/02/2023 en Python 3.7

from casesup import *
from Fuz import *
from Mouvement import *
from time import *
from init import *
from gameset import *
from pynput import *
from pynput.keyboard import Key
from victory import *
from possible import *
from fenetre import dele
from fenetre import tablo

#Bon du coups c'est pas des conditions, c'est le jeu
#Sans intérface graphique, tout apparaît dans la console

def start():
    global table                #La table est global pour être facile d'accès et non-modifié entre les programmes
    table = ini()               #Cf programme Init
    """table = [[2, 4, 8, 16]      #Ca c'est juste moi qui triche pour faire des test, faut mettre en comm après
    ,[32, 4, 2, 4]
    ,[64, 2, 8, 4]
    ,[8, 8, 32, 4]]
    print("")                   #C'truc c'est pour afficher la game tant que y a pas d'intérface, idem dans tout les programmes
    print(table[0])             
    print(table[1])
    print(table[2])
    print(table[3])
    print("")"""
    tablo()
    def inp(key):                       #La fonction appear quand le clavier est utilisé, je sais pas si on peut limiter le truc à 4 bouton par contre
        global table
        a = False
        win = False
        i = 0
        #while win == False and i < 15:
        poss = possibility(table)                   #Tout les moves autorisé pour que le programme te laisse pas faire n'importe quoi

        if  key == Key.right and 'R' in poss:        #Pour chaque flèche directionnel, on a un if différent pour matcher les moves
            table = game(table,'R')                  #Y a que R, L, U et D
            a = True
            dele()
            tablo()
        elif key == Key.left and 'L' in poss:
            table = game(table,'L')
            a = True
            dele()
            tablo()
        elif key == Key.up and 'U' in poss:
            table = game(table,'U')
            a = True
            dele()
            tablo()
        elif key == Key.down and 'D' in poss:
            table = game(table,'D')
            a = True
            dele()
            tablo()
            #Fonction win qui arrête tout en cas de victoire sinon break, y a rien pour l'instant

        if a:
            table = casebonus(table)
            print("")
            print(table[0])
            print(table[1])
            print(table[2])
            print(table[3])
            print("")
            winlose(table)
            a = False



            #return table

    with keyboard.Listener(on_release=inp) as listener:     #Merci Google, c'est ça qui surveille le clavier
        listener.join()
#start() #On lance la game, c'est ici qu'on peut jouer réellement



