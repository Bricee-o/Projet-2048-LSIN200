import tkinter as tk
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

fenetre = tk.Tk() #On créer notre fenêtre Tkinter
fenetre.title("2048") #On donne un titre à la fenêtre

label1 = tk.Label(fenetre, text="2048", font = ("helvetica", "30"),fg="#ede0c8") #Création d'un widget texte
label1.grid(column=2, row=0) #Positionement du widget dans la fenêtre

HEIGHT = 500                #Création d'une varaible "HEIGHT" qui va nous permettre de definir les dimensions du canvas que l'on va créer 
WIDTH = 500                 #Création d'une variable "WIDTH" qui va nous permettre de faire la meme chose que la variable HEIGHT
largeur_case = WIDTH // 4   #Création de la variable "largeur case" qui va nous permettre de defnir la taille des cases dans la grille de notre 2048
hauteur_case = HEIGHT // 4  #Création de la variable "hauteur case" même fonction que "largeur case"


canvas = tk.Canvas(fenetre, bg="gray", height=HEIGHT, width=WIDTH) #Création d'un Canevas carré gris, on utiluse HEIGHT et WIDTH pour le dimensionner
canvas.create_text(250,250,text="Cliquer sur Nouvelle partie pour commencer") #On ajoute du texte dans notre carré qui fait office d'interface de départ
canvas.grid(column=0,columnspan=5, row=1, rowspan=5) #On positionne le canvas dans notre fenêtre

#-------------------------------------------------------------------------------
#Fonctions

def tablo():
    global tabe
    global table
    tabe = []
    meh = []
    #table = [[2, 4, 8, 16]
    #,[32, 4, 2, 4]
    #,[64, 2, 8, 4]
    #,[8, 8, 32, 4]]
    print(table)
    print(tabe)
    for i in range(4):
        for j in range(4):

            color = "gray80"
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),((i+1)*largeur_case, (j+1)*hauteur_case), fill=color) 
            t = canvas.create_text(i*largeur_case+62, j*hauteur_case+62, text=table[i][j], font=("helvetica", "30"), tag=(str(i),str(j)))
            tabe.append(t)
    canvas.update()
    
    
def dele():
    global tabe
    for i in range(len(tabe)):
        canvas.delete(tabe[i])
        #canvas.update()
 
def sauvegarder():
    t=[]
    t=table.copy()
    f =open('fichier_a.txt', 'wb')
    pickle.dump(t, f)
    return t

def charger():
    f=open('fichier_a.txt', 'rb')
    charge = pickle.load(f)
    table=[]
    for i in range(len(charge)):
        h=[]
        table.append(h)
        for row in charge[i]:
            h.append(row)
        return table


def start():
    global table                #La table est global pour être facile d'accès et non-modifié entre les programmes
    table = ini()
    score()               #Cf programme Init
    """
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

        #if  key == Key.right and 'R' in poss:        #Pour chaque flèche directionnel, on a un if différent pour matcher les moves
        if  key == 'R' and 'R' in poss:    
            table = game(table,'R')                  #Y a que R, L, U et D
            a = True
        #elif key == Key.left and 'L' in poss:
        elif key == 'L' and 'L' in poss:    
            table = game(table,'L')
            a = True
        #elif key == Key.up and 'U' in poss:
        elif key == 'U' and 'U' in poss:    
            table = game(table,'U')
            a = True
        #elif key == Key.down and 'D' in poss:
        elif key == 'D' and 'D' in poss:    
            table = game(table,'D')
            a = True
            #Fonction win qui arrête tout en cas de victoire sinon break, y a rien pour l'instant

        if a:
            dele()
            print(0)
            tablo()
            print(1)
            table = casebonus(table)
            tablo()
            score()
            """
            print("")
            print(table[0])
            print(table[1])
            print(table[2])
            print(table[3])
            print("")
            """
            winlose(table)
            a = False
    """
    time.sleep(3.0)
    inp('U')
    time.sleep(3.0)
    inp('D')
    time.sleep(3.0)
    inp('R')
    time.sleep(3.0)
    inp('L')
    time.sleep(3.0)
    inp('D')
    time.sleep(3.0)
    inp('R')
    """
    def droite():
        inp('R')
    def gauche():
        inp('L')
    def bas():
        inp('D')
    def haut():
        inp('U')


    bouton8 = tk.Button(fenetre, text="Gauche", font=("helvetica", "10"),command=haut)
    bouton8.grid(column=0, row=7)

    bouton7 = tk.Button(fenetre, text="Droite", font=("helvetica", "10"),command=bas)
    bouton7.grid(column=2, row=7)

    bouton6 = tk.Button(fenetre, text="Haut", font=("helvetica", "10"),command=gauche)
    bouton6.grid(column=1, row=6)

    bouton5 = tk.Button(fenetre, text="Bas", font=("helvetica", "10"),command=droite)
    bouton5.grid(column=1, row=8)
    


    #with keyboard.Listener(on_release=inp) as listener:     #Merci Google, c'est ça qui surveille le clavier
    #    listener.join()
#start() #On lance la game, c'est ici qu'on peut jouer réellement

label2 = tk.Label(fenetre, text="Score: 0",fg="#f65e3b" ,font = ("helvetica", "20")) 
label2.grid(column=6, row=0)

def conter(liste):
    somme=0
    for k in range(len(liste)):
        somme+=sum(liste[k])
    return somme

def score():
    global table
    label2.config(text= "Score:" + str(conter(table)))
    canvas.update()



def exit():
    global table
    bouton8 = tk.Button(fenetre, text="Gauche", font=("helvetica", "10"),command=None)
    bouton8.grid(column=0, row=7)

    bouton7 = tk.Button(fenetre, text="Droite", font=("helvetica", "10"),command=None)
    bouton7.grid(column=2, row=7)

    bouton6 = tk.Button(fenetre, text="Haut", font=("helvetica", "10"),command=None)
    bouton6.grid(column=1, row=6)

    bouton5 = tk.Button(fenetre, text="Bas", font=("helvetica", "10"),command=None)
    bouton5.grid(column=1, row=8)
    
    #Fenetre de fin de partie

    fenetre2 = tk.Tk()
    fenetre2.title("FIN")
    label01 = tk.Label(fenetre2, text="Fin de partie", font = ("helvetica", "20"),bg="#eee4da")
    label01.grid(column=0, row=0,rowspan=5)
    label02 = tk.Label(fenetre2, text="Score:" + str(conter(table)), font = ("helvetica", "20"),bg="#eee4da")
    label02.grid(column=1, row=1)
    fenetre2.mainloop()






#-------------------------------------------------------------------------------
#Bouton

#m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

bouton1 = tk.Button(fenetre, text="Nouvelle Partie", font=("helvetica", "10"),command=start)
bouton1.grid(column=6, row=1)

bouton2 = tk.Button(fenetre, text="Exit", font=("helvetica", "10"),command=exit)
bouton2.grid(column=6, row=2)

bouton3 = tk.Button(fenetre, text="Save", font=("helvetica", "10"))
bouton3.grid(column=6, row=3)

bouton4 = tk.Button(fenetre, text="Load", font=("helvetica", "10"))
bouton4.grid(column=6, row=4)


fenetre.mainloop()
