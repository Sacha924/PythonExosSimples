"""Exercice 01
Écrire un programme en langage python qui affiche les  nombres entiers premiers parmi les nombres de 1 à 100"""

from distutils.log import error
from regex import E
from random import randint

from sqlalchemy import false, true



def getNbDivisor(number):
    return [d for d in range(1,100)if number%d==0]      
def Ex1():
    for number in range(1,101):
        if (len(getNbDivisor(number))==2):
            print(number)
#Ex1()

"""Exercice 03
Écrire un programme en langage python qui permet de saisir un entier positif composé de cinq chiffres différents , puis de vérifier et d’afficher si cet entier obéit à la règle ou non."""

def Exo3():
    nombre = -1
    try:
        nombre = int(input("saisir un entier positif composé de cinq chiffres différents : "))
    except:
        pass
    else:
        mySet = set()
        for chiffre in str(nombre):
            mySet.add(chiffre)
        if(len(mySet)==5 and len(nombre)==5):
            print(nombre)
        else : print("le nombre saisi ne respecte pas la règle qui est de contenir 5 chiffres différents")
#Exo3()

"""Exercice 04
Écrire un programme nombreVoyelles qui affiche le nombre de voyelles d’un mot (écrit en minuscule, sans caractère accentué).
Ce petit programme va nous permettre de voir comment on manipule facilement les chaînes de caractères avec Python.
Dans la boucle principale, on demande à l’utilisateur de saisir un mot. Le programme affiche alors le nombre de voyelles du mot donné."""
def Exo4():
    count = 0
    tabVoyelle = ["a","e","i","o","u","y"]
    for lettre in input("saisissez votre mot : "):
        if (lettre in tabVoyelle):
            count +=1
    print(count, " voyelle(s)")
#Exo4()

"""Exercice 05
Écrire programme en python permettant de lire un nombre entier N puis calcule son factoriel en utilisant une boucle while
Le programme ne se plante pas si l’utilisateur à décidé de saisir “bonjour” ou un nombre négatif plus-tôt que 6 par exemple ."""
def Exo5():
    nombre =-1
    try:
        nombre = int(input("saisissez un nombre : "))
    except: pass
    else :
        if(nombre <0) : print("Saisie invalide")
        else :
            nombreSaisi = nombre
            res = nombre
            while(nombre>1):
                nombre-=1
                res*= nombre 
            print("%d! = %d" % (nombreSaisi,res))
#Exo5()

"""Exercice 06
Énoncé
Écrire un programme en python qui affiche les tables de multiplications de 1 à N.
N : est un entier supérieur à zéro saisie par l’utilisateur.
Gérer l’affichage en ajoutant des espaces après chaque table.
Le résultat après exécution est donné par l’image suivant"""

def Exo6():
    N = int(input("saisir valeur : "))
    N+=1
    #Première ligne
    display =""
    for i in range(1,N):
        print(i, end= " ".ljust(8-len(str(i))))
        if(i+1!=N):
            display += "_"*8
        else :
            display+= "_"*len(str(10))
            
    print("\n",display)
    for i in range(1,N):
        for j in range (1,N):
            print(i*j, end= " ".ljust(8-len(str(i*j))))
        print()
#Exo6()
"""
mygenerator = (x*x for x in range(3))
print(type (mygenerator))
for i in mygenerator:
    print(i)"""
    
"""Exercice 07
Écrire un programme en langage python qui permet d’afficher un triangle isocèle formé d’étoile(*).
La hauteur du triangle (c ‘est a dire le nombre des lignes)sera fournie en donnée,comme dans l exemple ci dessous.
Le nombre des caractères étoiles(*) sur la base sera le double de hauteur du triangle
"""
def Exo7():
    heigth = int(input("saisissez la hauteur du triangle : "))
    for loop in range(heigth):
        line = "*"+ "*"*2*loop
        print("".rjust(heigth-loop), line)
#Exo7()

"""Exercice 08
Écrire un programme en langage python qui permet de trouver les nombres qui sont divisibles par 7 ,multiple de 3 et multiple de 5, entre deux bornes choisit par l’utilisateur (tous deux inclus).L’utilisateur doit saisir deux nombres positifs et le deuxième nombre doit être supérieur au premier
Dans le même programme:
Afficher le nombre des nombres trouvés
Afficher la somme des nombres trouvés
Afficher la liste des nombres trouvés"""

def Exo8():
    # je pourrais faire un try catch pour éviter que l'utilisateur saisisse du texte, mais bon déjà fait dans d'autres exos. 
    bornInf = int(input("saisir la borne inférieure : "))
    bornSup = int(input("saisir la borne supérieur : "))
    if(bornSup<bornInf):
        while(bornSup<bornInf):
            print("veuillez saisir une borne supérieure > borne inférieure, borne sup actuelle : %d, borne inf actuelle : %d" %(bornSup,bornInf))
            bornSup = int(input("saisir la borne supérieur : "))
    for number in range(bornInf,bornSup+1):
        if(number%3==0 and number%5==0 and number%7==0):
            print(number)
