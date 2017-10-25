# infinite generator for a fibonacci
def fibonacci():
    a, b = 0, 1
    while (1):
        yield a
        a, b = b, a + b


#generator  for a factorial
def factorial(n):
    if n==0:
        yield 1
    else:
        while n>0:
            a=n
            for i in range(1,a):
                a*=i
            yield a
            n-=1

        #yield a

# assigning
a = fibonacci()
b = factorial(5)

# a range provides for only 0 to n-1 in range(0,n)
for i in range(5):
    print (next(a))

print ("factorials")
for i in range(4):
    print (next(b))