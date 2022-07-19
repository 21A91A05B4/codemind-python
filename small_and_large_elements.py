s1=input()
d=[]
for i in s1.split():
        d.append(i)
print(min(d[0]),max(d[-1]),end=' ')