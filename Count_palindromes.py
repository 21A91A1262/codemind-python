n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    a=i
    s=0
    while(a>0):
        r=a%10
        s=s*10+r
        a//=10
    if(i==s):
        c+=1
print(c)
