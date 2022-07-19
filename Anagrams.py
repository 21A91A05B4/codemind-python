s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
f=0
for i in s1:
    if i not in s2:
        f=1
        break
if f==0:
    print('True')
else:
    print('False')
        