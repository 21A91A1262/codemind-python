n,m=map(int,input().split())
a=list(map(int,input().split()[:n]))
b=list(map(int,input().split()[:m]))
x=set(a)
k=set(b)
y=[]
for i in x:
    if i in k:
        y.append(i)
print(len(y))
