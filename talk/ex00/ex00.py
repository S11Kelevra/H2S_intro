#!/usr/bin/env python

def ask():
    name = raw_input("Hello Hacker, what is your name?\n")
    return(name)

def welcome(name):
    print("Welcome, " + name + ".")

def main():
    name = ask()
    welcome(name)

main()
