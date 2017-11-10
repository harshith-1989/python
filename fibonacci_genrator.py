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
            yield ("!{} = {}".format(i+1,a))
            n-=1

def get_integer_input() -> int:
    number = input("Please enter a number : ")
    try:
        return int(number)
    except:
        print("please enter a valid number. Aborting")
        exit(1)


# assigning

range_expected = get_integer_input()

a = fibonacci()
b = factorial(range_expected)

# a range provides for only 0 to n-1 in range(0,n)
print ('generating the fibonacci sequence for the specified range...')
for i in range(range_expected):
    print (next(a))

print ('generating the factorials for the numbers in the specified range...')
for i in range(range_expected-1):
    print (next(b))