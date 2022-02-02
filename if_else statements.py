#  A program with if - else statement with or and and operator


is_male = True # A boolean variable
is_tall  = False
is_educated = False

def test():
    if is_male and is_educated:
        print("Bhargav")
    elif is_male and is_tall:
        print("You are tall and a male")
    #elif is_male:
        #print("You are a male")
    elif not(is_educated) and is_male:      # Using not operator
        print("You are not educated but is a male")

test()


