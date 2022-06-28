r,c=map(int,input().split())
a=[list(map(int,input().split()))for i in range(r)]
s=0
e=0
for i in range(r):
    for j in range(c):
        if a[i][j]%2==0:
            s=s+a[i][j]
print(s,end=' ')
for i in range(r):
    for j in range(c):
        if a[i][j]%2!=0:
            e=e+a[i][j]
print(e)