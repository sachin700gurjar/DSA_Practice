def fact(n):
    if n==0 or n==1:
        return 1 
    return n *fact(n-1)
a = fact(5)
print(a)

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
b = fib(10)
print(b)

def Nsum(n):
    if n == 1:
        return 1
    else:
        return n+Nsum(n-1)
c = Nsum(5)
print(c)

def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)
print(power(4,3))
