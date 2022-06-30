n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    if a[i]!=0 and a[i]!=1:
        s=1
        break
if s==0:
    print('True')
else:
    print('False')