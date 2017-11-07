
def return_filehandle_for_reading (fileName):
    return open(fileName,'r',-1,"utf-8")

def return_filehandle_for_writing (fileName):
    return open(fileName,'w')

def return_filehandle_for_read_and_write (fileName):
    return open(fileName,'w+')

fopen = return_filehandle_for_reading("/Users/harshith/PycharmProjects/python/regex_patterns.txt")
print (fopen.readlines())
