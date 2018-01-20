#!/usr/bin/env python
# coding: utf-8
def check(guess, tries):
    if guess == word:
        print("Good Job! You are one with the Source.")
        exit(0)
    elif guess == "lol":
        print("You wasted a guess =P")
    elif len(guess) < 5:
        print("0, 1, 2, 3, 4 that’s how we count to five!")
    elif guess[0] != word[0]:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    else:
        print("you have " + str(tries) + " guesses left!")

def main():
    tries = 10
    print("The secret word begins with a " + word[0])
    while tries > 0:
        tries -= 1
        guess = raw_input("GUESS?: ")
        check(guess, tries)
    exit(0)

word = "moist"
main()
