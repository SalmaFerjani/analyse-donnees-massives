# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 01:26:20 2023

@author: Salma
"""

tab=[]
n=int(input("saisir un entier n :"))
def multiplication(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            multi=i*j
            tab.append(multi)
    return tab
print(multiplication(n))