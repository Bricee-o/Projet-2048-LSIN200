import tkinter as tk
from random import *
import json

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
#Fonction


def ini():      #On initialise le tableau de base, composé de 0 puis de 2 cases au hasard.
    global table    #Le tableau est une variable global pour ne pas l'envoyer et le recevoir a chaque fois
    table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    casebonus()         #Casebonus rajoute 2 ou 4 dans une case vide, donc on l'utilise 2 fois
    casebonus()         # en début de partie, pour avoir 2 cases pré-rempli


def possibility(table):
    poss = []           #La fonction suivante détérmine toute les possibilités envisageable et renvoie une liste de toute les possibilités
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] != 0:
                if j == 0:
                    if table[i][j+1] == 0 or table[i][j+1] == table[i][j]:  #Pour chaque mouvement possible, ça va vérifier si la case à coté
                        if 'D' not in poss:                                 #est soi vide, soi identique
                            poss.append('D')                                #Ensuite sa vérifie si le mouvement n'est pas déjà présent dans la liste
                elif j == len(table)-1:                                     #Sinon ça rajoute le mouvement
                    if table[i][j-1] == 0 or table[i][j-1] == table[i][j]:  #Note: Y a 3 if a chaque fois au cas où l'un des voisins est hors-tableau
                        if 'U' not in poss:
                            poss.append('U')
                else:
                    if table[i][j+1] == table[i][j] or table[i][j+1] == 0:
                        if 'D' not in poss:
                            poss.append('D')
                    if table[i][j-1] == 0 or table[i][j-1] == table[i][j]:
                        if 'U' not in poss:
                            poss.append('U')
                if i == 0:
                    if table[i+1][j] == 0 or table[i+1][j] == table[i][j]:
                        if 'R' not in poss:
                            poss.append('R')
                elif i == len(table)-1:
                    if table[i-1][j] == 0 or table[i-1][j] == table[i][j]:
                        if 'L' not in poss:
                            poss.append('L')
                else:
                    if table[i-1][j] == 0 or table[i-1][j] == table[i][j]:
                        if 'L' not in poss:
                            poss.append('L')
                    if table[i+1][j] == table[i][j] or table[i+1][j]==0:
                        if 'R' not in poss:
                            poss.append('R')
    return poss     


def mouvement(move):
    global table
    if move == 'D':
        for i in range(len(table)):
                for j in range(len(table[0])-1,-1,-1):
                    if table[i][j] != 0:                 #Quasiment la même chose que Fuz
                        k = 1                           #Si la case est 0, on déplace la case avant jusqu'à ce que se soit pas 0
                        while j+k < len(table) and table[i][j+k]== 0:
                            case_vide = 0                       #Tant que k et j n'indique pas à l'exterieur du tableau
                            case_deplace = table[i][j+k-1]         # et que la case suivantz est vide
                            table[i][j+k] = case_deplace           #Tout ça c'est la base du déplacement dans une Matrice
                            table[i][j+k-1] = case_vide
                            k += 1


    elif move == 'U':                       #Même chose 4 fois pour les 4 directions possibles
        for i in range(len(table)):         #Pas de return car le tableau est global
                for j in range(1,len(table[0])):
                    if table[i][j] != 0:
                        k = 1

                        while j-k > -1 and table[i][j-k]== 0:

                            case_vide = 0
                            case_deplace = table[i][j-k+1]
                            table[i][j-k] = case_deplace
                            table[i][j-k+1] = case_vide
                            k += 1

    elif move == 'R':
        for j in range(len(table[0])):
                for i in range(len(table)-2,-1,-1):
                    if table[i][j] != 0:
                        k = 1
                        while i+k < len(table) and table[i+k][j]== 0:
                            case_vide = 0
                            case_deplace = table[i+k-1][j]
                            table[i+k][j] = case_deplace
                            table[i+k-1][j] = case_vide
                            k += 1

    elif move == 'L':
        for j in range(len(table[0])):
                for i in range(len(table)):
                    if table[i][j] != 0:
                        k = 1
                        while i-k > -1 and table[i-k][j]== 0:
                            case_vide = 0
                            case_deplace = table[i-k+1][j]
                            table[i-k][j] = case_deplace
                            table[i-k+1][j] = case_vide
                            k += 1


