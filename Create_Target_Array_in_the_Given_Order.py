n=int(input())
nums=list(map(int,input().split()))
m=int(input())
tar=list(map(int,input().split()))
c=[]
for i in range(len(nums)):
    c.insert(tar[i],nums[i])
print(*c)