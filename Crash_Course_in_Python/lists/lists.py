x = ["Now", "we", "are", "cooking"]

print(x)  # this gives you the contents of the list

print(len(x))  # this gives the number of elements inside of the list

print("are" in x) # this returns true if the word are is present in the x list otherwise it returns false

# list indexing

print(x[0]) # this returns the first element of the x list

print(x[-1]) # this returns the last element of the x list

# this displays the first 3 elements of the list; 
# IMPORTANT NOTE: the command will INCLUDE the FIRST element while EXCLUDING the SECOND Element
print(x[0:3])

print(x[:2]) # this will display every element of the x list UP TO the third element

print(x[1:]) # this will display every element of the x list STARTING from the FIRST element onwards

Fruits = ["Pineapple", "Apple", "orange", "Melon"]

Fruits.append("Kiwi")  # this adds the word kiwi at the END of the Fruits list

print(Fruits)

# the insert function takes 2 arguments: the index and the name of the element to be added to the list
# using an index that is higher than the length of the list will result in the element being added at the end of the list
# this adds the word watermelon as the FIRST element.
Fruits.insert(0, "Watermelon")

print(Fruits)

Fruits.insert(25, "Strawberry")

print(Fruits)

# this removes the element melon from the Fruits list
Fruits.remove("Melon")

# this shows which element was removed from the list
print(Fruits.pop(3))


print(Fruits)

# this changes the first element of the fruits element
Fruits[0] = "Vegetables"

print(Fruits)

# list iteration
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]

chars = 0

for animal in animals:
    chars += len(animal)

print("Total Characters: {chars}, Average characters: {avg_chars}".format(avg_chars = chars/len(animals), chars = chars))

winners = ["Ashley", "Dylan", "Reese"]

# the enumerate function returns a tuple for each element in the list: the first value is the index of the element in the list
# while the seconds value is the element in the list
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
    
names = ["Terry", "Cherry", "Crystal"]

names.reverse()

print(names)

