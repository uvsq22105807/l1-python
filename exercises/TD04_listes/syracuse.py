###################################################################



def syracuse(n):
    L=[]
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        L.append(n)
    return(L)

print(syracuse(100))


##################################################################


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(1,n_max):
        syracuse(i)
    return True
print(testeConjecture(10000))


##################################################################


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))
print("Le temps de vol de", 3, "est", tempsVol(3))


##################################################################


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    A=[]
    for i in range(1,n_max):
        A.append(tempsVol(i))
    return A    

print(tempsVolListe(10000))


##################################################################

B=tempsVolListe(10000)
maximum=0
indice=0
for i in range(0, len(B)):
    if B[i]>maximum:
        maximum=B[i]
        indice=i
    else:
        maximum=maximum
        indice=indice

print("Le plus grand temps de vol est", maximum ,"pour le vol", indice+1)

##################################################################



##################################################################
