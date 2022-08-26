s=input()
s=s.split()
a=[]
b=[]
for i in range(len(s)):
    b.append(s[i])
    break
for i in (s[::-1]):
    a.append(i)
    break
l=''
x=''
for i in b:
    l=i
for i in a:
    x=i
a=[]
b=[]
for i in range(len(l)):
    b.append(ord(l[i]))
for i in range(len(x)):
    a.append(ord(x[i]))
print(chr(min(b)),end=' ')
print(chr(max(a)))