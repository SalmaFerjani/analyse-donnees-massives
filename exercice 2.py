try:
    n = int(input("Donnez un entier positif n : "))
    if n < 0:
        raise ValueError
except ValueError:
    print("Veuillez entrer un entier positif.")
else:
    val = n
    resultat = 0
    while val % 2 == 0:
        resultat += 1
        val = val // 2
    print(f"{n} est divisible par 2 : {resultat} fois")

