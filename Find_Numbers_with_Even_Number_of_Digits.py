n=int(input())
a=list(map(int,input().split()))
#b=list(map(int,input().split()))
#b=[]
ec=0
#for i in a:
   # if i not in b and a.count(i)>1:
        #b.append(i*i)
        #c+=1
for i in range(len(a)):
    c=0
    while(a[i]>0):
        d=a[i]%10
        a[i]=a[i]//10
        c+=1
    if c%2==0:
        ec+=1
print(ec)