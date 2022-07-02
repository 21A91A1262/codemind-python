n=int(input())
l=list(map(int,input().split()))
s=0
l1=l[:]
l1.sort(reverse=True)

if(l==l1):
    s=1
if(s):
    print("yes")
else:
    print("no")
    