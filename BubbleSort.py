count = 0
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return (a,b)

def bubble_sort(array):
    swap_happened = False
    global count
    for i in range(0,len(array)-1):
        if array[i] > array[i+1]:
            array[i],array[i+1] = swap(array[i],array[i+1])
            swap_happened = True
    if swap_happened:
        count+=1
        bubble_sort(array)
    else:
        print("{} sorted in {} tries".format(array, count))

bubble_sort([1,2,3,5,4])