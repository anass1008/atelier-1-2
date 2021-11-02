def chang_dict(l): #declaration d'une function qui changer un list vers un dict
    dic = {}
    for i in l:
        a = l.count(i) #calculer combien des fois un elemets repeter dans la liste
        dic[i] = a

    return dic
list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(chang_dict(list)) #calling the function