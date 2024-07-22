#le but de ce jeux c'est que l'ordinateur saisir un entier entre high et low puis vous cherche ce entier si c'est vrai 
#le pragramme affiche que c'est vrai sinon il vous aidez pour cherche ce valeur 
import random
def guess(x):
     low=1
     high=10
     rand_value=random.randint(low,high)
     while guess != rand_value :
         value=int(input("saisir un entier"))
         if value < low :
              print(f"{value} est plus petit que {low}")
         elif value>high :
              print(f"{value} est plus grand que {high}")
print(f"Correct, {rand_value} c'est la réponse correct")
guess(5)