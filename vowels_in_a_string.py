n=input()
c=input()
a="aeiouAEIOU"
for i in n:
    if c in n:
        print(True)
        print(n.index(c))
        break
else:
    print("False")