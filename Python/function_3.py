def add_(a, b, c=None, flag=False):
    if(flag):
        print("Flag is true")
    if(c==None):
        return a+b
    else:
        return a+b+c
print(add_(1, 2, flag=True))
print("first part finished")
print(add_(1, 2, c=None))
print("2nd part finished")
print(add_(1, 2, 3, flag=True))
print("3rd part finished")
