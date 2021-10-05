str1 = "C@#he26ma^&Du5ran"
char = 0
digit = 0
symbol = 0
for x in str1:
    if(x.isdigit()):
        digit += 1
    elif(x.isalpha()):
        char += 1
    else:
        symbol += 1   

print("Carácteres = ", char)
print("Digitos = ",digit)
print("Símbolos = ", symbol)