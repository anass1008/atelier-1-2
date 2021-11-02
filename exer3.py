def somme(n): #Declaration d'une fuct qui calcule la somme de 1 jusqu'a n
    if n == 1 :
        return 1
    else:
        return n + somme(n-1)   #la récursivité
x = int(input("Entrer une valeur :"))
print("la somme de 1 jusq'a ",x ,"est :" ,somme(x)) #calling the fuct

