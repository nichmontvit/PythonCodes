#!/usr/bin/env python3
# we can take information from user input by using the input method

def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

print("Welcome to the time converter")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the amount of hours: "))
    minutes = int(input("Enter the amount of minutes: "))
    seconds = int(input("Enter the amount of seconds: "))
    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [press y to continue]")

print("Goodbye!")
