class Apple:
    # we define the attributes of the apple class and assign an empty string to each one of them
    color = ""
    flavor = ""

# we can create an instance of a class by calling the name of the class and assigning it to a variable 
# which acts as the instance of the class
jonagold = Apple()

# we set the values for the color and flavor attributes
jonagold.color = "red"
jonagold.flavor = "sweet"

print("the color of the apple is {} and it is {}".format(jonagold.color, jonagold.flavor))


class Piglet:
    # the self parameter represents the instance that the method is being executed on 
    def speak(self):
        print("oink oink")

pig = Piglet()
pig.speak()

class Piglet2:
    name = "Piglet"
    # functions defined inside of a class are called methods
    def speak(self):
        print("oink! i'm {} oink!".format(self.name))
        
hamlet = Piglet2()
hamlet.name = "Hamlet"
# this line calls the method speak defined inside the Piglet2 class

class Piglet3:
    years = 0
    def pig_years(self):
        # difference betwwen return and print functions is that the print function prints a speficied message in the terminal
        # return function returns a specified value but does NOT display it in the terminal
        print(self.years * 18)
        # return self.years * 18

pig = Piglet3()
pig.years = 5

# use the print statement to display the content of the years variable if the variable was returned using the return statement
# otherwise just call the function
pig.pig_years()
# print(pig.pig_years())

class Orange:
    # the __init__ method is called a constructor
    # a constructor of a class is the method called when you call the name of the class
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
    # Simply running "print(test)" will display the location of the object in the computer's memory which is the default respresentation
    # to remedy this setback; we use the __str__ method 
    # The __str__ special method allows us to define how an instance of an object will be printed when it’s passed to the print() function
    def __str__(self):
        return "this orange is {} and its flavor is {}".format(self.color, self.flavor)
        
test = Orange("orange", "sweet")
print(test.color)

test1 = Orange("orange", "bitter")
print(test1)

# this gives us all the defined methods of the orange class
help(Orange)

def to_seconds(hours, minutes, seconds):
    # this is a docstring which allows us to give the user information about the purpose of the defined function
    """Returns the amount in seconds in the given hours, minutes and seconds"""
    return hours * 3600 + minutes * 60 + seconds

help(to_seconds)