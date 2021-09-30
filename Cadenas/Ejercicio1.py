str = "ChemTioaDur"

if(len(str) % 2 != 0 and len(str) >=7 ):
    str2 = str[round(len(str)/2)-2:round(len(str)/2)+1]


print(str2)