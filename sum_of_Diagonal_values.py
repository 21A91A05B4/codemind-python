r,c=map(int,input().split())
a=[list(map(int,input().split()))for i in range(r)]
s=0
t=0
for i in range(r):
    for j in range(c):
        if i==j:
            s=s+a[i][j]
for i in range(r):
    if i!=r-i-1:
        t=t+a[i][r-i-1]
print(s+t)