n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
s=0
for i in a:
    if(i<x or i>y):
        b.append(i)
print(sum(b))

    