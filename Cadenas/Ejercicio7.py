s1 = "hDtarC"
s2 = "ChemaDuran"

equilibrado = False

for x in s1:
    if x in s2:
       equilibrado = True
    elif x not in s2:
        equilibrado = False
        break


print(equilibrado)