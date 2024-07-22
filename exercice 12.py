# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:33:12 2023

@author: Salma
"""
mydict = {"devise":"laptop","constructeur":"acer","ram":"8G","processeur":"intel core i5","stockage":"500G"}
L1=[]
L2=[]
L3=[]
print(f"voici le dictionnaire : {mydict}")
for cle,valeur in mydict.items() :
    L1=L1+[cle]
print(f"{L1} sont les clés dans le dictionnaire")
for cle,valeur in mydict.items() :
    L2=L2+[valeur]
print(f"{L2}sont les valeur dans le dictionnaire")
for cle,valeur in mydict.items():
    L3=L3+[cle,valeur]
print(f"{L3}sont les cle et les valeur dans le dictionnaire")
mydict["Système d'exploitation"]="Windows 10"
print(f"le dictionnaire finale est {mydict}")
key=input("saisir un clé :")
if key in L1 :
     print(f"{key} exist dans mydict")
else :
     print(f"{key} n'existe pas dans mydict")
value=input("saisir un valeur :")
if value in L2 :
     print(f"{value} exist dans mydict")
else :
     print(f"{value} n'existe pas dans mydict")
     
     
     