a,b=map(int,input().split())
s=0
m=[]
for i in range(a):
    k=list(map(int,input().split()))
    
    for i in k:
        s+=i
        m.append(s)
print(max(m))