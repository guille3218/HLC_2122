s1 = "Abc"
s2 = "Xyz"
s3 = ""

s1l = len(s1)
s2l = len(s2)

if s1l < s2l:
    mostL = s2l
else:
    mostL = s1l

i=0
while i < mostL:
    if s1l > 0:
        s3 += s1[i]
        s1l -= 1
    if s2l > 0:
        s3 += s2[(len(s2)-1)-i]
        s2l -= 1
    
    i +=1
print(s3)