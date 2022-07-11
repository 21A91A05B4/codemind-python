s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
d=[]
c=0
for i in s2.split():
    if  i in s1.split():
        c+=1
        d.append(i)
if(c==0):
    print('-1')
else:
    print(*d)