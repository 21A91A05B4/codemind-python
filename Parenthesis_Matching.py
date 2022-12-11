s=input()
arr=[]
f=1
for i in range(len(s)):
    if s[i] in '({[':
        arr.append(s[i])
        f=1
    else:
        if len(arr)>0:
            if arr[-1]=='(' and s[i]==')':
                arr.pop()
            elif arr[-1]=='{' and s[i]=='}':
                arr.pop()
            elif arr[-1]=='[' and s[i]==']':
                arr.pop()
            else:
                print(i+1)
                f=0
                break
        else:
            print(i+1)
            f=0
            break
if f==1:
    if len(arr)==0:
        print(0)
    else:
        print(len(s)+1)