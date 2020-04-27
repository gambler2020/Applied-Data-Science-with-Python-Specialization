def add_(a, b, c=None):
    if(c==None):
        return a+b
    else:
        return a+b+c
print(add_(1, 3))
print(add_(1, 3, 5))
