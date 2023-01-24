

def duz_liste_yap(liste):
    if not isinstance(liste,list):
        return [liste]
    
    elif not liste:
        return []
    else:
        print(duz_liste_yap(liste[0]))
        
        return duz_liste_yap(liste[0]) + duz_liste_yap(liste[1:])
        

l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]

print(duz_liste_yap(l))