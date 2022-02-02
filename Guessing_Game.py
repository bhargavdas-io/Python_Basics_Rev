# A game that asks the user for input and until the user guesses the name of the animal, The program will keep on asking the user to input and try again

word  = "Cat"
guess_word = " " # Empty string
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess_word != word and not(out_of_guess):
    if guess_count<guess_limit:
        guess_word = input("Enter the secret animal name: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("No more guesses left")
else:
    print("You Win")
