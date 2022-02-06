# r: means read only    w: means write only    r+: means read + write and   a: means append (using this we can only append information to the already existing file.


test_file = open("test_file.txt", "r+")
#print(test_file.readable())
#print(test_file.read())
#print(test_file.readline())



for employee in test_file.readlines():
    print(employee)

test_file.close()   # It's a good practise to always close a file after being opened