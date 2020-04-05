message = "this kine has a typo"

# message[5] = "l" executing this line leads to an error as strings are immutable in python

print(message)

# this will grab the first 4 characters of the message variable, add the letter l and then add the rest of the content of the message variable
new_message = message[:5] + "l" + message[6:] 

print(new_message)

message2 = "this is a message "

print(message2)

# message2 = "and this is another message" executing this code will overwrite the content of the message2 variable instead of adding it 

message2 += "this is another message" # this will concatenate the "this is another message" text to the content of the message2 variable

print(message2)

pets = "Cats & Dogs"

pets.index("&") # this will give the index of the specified element, i.e. its location in the string

list1 = [["Cats", "Worms"], ["Dogs", "Insects"]]

print(list1[0])

# this checks if the dragons element is in the pets list, if it is, the code returns True, otherwise it returns False
print("Dragons" in pets) 

print("Mountains".upper()) # this turns all the letter of the word mountains into capital letters

print("Mountains".lower()) # this turns all the letter of the word mountains into small letters

print(" yes ".strip()) # this removes all the white spaces in the string

print("the word e has appeared many times over".count("e")) # this returns how many times the letter e appears on the string

# this returns True if the string Forest ends with the substring rest, otherwise it returns False
print("Forest".endswith("rest"))

print("Forest".isnumeric()) # this returns True if the string is composed of ONLY number, otherwise it returns False

print(" ".join(["this", "is", "a", "phrase", "joined", "by", "spaces"]))

print("This is an example".split()) #this splits a string into a list of substrings  
