word = input("Give me a word for the other player to guess.\n")
guesses = ''
correctGuesses = ''
turns = 13
import time
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
name = input("What is your name?\n")
print("Hello, " + name, " time to play hangman.\nStart guessing!")
def checkforcharacter(turns, guesses, word, correctGuesses):
    while True:
        if(turns == 0):
            print("You lost. The word was " + word + ".")
            break
        if all(l in correctGuesses for l in word):
            print("You have the entire word! The word was " + word + ".")
            break
        guess = input("Guess a character: ")
        guesses +=guess
        if(guess not in word):
            turns = turns - 1
            print("Sadly that guess is wrong. You guessed '" + guess + "'.")
            print("You have ", + turns, " more guesses.")
            print("Your guesses so far: " + guesses + ".")
            print("So far, the word is: ")
            displayedWord = ""
            correctGuesses +=guess
            for c in word:
                if c in correctGuesses:
                    displayedWord += c
                else:
                    displayedWord += " _ "
            print(displayedWord)
        else:
            print("That guess was correct!")
            print("You have ", + turns, " more guesses.")
            print("Your guesses so far: " + guesses)
            print("So far, the word is: ")
            displayedWord = ""
            correctGuesses +=guess
            for c in word:
                if c in correctGuesses:
                    displayedWord += c
                else:
                    displayedWord += " _ "
            print(displayedWord)
checkforcharacter(turns, guesses, word, correctGuesses)