"""Exercice 01
Écrire un programme en langage python qui affiche les  nombres entiers premiers parmi les nombres de 1 à 100"""

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
    finally:
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
    finally :
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
Exo7()

"""Exercice 08
Écrire un programme en langage python qui permet de trouver les nombres qui sont divisibles par 7 ,multiple de 3 et multiple de 5, entre deux bornes choisit par l’utilisateur (tous deux inclus).L’utilisateur doit saisir deux nombres positifs et le deuxième nombre doit être supérieur au premier
Dans le même programme:
Afficher le nombre des nombres trouvés
Afficher la somme des nombres trouvés
Afficher la liste des nombres trouvés"""