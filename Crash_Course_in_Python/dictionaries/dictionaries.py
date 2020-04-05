import re
# a dictionary is a data type that allow us to organize elements into collections
# unlike lists, one cannot access an element inside of a dictionary by using its position
# one must instead use what we call its "key" and "values"

# additionaly, the index of a list must be a number while in a dictionary, several data type can be used as keys

# one can define a dictionary by using the curly braces
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py":23}
print(file_counts)

# this gives the value associated with the txt key
# dictionary values can be accessed by referencing the key with which the value is associated
print(file_counts["txt"])

# this returns true if the jpg key is in the file counts dictionary, otherwise it returns false
print("jpg" in file_counts) 

# this adds the cfg key to the file_counts dictionary and associtates the number 8 with it
file_counts["cfg"] = 8 

print(file_counts)

# this removes the cfg key from the file_counts dictionary
del file_counts["cfg"]

print(file_counts)

# dictionary iteration

# NOTE: this will ONLY return the KEYS of the created dictionary not the values associeated with the keys
for extension in file_counts:
    print(extension)
 
# This displays the values of a dictionary
print(file_counts.values())

# this displays the key of a dictionary
print(file_counts.keys())

# this displays both keys and their respective values
print(file_counts.items())

for ext, amount in file_counts.items():
    print("there are {} files with the {} extension".format(amount, ext))
    
# use dictionaries when you plan on searching for a specific element

# dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.

# dict.clear() - Removes all the items of the dictionary

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())