s=input()
b=[]
c=-1
for i in s.split():
    c+=1
    if(c%2==0):
        b.append(i[::-1])
    else:
        b.append(i)
print(*b)
        