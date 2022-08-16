import random

secretnumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.\nTake a guess. You can use up to 6.\n")
for guessestaken in range(1, 7):
    guess = int(input())

    if int(guess) < secretnumber:
        print("Your guess is too low.")
    elif int(guess) > secretnumber:
        print("Your guess is too high.")
    else:
        break

if int(guess) == secretnumber:
    if guessestaken == 1:
        print("Good job! You guessed my number with just 1 guess!")
    else:
        print("Good job! You guessed my number in", guessestaken, "guesses!")
else:
    print("Nope. The secret number I was thinking of was " + str(secretnumber) + ".")
    
