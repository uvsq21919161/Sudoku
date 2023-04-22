from random import shuffle, randint

grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1, 9+1):
        print("".join(n+s for (n, s)
              in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])

    return

def unique(x) :
    """renvoie true si tous les elements de x sont differents (sauf 0)"""
    doublons = []
    for e in x :
        if e == 0 :
            continue
        if e in doublons :
            return False
        doublons.append(e)
    return True

def ligne(x,i) :
    """renvoie la ligne i d'un sudoku"""
    return x[i-1]

def colonne(x,i) : 
    """renvoie la colonne d'un sudoku"""
    return [ligne[i-1] for ligne in x]

def region(x,i) :
    """renvoie la region i d'un sudoku"""
    i-=1
    return [item for sublist in [ligne[3*(i%3):3*(i%3)+3] for ligne in x[3*(i//3):3*(i//3)+3]] for item in sublist]
    
def ajouter(x, i, j, v) :
    """ajoute la valeur v au coordonnees (i,j) sur la grille x"""
    old_value = x[i-1][j-1] 
    x[i-1][j-1] = v
    v_region = 3*((i-1)//3) + ((j-1)//3) +1

    if not (unique(region(x,v_region)) and unique(colonne(x,j)) and unique(ligne(x,i))) :
        x[i-1][j-1] = old_value
    return

def verifier(x) :
    """verifie que la grille a ete correctement remplie
       (si la grille ne contient aucun 0 et
        les lignes colonnes et regions sont valides)"""
    #on verifie que toutes les cases soient pleines
    for line in x :
        for case in line :
            if case == 0 :
                return False
    #on verifie toutes lse colonnes, lignes, et regions
    for i in range(1,10) :
        if not (unique(region(x,i)) and unique(colonne(x,i)) and unique(ligne(x,i))) :
            return False
    return True

def jouer(x) :
    while not verifier(x) :
        afficher(x)
        try :
            j = int(input("Entrez la colonne :\n"))
            i = int(input("Entrez la ligne :\n"))
            v = int(input("Entrez la valeur :\n"))
            if i<1 or i>9 or j<1 or j>9 or v<0 or v>9 :
                raise ValueError
        except ValueError:
            print("Entrees incorrectes, les valeures acceptees sont les entiers 1-9")
            continue
        ajouter(x,i,j,v)
    print("Bravo! vous avez resolu le sudoku!")
    return

def solutions(x) :
    """renvoie un dictionnaire contenant
    les valeurs potentielles de chaque case vide de x"""
    #etape 1
    answers = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[] , 8:[], 9:[]}
    #etape 2
    for i in range(9):
        for j in range(9) :
            if x[i][j] == 0 :
                v_region = 3*(i//3) + (j//3) +1
                valeurs_presentes = region(x,v_region) + colonne(x,j+1) + ligne(x,i+1)
                valeurs_potentielles = [v for v in [1,2,3,4,5,6,7,8,9] if v not in valeurs_presentes]
                #etape 3
                answers[len(valeurs_potentielles)].append((i+1,j+1,valeurs_potentielles))
    return answers

def resoudre(x) :
    """resouds la grille de sudoku x"""
    #etape 1
    answers = solutions(x)
    l = [item for sublist in answers.values() for item in sublist]
    #etape 2
    if answers[0] != [] :
        return False
    if l == [] :
        return x
    
    #etape 3
    for (i,j,v) in l :
        for t in v :
            ajouter(x,i,j,t)
            
            if resoudre(x) :
                return x
            else :
                ajouter(x,i,j,0)

        return False

def generer(x) :
    """cree une grille aleatoire a partir d'une grille vide"""
    #etape 1
    answers = solutions(x)
    l = [item for sublist in answers.values() for item in sublist]
    #etape 2
    if answers[0] != [] :
        return False
    if l == [] :
        return x
    
    #etape 3
    shuffle(l)
    for (i,j,v) in l :
        shuffle(v)
        for t in v :
            ajouter(x,i,j,t)
            if resoudre(x) :
                return x
            else :
                ajouter(x,i,j,0)

        return False

def nouvelle() :
    """cree une nouvelle grille de sudoku"""
    #etape 1
    new_map = [[0 for i in range(9)] for j in range(9)]
    generer(new_map)
    #etape 2
    cases_pleines = [(i,j) for i in range(9) for j in range(9) if new_map[i][j]!=0]
    while(len(cases_pleines)>17) :
        (i,j) = cases_pleines[randint(0,len(cases_pleines)-1)] #case a supprimer
        new_map[i][j] = 0
        cases_pleines = [(i,j) for i in range(9) for j in range(9) if new_map[i][j]!=0]
    return new_map





jouer(nouvelle())


"""afficher(nouvelle())
afficher(resoudre(nouvelle()))

"""