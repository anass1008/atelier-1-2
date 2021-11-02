def div(l): #Declaration d'une function qui divise une liste en 3 morceaux égaux et inverser chaque morceau
    l1 = []
    l2 = []
    l3 = []
    for i in range(len(l)):
        if i < 3:
            l1.append(l[i])

    for j in range(3,len(l)):

        if j < 6:
            l2.append(l[j])

    for k in range(6,len(l)):

        if k < 9:
            l3.append(l[k])

    return print(l1[::-1] , l2[::-1] ,l3[::-1])
list = [1,2,3,4,5,6,7,8,9]
div(list) #calling the function