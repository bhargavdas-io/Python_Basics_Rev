# A program that takes user input and asks the user to enter two numbers and the program finds the modulus is even or odd

user_name = input("Please enter your name:")
user_age= input("Hi "+user_name +" enter your age:")

num_1 = input("Enter your first number:")
num_2 = 2

mod_calc = (int( num_1 )% num_2)

print(str(mod_calc)," is the modulus")

if mod_calc == 0:
    print("The modulus is even")
else:
    print("The modulus is odd")



