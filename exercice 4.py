# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:10:19 2023

@author: Salma
"""

from math import *
rayon=int(input("saisir le rayon de cercle :"))
def calculs (rayon):
    surface=3.14*rayon**2
    périmétre=3.14*rayon*2
    return surface , périmétre
resultat=calculs(rayon)
print(f"le périmétre et la surface de cercle sont {resultat}")
