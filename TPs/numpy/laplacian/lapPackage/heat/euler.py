# -*- coding: utf-8 *-*

def euler(u, dt, f, fargs=()):
    """
    Euler explicite pour un système 

    d u
    --- = f(u, t)
    d t
    
    Parameters :
    ------------

    u: solution à l'instant n
    
    dt:  pas de temps du schéma
    
    f: fonction second membre

    fargs: paramètres optionnels de la fonction autre que u

    """
    return u + dt*f(u, *fargs)
