# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:04:56 2023

@author: Salma
"""
import random
Liste=[]
def LireN():
    N=random.randint(0, 21)
    return N
print(LireN())
def RemplirL(N):
   for i in range (1,N+1):
       while True :
           try 
               Liste 
       element=random.randint(1, 101)
       Liste.append(element)
   return Liste
print(RemplirL(20))
def SupprimeDoublons(Liste,N):
    for i in range(1,N+1):
        x=Liste.count(i)
           while x != 1 :
                Liste1=Liste.remove(i)
    return Liste1
print(SupprimeDoublons(Liste,10))
        
    
        
    