# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:05:14 2023

@author: Salma
"""

def LireN():
    while True :
       try :
           N=int(input("saisir un entier n entre 0 et 20 :"))
           if N not in range(1,21):
               print("donner une entier entre 0 et 20")
           else :
               return N
       except ValueError :
               print("!!! ajouter un valeur correct !!!")
def RemplirL(N):
    L=[]
    for i in range(N+1):
        while True :
            try :
                L=input("saisir un entier n entre 0 et 100 :")
                if N not in range(0,101):
                   print("donner une entier entre 0 et 100")
                else :
                   break
            except ValueError :
                  print("!!! ajouter un valeur correct !!!")
    return L
def SupprimeDoublons(L):
    L1 = []
    for x in L:
        if x not in L1:
            L1.append(x)
    return L1