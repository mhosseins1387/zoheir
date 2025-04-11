# operations
ops = ['+','-','x','/']
def sum(a,b):
    return int(a) + int(b)
def sub(a,b):
    return int(a) - int(b)
def mult(a,b):
    return int(a ) * int(b)
def div(a,b):
    return int(a) / int(b)
def correct(op,a,b):
    if op not in ops:
        return False
    else:
        return True 
    try:
        int(a,b)
        return True
    except ValueError:
        return False
# loop
while True:
    op = input('witch operation are you going to use (+,-,x,/)?')
    a = input('first number:')
    b = input('second number:')
    x = correct(op,a,b)
    if x == False:
        print('something went wrong. please try again...')
    else :
        if op == ops[0]:
            print(sum(a,b))
        if op == ops[1]:
            print(sub(a,b))
        if op == ops[2]:
            print(mult(a,b))
        if op == ops[3]:
            print(div(a,b))

    