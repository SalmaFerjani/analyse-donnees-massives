# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 01:30:45 2023

@author: Salma
"""

import numpy as np

def random_mat(N) :
    M = 5 + 5 * np.random.randn(N,2)
    M[:,1]=2*M[:,0] 
    return M


def build_m(M, N, n=2):
    while (n>0):
        i = np.random.randint(N-1)
        j = np.random.randint(1)
        M[i , j] = np.nan
    return M

def nettoyage(M) :
    medcolonne=np.nanmedian(M,axis=0)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if np.isnan(M[i,j]):
                M[i,j]=medcolonne[j]
    return M
#PP
mat=random_mat(5)
print("matrice M :",mat)
mat=build_m(mat,5)
print("matrice NAN M : ",mat)
mat=nettoyage(mat)
print("matrice median M : ",mat)


