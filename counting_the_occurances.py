s=input()
n=input()
c=0
for i in s:
    #if i>='0' and i<='9':
    if i==n:
        #c=c+int(i)
        c+=1
if c==0:
    print(-1)
else:
    print(c)