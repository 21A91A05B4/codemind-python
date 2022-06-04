n=int(input())
b=[]
c=0
while n>0:
    d=n%10
    n=n//10
    if d not in b:
        b.append(d)
    else:
        c=1
if c==0:
    print('Unique Number')
else:
    print('Not Unique Number')