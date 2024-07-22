# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 08:57:53 2023

@author: Salma
"""
import numpy as np

def Mad (M , axis=None):
    mad = np.median(M, axis, keepdims=True)
    m= np.abs(M-mad)
    return np.median(m, axis)

m =np.random.randint(10,100,size=(2,3))
mad = Mad(m)
print("la medianne de la matrice est : ", mad)
mad_0 = Mad(m, 0)
print("la longeur de l'axe 0 (colonnes) : ", mad_0 )
mad_1 = m=Mad(m, 1)
print("la longeur de l'axe 1 (lignes) : ", mad_1)




