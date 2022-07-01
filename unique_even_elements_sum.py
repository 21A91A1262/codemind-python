n=int(input())
m=list(map(int,input().split()))
k=set(m)
s=0
for i in  k:
    if(i%2==0):
        s=s+i
print(s)