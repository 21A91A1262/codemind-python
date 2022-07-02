n=int(input())
l=list(map(int,input().split()))

for i in range(n):
    s=0
    if(l[i]==0):
        s+=1
    if(l[i]<0):
        l[i]=l[i]*-1
    
    while(l[i]>0):
        r=l[i]%10
        s+=1
        l[i]=l[i]//10
    print(s,end=" ")
