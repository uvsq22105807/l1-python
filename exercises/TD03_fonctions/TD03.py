def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return ((temps[0]*3600*24) + (temps[1]* 3600) + (temps[2]*60) + temps[3])

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j= seconde//(3600*24)
    h= (seconde-(j*3600*24))// 3600
    m= (seconde-(j*3600*24)-(h*3600))// 60
    s= (seconde-(j*3600*24)-(h*3600)-(m*60))
    return (j, h, m, s)
    
temps = secondeEnTemps(342094)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")






#fonction auxiliaire ici

def afficheTemps(temps):
    if 
    
    
afficheTemps((1,0,14,23))   