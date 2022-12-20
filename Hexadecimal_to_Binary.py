n=int(input())
for _ in range(n):
    s=input()
    r=bin(int(s,16))
    r=r[2:]
    if (len(r)%4==0):
        print(r)
    elif len(r)%4==1:
        print('000'+r)
    elif len(r)%4==2:
        print('00'+r)
    else:
        print('0'+r)