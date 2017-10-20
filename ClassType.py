
array = []
array.append(1)
array.append("asdf")
array.append(array)

for a in array:
    print(type(a))
    if "list" in str(type(a)):
        print ("in subclass")
        for b in a:
            print(type(b))

