try:
    n = int(input("Donnez un entier n : "))
    if n < 0:
        raise ValueError
except ValueError:
    print("Veuillez entrer un entier positif.")
while True and n>0 :
     if n % 2==0 :
        print("n est un entier PAIR")
        break
     else:
        print("n est IMPAIR")
        break

