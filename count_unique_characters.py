n=input()
k=n.lower()
c=0
for i in k:
    if i!=" ":
        if n.count(i)==1:
            c+=1
            
print(c)
    