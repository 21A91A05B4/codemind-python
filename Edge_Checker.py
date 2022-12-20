a,b=map(int,input().split())
if a>0 and b>0:
    if b==a+1 or b==a-1 or b==10 and a==1 or b==1 and a==10:
        print("Yes")
    else:
        print("No")