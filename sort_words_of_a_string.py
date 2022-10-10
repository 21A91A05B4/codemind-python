s=input().split()
for i in s:
    b=[]
    for j in i:
        if j.isalpha():
            b.append(j)
    b.sort()
    c=0
    for k in range(len(i)):
        if i[k].isalpha():
            print(b[c],end='')
            c+=1
        else:
            print(i[k],end='')
    print(end=' ')
        
    
            