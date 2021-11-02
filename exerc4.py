def fibonacci(n): #declaration d'une function qui imprimer la serie de Fibonacci
    if n in [0,1]:
         return n
    else:
        return fibonacci(n-1) +fibonacci(n-2)
n = int(input("Entrer une valeur :"))
print("la serie de fibonacci est :",end=' ')
list = [fibonacci(i) for i in range(n)]
for i in list:
    print(i , end=' ') #imprimer la serie dans un ligne


