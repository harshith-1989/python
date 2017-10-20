number = input("Please enter a number : ")
try:
    number = int(number)
except:
    print ("please enter a valid number. Aborting")
    exit(1)

for a in range(number-10, number+10):
    if number>a :
        print ("{} is greater than {}".format(number,a))
    elif number==a :
        print ("{} is equal to {}".format(number,a))
    else:
        print ("{} is lesser than {}".format(number,a))

