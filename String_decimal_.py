T=int(input())
for t in range(1,T+1):
    s=input()
    c=0
    f=0
    for i in s:
        if i>='0' and i<='9':
            c+=1
        else:
            f=1
    if f==1:
        print('False')
    else:
        print('True')