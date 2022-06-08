n=int(input())
x=list(map(int,input().split()))
temp=0
for i in range(len(x)):
    if(x[i]%2!=0):
        temp+=1
if temp<=2:
    print('YES')
else:
    print('NO')