r,c=map(int,input().split())
a=[list(map(int,input().split())) for i in range(r)]
for j in range(c):
    max=0
    for i in range(r):
        if a[i][j]>max:
            max=a[i][j]
    print(max)