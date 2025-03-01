n = int(input(()))
l = []
for i in range(n) :
    p = int(input())
    l.append(p)
x = 0 
for i in range(len(l)):
    if x < l[i] :
        x = l[i]
print(x)
