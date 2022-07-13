n=input()
b=['a','e','i','o','u']
c=[]
for i in b:
    if i not in n:
        c.append(i)
if len(c)!=0:
    print(*c)
else:
    print("0")