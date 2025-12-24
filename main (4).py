def factorial(n):
    out=1
    while n>=1:
     out=out*n
     n=n-1
    return out
n=int(input("enter the number:"))
print(factorial(n))