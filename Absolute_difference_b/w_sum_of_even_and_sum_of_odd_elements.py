n=int(input())
l=list(map(int,input().split()))
s=0
o=0
for i in range(n):
    if(l[i]%2==0):
        s=s+l[i]
    else:
        o=o+l[i]
print(abs(s-o))
