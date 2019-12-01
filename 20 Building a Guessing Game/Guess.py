
secret_word = "giraffe"
guess = ""
number_of_guesses = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_limit > number_of_guesses:
        guess = input("Enter a guess: ")
        number_of_guesses += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out if guesses. You Lose!")
else:
    print("Correct word. You Win!")