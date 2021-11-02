def funct(n): #declaration d'une function qui compter les chiffres d'un nombre donné
   if n < 10:
       return 1
   else:
       return 1 + funct(n//10)
n = int(input("entrer un nombre :"))
print("cette nombre",n,"contient",funct(n) , "chiffre") #calling the function



