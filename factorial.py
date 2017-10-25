'''
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))
'''
import sys

def factorial(n):
  listArr = range(1,n)
  s = iter(listArr)
  while (1):
    try:
      n = n*next(s)
    except:
      return n

try:
  accept_user_input = int(input ("enter number for factorial : "))   
  if (accept_user_input == 0):
    print("1")
  else:
    print(factorial(accept_user_input))
    
except:
  print ("number not entered")
  

  
