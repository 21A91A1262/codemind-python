n=input()
k=n.lower()
p=set(k)
c=0
for i in p:
    if i!=" ":
        c+=1
print(c)