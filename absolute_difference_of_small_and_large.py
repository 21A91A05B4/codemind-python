s=input()
s=s.split()
b=[]
l=''
a=[]
for i in range(len(s)):
    b.append(s[i])
for i in range(len(b)):
    l=b[i]
    for k in range(len(l)):
        a.append(ord(l[k]))
    m=min(a)
    n=max(a)
    print(n-m,end=' ')
    l=''
    a=[]
    i+=1
    
        
    
    
    
    
    
    
    
    