n=int(input())
l=list(map(int,input().split()))
b=[]
c=0
for i in l:
    if i not in b and l.count(i)==i:
        b.append(i)
        c+=1
print(c)