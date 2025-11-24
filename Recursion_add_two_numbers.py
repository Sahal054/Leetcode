def add(a,b):
    if b == 0:
        return a
    if b>0:
        return add(a+1,b-1)

print(add(1,4))