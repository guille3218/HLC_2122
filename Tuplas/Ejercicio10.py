tupla = (45, 45, 45, 45)

a=tupla[0]

same = True

for x in range(len(tupla)):
    if a != tupla[x]:
        same = False
        break
    
print(same)