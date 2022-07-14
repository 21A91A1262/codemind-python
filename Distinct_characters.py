n=input()
k=n.lower()
b=[]
for i in k:
    if k.count(i)==1 and i!=" ":
        b.append(i)
b=sorted(b)
for j in b:
    print(j,end='')
        