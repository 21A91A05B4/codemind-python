s=input()
s=s.lower()
d=0
for i in range(len(s)):
    if s.count(s[i])==1:
        c=i
        d+=1
        break
if d==0:
    print(-1)
else:
    print(c)