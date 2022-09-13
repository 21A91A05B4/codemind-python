s=input()
min=9999
minord=9999
maxord=0
max=0
for i in s:
    if i==' ':
        continue
    else:
        if(ord(i)<minord):
            min=s.count(i)
            minsumord=ord(i)*s.count(i)
            minord=ord(i)
            d=i
print(d,min,end=' ')
for i in s:
    if i==' ':
       continue
    else:
       if(ord(i)>maxord):
           maxordsum=ord(i)*s.count(i)
           maxord=ord(i)
           max=s.count(i)
           x=i
#print(s)
print(x,max)          
           
