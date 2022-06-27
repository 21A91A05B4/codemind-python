s=input()
c=input()
#c='aeiou'
b=[]
m=0
for i in range(len(s)):
    if s[i]== c:
        print('True')
        print(i)
        break
else:
    print('False')