def casebonus():                            
    global table
    vide = []                               
    for i in range(len(table)):             
        for j in range(len(table)):         #Là, ça va vérifier s'il y a des cases vides
            if table[i][j] == 0:            #Puis si c'est le cas, tiré un chiffre au hasard pour déterminer si c'est 4 ou 2
                vide.append([i,j])          #Puis le placé dans une case au pif

    if vide:                                    #Si la liste renvoie True, c'est que la liste n'est pas vide, donc au moins 1 case est vide
        case_choisi = randint(0,len(vide)-1)              #Sinon on touche a rien
        hasard = randint(1,10)                       #Le b c'est pour gerer la chance d'obtenir 2 ou 4
        if hasard <= 9:
            table[vide[case_choisi][0]][vide[case_choisi][1]] = 2
        else:
            table[vide[case_choisi][0]][vide[case_choisi][1]] = 4


def fusion(move):                             #Ici, les cases fusionnent avec leur voisin selon le mouvement indiqué.
    global table                                    #Attention, le programme ne détecte pas sur quel coté la case fusionné doit se placer, tout est déplacé plus tard.
                                                    
    if move == 'D':                                 #C'est pour éviter les bug
        for i in range(len(table)):                 #Déjà y a 1 function pour chaque mouvement
            for j in range(len(table)-1,0,-1):  #Ca c'est la ligne en Y
                if table[i][j] == table[i][j-1]:
                    table[i][j] *= 2                #Ca c'est les X, on les parcours à l'envers pour éviter les bug
                    table[i][j-1] = 0               #L'évolution des cases ce fait par addition de 2 cases identiques
                                                    
    elif move == 'U':                               #Donc c'est une multiplication par 2, pour pas mettre une conditon pour chaque nombre
        for i in range(len(table)):                 #Repeat chaque explication frérot
            for j in range(len(table[0])-1):

                if table[i][j] == table[i][j+1]:
                    table[i][j] *= 2
                    table[i][j+1] = 0

    elif move == 'R':
        for i in range(len(table)-1,0,-1):
            for j in range(len(table[0])):
                
                if table[i][j] == table[i-1][j]:
                    table[i][j] *= 2
                    table[i-1][j] = 0

    elif move == 'L':
        for i in range(len(table)-1):
            for j in range(len(table[0])):
                if table[i][j] == table[i+1][j]:
                    table[i][j] *= 2
                    table[i+1][j] = 0


def game(move):          #On gère ici le mouvement du tableau.
    global table
    mouvement(move)   #Le principe c'est que tout bouge, puis on fusionne, puis on rebouge pour tout mettre en ordre.
    fusion(move)
    mouvement(move)


def tablo():
    global case_graphique
    global table
    case_graphique = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            color = "gray80"
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
            if table[i][j]!=0:
                t = canvas.create_text(i*largeur_case+62, j*hauteur_case+62, text=table[i][j], font=("helvetica", "30"))
                case_graphique.append(t)
    canvas.update()


def cheat():
    global table
    table = [[0, 0, 0, 16],[0, 0, 0, 16],[0, 0, 0, 0],[0, 0, 0, 0]]
    tablo()
    score()
    poss = possibility(table)                   #Tout les moves autorisé pour que le programme te laisse pas faire n'importe quoi


