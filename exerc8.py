def find(str , char): # declaration d'une fuction qui  trouver la fréquence d’un caractère dans une chaîne.
    return str.count(char)
str1 = input("entrer le string :")
char1 = input("entrer le char :")
print("le char",char1 , "repeter",find(str1 , char1) ,"fois")#calling the function
