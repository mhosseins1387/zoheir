n = int(input())
list = []
x = 1
for i in range(1,n+1):
    list.append(i)
for i in range(len(list)):
    x = x*list[i]
print(x) 
