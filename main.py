#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
"""
Module principal pour la génération d'art ASCII et l'encodage de chaînes.
"""
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)

#### Fonctions secondaires

def artcode_i(s: str):
    """
    Fonction d'encodage itératif pour l'art ASCII.
    """
    if s == "":
        return []
    chars = [s[0]]
    occurences = [1]
    for k in range(1, len(s)):
        if s[k] == s[k-1]:
            occurences[-1] += 1
        else:
            chars.append(s[k])
            occurences.append(1)
    return list(zip(chars, occurences))

def artcode_r(s: str):
    """ 
    Fonction d'encodage récursif pour l'art ASCII.
    """
    if s == "":
        return []
    premier = s[0]
    tuple_premier = (premier, ord(premier))
    reste_code = artcode_r(s[1:])
    return [tuple_premier] + reste_code

#### Fonction principale

def main():
    """
    Fonction principale pour tester les encodages ASCII-art.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
