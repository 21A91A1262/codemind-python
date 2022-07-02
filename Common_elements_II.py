n,m=map(int,input().split())
a=list(map(int,input().split()[:n]))
b=list(map(int,input().split()[:m]))
y=[]
for i in a:
    if i not in b:
        y.append(i)
for i in b:
    if i  not in a:
        y.append(i)
print(*y)