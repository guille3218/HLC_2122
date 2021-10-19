lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]
lista2 = []

for x in range(len(lista)-1):
    if lista[x]!="":
      lista2.append(lista[x])

print(lista2)