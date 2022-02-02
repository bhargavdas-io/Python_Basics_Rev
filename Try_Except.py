# A try-except block is used to handle errors in python.
# If a user inputs an invalid input, instead of Python throwing out errors, we can handle that error using a try-except block and return a custom message

try:
    #division = 10/0
    number = int(input("Please enter a number: "))
    print(number)
except ZeroDivisionError:                                                     # It is  a good practise to specify which type of error we are trying to except instead of using just *except*, that will except all the types of errors
    print("Division by zero is prohibited")
except ValueError:
    print("Enter a integer value")