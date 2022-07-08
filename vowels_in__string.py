n=input()
k="aeiouAEIOU"
b=[]
for i in n:
    if i in k:
        if i not in b:
            b.append(i)
if len(b)!=0:
    print(*b)
else:
     print(-1)