#مربع
def square(n):
    for i in range(n):
        for x in range(n-1):
            print('*  ',end='')
        print('*')

n = int(input('enter the length of your square: '))
square(n)



#مثلث قائم الزاویه
def fool(n):
    for i in range(2,n+2):
        for u in range(i-1):
           print('*',end='  ')
        print('')
n = int(input("enter perpendicular triangle's height : "))
fool(n)
 
# مثلث متساوی الاضلاع
def fol(n):
    for i in range(n):
        for x in range(n-i):
            print(" ",end='')
        for y in range(2*i):
            print('*',end='')
        print('*')
n = int(input('enter the height(1): '))
fol(n)

# مثلث متساوی الاضلاع برعکس
def lof(n):
    for i in range(n):
        for x in range(i+1):
            print(' ',end='')
        for y in range(2*(n-i-1)):
            print('*',end='')
        print('*')
n = int(input('enter your height: '))
lof(n)

# لوزی
N = int(input('enter your height: '))
fol(n)
for i in range(2*n):
    print('*',end='')
print('*')
lof(n)

x= int(input())
for i in range(x):
    for y in range(x-i-1):
        print(' ',end='')
    for c in range(i):
        print('* ',end='')
    print('*')
p = x -1
for i in range(p):
    for u in range(i+1):
        print(' ',end='')
    for v in range(p-i-1):
        print('*',end=" ")
    print('*')

n = int(input())
for i in range(n):
    for i in range(n-i-1):
        print(' ',end='')
    for i in range(n-1):
        print('* ',end='')
    print('*')