n=int(input())
c=0
while(n>=0):
    a=input()
    c=0
    for i in a:
        if(i.isdigit()):
            c+=1
    if(c==len(a)):
        print('True')
    else:
        print('False')
        
        