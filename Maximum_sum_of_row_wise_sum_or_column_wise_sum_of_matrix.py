a,b=map(int,input().split())
m=[]
for i in range(a):
    k=list(map(int,input().split()))
    s=0
    for i in k:
        s+=i
    m.append(s)
print(max(m))