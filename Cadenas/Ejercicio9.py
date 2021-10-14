
#Cadena inicial
str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"

#Se crea una cadena en la que solo están los números y los espacios
str2 = ""
for x in str1:
    if(x.isdigit()):
        str2 += x

    if(x == " "):
        str2 += x

#Se crea una lista con numeros y algunos nulos
numbersSpace = str2.split(" ")

#Se crea una lista con solo números
numbersWithoutSpace = []
for x in numbersSpace:
    if (x != ""):
        numbersWithoutSpace.append(x)

#Suma de los números
total=0
for x in numbersWithoutSpace:
    total += int(x)

#promedio de los números
promedio = total/len(numbersWithoutSpace)

#Salida por consola
print("La suma es",total)
print("El promedio es",promedio)