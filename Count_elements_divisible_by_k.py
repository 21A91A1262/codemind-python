n,k=map(int,input().split())
b=list(map(int,input().split()))
c=0
for i in range(len(b)):
    if b[i]%k==0:
        c+=1
print(c)
