def rec (n):
    if n == 0:
        return 0
    return (n+ rec(n-1))

print(rec(5))




# def rec(n, sum):
#     if n<1:
#         print(sum)
#         return

#     rec(n-1, sum+n)

# rec(5,0)
    

