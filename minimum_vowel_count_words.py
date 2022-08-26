s=input()
s=s.split()
b=[]
f=[]
l=''
c=0
a=0
for i in s:
    b.append(i)
v='aeiouAEIOU'
for i in b:
    l=i
    #print(l)
    for j in l:
        if j in v:
            c+=1
    f.append(c)
    c=0
    l=''
#print(f)
w=min(f)
z=0
i=0
for i in f:
    if i==w:
        z+=1
print(z)
    
    