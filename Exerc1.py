#declaration d'un fonct qui calcule le factoriell Ex : 3! = 3*2*1
def facturiel(n):
    if n == 0 :
        return 1
    else :
        return n*facturiel(n-1)
def summ(x):  # declaration d'une funct qui calcule la somme des series n!/n + .... + 1!/1
    n = 0
    for i in range(1,x+1):
        n += facturiel(i)/i
    return n
x = int(input("entrer une valeur :"))

print("la somme de la serie est :" , summ(x)) #calling the function
