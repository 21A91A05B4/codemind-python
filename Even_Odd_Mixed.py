n=int(input())
en=0
on=0
while n:
    d=n%10
    n=n//10
    if(d%2==0):
        en+=1
    else:
        on+=1
if(on>=1 and en>=1):
    print('Mixed')
if(en>=1 and on==0):
    print('Even')
if(on>=1 and en==0):
    print('Odd')
    