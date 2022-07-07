n = input()
c = 0
for i in range (len(n)):
    for j in range(len(n)):
        if (n[i]==n[j]) and i!=j:
            c = c + 1
if c>=1:
    print(False)
else:
    print(True)