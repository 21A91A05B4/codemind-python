s=input()
v=0
c=0
d=0
l=0
for i in s:
    if i>='0' and i<='9':
        d+=1
    elif i=='A' or i=='E' or i=='O' or i=='I' or i=='U' or i=='a' or i=='e' or i=='i'or i=='o' or i=='u':
        v+=1
    elif i==' ':
        l+=1
    else:
        c+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',l)