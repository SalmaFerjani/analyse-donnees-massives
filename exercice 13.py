# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 01:12:22 2023

@author: Salma
"""

n=int(input("Entrer un entier n :"))
list=[]
def Diviseur(n):
    for i in range(1,n+1):
        if n%i==0 :
            print(f"{i} est parmi les diviseur de {n}")
            list.append(i)
        else :
            print(f"{i} n'est pas parmi les diviseurs de {n}")
print(Diviseur(n),list)