# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 01:46:52 2023

@author: Salma
"""

def multiplication():
    for i in range(1,10) :
        tab=[i]
        for j in range (1,i+1):
            for z in range (1,i+1):
                multi=j*z
                tab.append(multi)
    return tab
resultat = multiplication()
for ligne in resultat:
    print(ligne)