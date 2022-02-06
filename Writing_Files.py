#test_file = open("test_file.txt", "a")
#print(test_file.write("This is the text that got appended"))
#print(test_file.write("\nThis is how to append text in a new line"))


#We can create a new file in python itself:

file_create = open("File_Creation.txt", "w")
file_create.write("This is a new file created in python itself")
print(file_create.read())