#Exo8()

"""Exercice 10
Écrire un programme en langage python qui permet d’afficher les N premiers termes d’une suite dite "Suite de Fibonacci".
Le nombre N est fournit par l’utilisateur.
Il s’agit d’une suite de nombres dont chaque terme est égal à la somme des deux termes qui le précèdent.
Ses deux premiers termes sont 0 et 1, et ensuite, chaque terme successif est la somme des deux termes précédents. Ainsi 0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8, etc.
"""

def Exo9():
    N = int(input("saisir le nombre de termes de la suite de Fibonacci : "))
    F_0,F_1 = 0 ,1   #terme à n = 0 initiallement   #terme à n = 1 initiallement
    print("F_0 = ",F_0 , "\n" , "F_1 = ",F_1, sep="")
    for loop in range(2,N+1):
        memory = F_1
        F_1 = F_0+F_1   #create the term F_n
        F_0 = memory    #the former F_n become F_n-1
        print("F_%d = %d" % (loop,F_1))
#Exo9()

"""recursive way : """
def Recursive_fib(n):
    if(n==0 or n==1):
        return n
    return Recursive_fib(n-1)+Recursive_fib(n-2)
n = 12
for i in range(n+1):
    print(Recursive_fib(i))



"""Exercice 04
Écrivez un programme en python, qui demande à l’utilisateur de: Saisir deux nombres et qui doit trouver le plus grand diviseur commun entre ces deux nombres.
"""
def Ex4():
    a,b = int(input("saisir a : ")),int(input("saisir a : "))
    for loop in range (1,min(a,b)+1):
        if(a%loop==0 and b%loop==0):
            diviseur = loop
    print(diviseur)
    
#Ex4()

"""Exercice 05
Écrire un jeu dans lequel python choisit aléatoirement un nombre entre 0 et 99.
L’ordinateur choisit au hasard un nombre mystère. Le joueur propose une réponse.
L’ordinateur répond “le nombre à trouver est plus grand” ou “le nombre à trouver est plus petit” ou “bravo, c’est le bon nombre !”
Pour compliquer le jeu, l’ordinateur a le droit de mentir de temps en temps. Environ une fois sur quatre l’ordinateur donne la mauvaise indication “plus grand” ou “plus petit”."""
def Ex5():
    value = randint(0, 99)
    repPlayer = int(input("saisissez une valeur : "))
    while (repPlayer != value):
        if(randint(0,3)==0): lie = True
        else : lie = False
        
        if(repPlayer>value):
            if(lie): print("la valeur recherchée est plus grande")
            else : print("la valeur recherchée est plus petite")
        if(repPlayer<value):
            if(lie): print("la valeur recherchée est plus petite")
            else : print("la valeur recherchée est plus grande")
        
        repPlayer = int(input("saisissez une valeur : "))
    print("congrats ! %d is the good answer" % value)
#Ex5()


"""hangman game"""
import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def HangmanGame():
    alive,finished,alreadySaid,myLetter,errorCount = True,False,[],"",0
    letterSelectedWord = list(words[randint(0,len(words)-1)])
    currentRepr = letterSelectedWord[0] +"_" * (len(letterSelectedWord)-2)+letterSelectedWord[len(letterSelectedWord)-1]
    while(alive and not finished):
        print(currentRepr)
        print(HANGMAN_PICS[errorCount])
        if(len(alreadySaid)!=0):
            print("letters you already said : %s" % alreadySaid)
        while(myLetter in alreadySaid or myLetter == ""):
            myLetter = input("Enter a letter : ")
        alreadySaid.append(myLetter)
        if(myLetter in letterSelectedWord):
            indexs =  [i for i in range(len(letterSelectedWord)) if myLetter == letterSelectedWord[i]]
            currentRepr = list(currentRepr)
            for index in indexs :
                currentRepr[index] = myLetter
            currentRepr = "".join(currentRepr)
        else:
            errorCount += 1
            print(HANGMAN_PICS[errorCount])
            if(errorCount==len(HANGMAN_PICS)-1):
                alive = False           
        if(currentRepr.count("_") == 0):
            finished = True
    if(finished):
        print("You WIN")
    else:
        print("You LOSE")
    print("the word was %s" % "".join(letterSelectedWord))
#HangmanGame()

#RQ :Alors que les variables de classe sont normalement déclarées sous la définition de classe en dehors de toutes les méthodes et autres
# variables, les variables de classe globale sont déclarées en dehors d’une classe. Ils sont accessibles par n’importe quelle méthode et classe.


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()
            self.fix_spot(row - 1, col - 1, player)
            
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            if self.is_board_filled():
                print("Match Draw!")
                break

            player = self.swap_player_turn(player)
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
        
        
        
    
"""travailler sur les méthodes de tri"""