def start():
    global table                #La table est global pour être facile d'accès et non-modifié entre les programmes
    ini()
    score()               #Cf programme Init
    tablo()
    poss = possibility(table)                   #Tout les moves autorisé pour que le programme te laisse pas faire n'importe quoi
    def inp(key):                       #La fonction appear quand le clavier est utilisé, je sais pas si on peut limiter le truc à 4 bouton par contre
        global table
        a = False
        poss = possibility(table)          #Tout les moves autorisé pour que le programme te laisse pas faire n'importe quoi     
        if  key == 'R' and 'R' in poss:    #Pour chaque flèche directionnel, on a un if différent pour matcher les moves
            game('R')                      #Y a que R, L, U et D
            a = True

        elif key == 'L' and 'L' in poss:    
            game('L')
            a = True

        elif key == 'U' and 'U' in poss:    
            game('U')
            a = True

        elif key == 'D' and 'D' in poss:    
            game('D')
            a = True


        if a:
            tablo()
            casebonus()
            tablo()
            score()
            lose(table)
            a = False
        


    bouton8 = tk.Button(fenetre, text="Gauche", font=("helvetica", "10"),command=lambda:inp('L'))
    bouton8.grid(column=0, row=7)

    bouton7 = tk.Button(fenetre, text="Droite", font=("helvetica", "10"),command=lambda:inp('R'))
    bouton7.grid(column=2, row=7)

    bouton6 = tk.Button(fenetre, text="Haut", font=("helvetica", "10"),command=lambda:inp('U'))
    bouton6.grid(column=1, row=6)

    bouton5 = tk.Button(fenetre, text="Bas", font=("helvetica", "10"),command=lambda:inp('D'))
    bouton5.grid(column=1, row=8)
    




label2 = tk.Label(fenetre, text="Score: 0", font = ("helvetica", "20")) 
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
    
    fenetre2 = tk.Tk()
    fenetre2.title("Fin de partie")
    label01 = tk.Label(fenetre2, text="FIN DE PARTIE", font = ("helvetica", "20"))
    label01.grid(column=0, row=0)    #Mettre victoire ou defaite au milieu des deux
    label02 = tk.Label(fenetre2, text="Score: " + str(conter(table)), font = ("helvetica", "20"))
    label02.grid(column=0, row=2)

    win = False
    for i in range(len(table)):             
        if max(table[i]) >= 2048:
            win = True
    if win:
        label03 = tk.Label(fenetre2, text="Victoire", font = ("helvetica", "30"))
    else:
        label03 = tk.Label(fenetre2, text="Perdu", font = ("helvetica", "30"))
    label03.grid(column=0, row=1)

    fenetre2.mainloop()

def lose(table):
            
    a = possibility(table)                 #Programme de gêle du jeu + écran de victoire
    if len(a) == 5 or len(a) == 0:         #On utilise sa pour verifier que y'ai pas de bug
        exit()                             #Mais on pourrait l'utiliser pour vérifier si y a une defaite dans le cas où     
        return                             #la liste est vide 


def sauvegarder():
    t=[]
    t=table.copy()
    f =open('savestate1.txt', 'w')
    json.dump(t, f) #dump : utilisée lorsque nous voulons stocker et transférer des objets dans un fichier sous forme de JSON 
    f.close()

def charger():
    global table
    f=open('savestate1.txt', 'r')
    charge = json.load(f)
    table=[]
    for i in range(len(charge)):
        h=[]
        table.append(h)
        for l in charge[i]:
            h.append(l)
    tablo()
    score()
    f.close()


#-------------------------------------------------------------------------------
#Bouton


bouton1 = tk.Button(fenetre, text="Nouvelle Partie", font=("helvetica", "10"),command=start)
bouton1.grid(column=6, row=1)

bouton2 = tk.Button(fenetre, text="Exit", font=("helvetica", "10"),command=exit)
bouton2.grid(column=6, row=2)

bouton3 = tk.Button(fenetre, text="Save", font=("helvetica", "10"),command=sauvegarder)
bouton3.grid(column=6, row=3)

bouton4 = tk.Button(fenetre, text="Load", font=("helvetica", "10"),command=charger)
bouton4.grid(column=6, row=4)

bouton9 = tk.Button(fenetre, text="Cheat", font=("helvetica", "10"), command=cheat)
bouton9.grid(column=6, row=5)


fenetre.mainloop()
