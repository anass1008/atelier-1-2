def binaire(n): #declartion d'un funct qui convertir le nombre décimal en nombre binaire
     if n == 0 :
         return 0
     else:
         return n%2 + (10*binaire(n//2))
n = int(input("entrer la valeur de n :"))
print("le binaire de la valeur ",n ,"est :" ,binaire(n))  #calling the function
