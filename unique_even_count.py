n=int(input())
m=list(map(int,input().split()))
s=set(m)
c=0
for i in s  :
    if(i==0):
        continue
    if(i%2==0):
        c+=1
print(c)