tupla = (('a', 23),('b', 37),('c', 11), ('d',29))

print(tupla)

lista = list(tupla)

lista.sort(key = lambda x: x[1])

tupla = tuple(lista)

print(tupla)