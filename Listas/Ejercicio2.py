lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]

lista3=""
i=0
while(i<len(lista1)):
    lista3+=lista1[i]
    lista3+=lista2[i]
    lista3+= " "
    i+=1

print(lista3)