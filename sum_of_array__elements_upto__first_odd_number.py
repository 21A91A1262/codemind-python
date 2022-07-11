n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s+i
    if i%2!=0:
        s=s-i
    
        break
print(s)

        