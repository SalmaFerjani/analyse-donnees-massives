# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 14:17:24 2023

@author: Salma
"""
import tkinter as tk
import random
fenetre = tk.Tk()
fenetre.title("random-project")
fenetre.geometry("200x100")
def guess(x):
    rand_value=random.randint(1, x)
    guess=0
    guess =int(input(f"Guess the number between 1 and {x}"))
    if guess < rand_value :
         print(f"Sorry, Guess again, {guess} is to low")
    elif guess > rand_value :
         print(f"Sorry, Guess again, {guess} is to high")
    else : 
         print("correctly")
guess(5)
fenetre.mainloop