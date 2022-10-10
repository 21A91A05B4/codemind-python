s=input()
v='aeiouAEIOU'
f='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
c=0
x=0
k=len(s)-1
while(x<k):
    if (s[x] in v and s[k]  in f) or (s[x] in f and s[k]  in v):
        c+=1
    x+=1
    k-=1
print(c)