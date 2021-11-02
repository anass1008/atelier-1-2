def tri_bulle(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0,n-i-1):
            if tab[j] > tab[j+1]:
                tab[j],tab[j+1] = tab[j+1],tab[j]
    return tab
def tri_selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1 , len(tab)):
            if tab[min] > tab[j]:
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return  tab
def tri_insertion(tab):
    for i in range(1,len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j]:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = k
    return tab



tab = [11,25,36,24,87,98,26,14,278]
print("tri a bull :" , tri_bulle(tab))
print("tri par selection :" , tri_selection(tab))
print("tri par insertion :" , tri_insertion(tab))