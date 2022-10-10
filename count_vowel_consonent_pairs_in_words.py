s=input()
s.lower()
s=s.split()
v='aeiou'
c=0
for i in s:
    x=0
    k=len(i)-1
    while x<k:
        if (i[x] in v and i[k] not in v) or (i[x]  not in v and i[k]in v):
            c+=1
        x+=1
        k-=1
print(c)