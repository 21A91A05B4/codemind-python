s=input()
n=int(input())
m=n%len(s)
l=n//len(s)
c=0
for i in s:
    if i=='a':
        c+=1
na=l*c
d=0
for i in range(0,m):
    if s[i]=='a':
        d+=1
print(na+d)
            