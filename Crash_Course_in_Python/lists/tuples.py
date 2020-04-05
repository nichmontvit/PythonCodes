# tuples are lists in which one cannot change its elements
# one can define a tuple by using paranthese
x = ("this is a tuple")

print(x)


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


print(type(convert_seconds(9000)))

# one can unpack a tuple i.e. we turn a tuple of 3 elements into 3 separate variables
# when working with tuples, the order in which elements appear in the tuple matter since they don't change
hours, minutes, seconds = convert_seconds(9000)

print(hours, minutes, seconds)

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0

for animal in animals:
    chars += len(animal)

print("Total Characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]

# the enumerate function returns a tuple for each element in the list: the first value is the index of the element in the list
# while the seconds value is the element in the list
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


tuples = (1,2,3,4,5)

print(tuples) 

print(tuples[0])   
