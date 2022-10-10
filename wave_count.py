n=int(input())
a=list(map(int,input().split()))
b=[]
d=[]
c=0
s=0
for i in range(len(a)):
    if(i%2==0):
        b.append(a[i])
    else:
        d.append(a[i])
for i in range(len(a)//2):
    if(b[i]>d[i]):
        c=1
        break
    else:
        s+=1
if(c==1):
    print('-1')
else:
    print(len(b)-1)
    