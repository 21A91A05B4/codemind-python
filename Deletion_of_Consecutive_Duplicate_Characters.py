t=int(input())
for i in range(t):
    s=input()
    b=[]
    c=0
    for i in s:
        if(len(b)==0):
            b.append(i)
        else:
            if(b[-1]==i):
                c+=1
            else:
                b.append(i)
    print(c)   