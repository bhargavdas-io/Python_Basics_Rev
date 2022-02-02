# A basic translation program, that takes a user input phrase and replaces the volwels in the phrase with g

def translation(phrase):
    translate = " "
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translate = translate + "G"
            else:
                translate = translate + "g"
        else:
            translate = translate + letter
    return translate


print(translation(input("Please enter a phrase to be translated: ")))
