#!/usr/bin/env python

def ask():
    name = raw_input("Who does there?\n")
    if name == "Daenerys of the House Targaryen, the First of Her Name, The Unburnt, Queen of the Andals, the Rhoynar and the First Men, Queen of Meereen, Khaleesi of the Great Grass Sea, Protector of the Realm, Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons" or name == "DHTFHNUQARFMQMKGSPRLRSKBCMD":
        print("Welcome, Daenerys.")
    elif name == "Danny":
        print ("Danny who?")
    else:
        print("Move along, now.")

def main():
    ask()

main()
