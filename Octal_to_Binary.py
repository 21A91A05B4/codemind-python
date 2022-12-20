n=int(input())
for _ in range(n):
    k=(input())
    b=int(k,8)
    b=bin(b)
    print(b[2:])