class Fruit():
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

# inheritance is useful as it reduces code redundancy
# in python, inheritance is declared by using parantheses in the class declaration
# if a class A inherit from class B, then Class A will have the same constructor as class B
class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("{sound} I'm {name}!  {sound}".format(sound = self.sound, name = self.name))
        
class Piglet(Animal):
    sound = "oink"
    
hamlet = Piglet("Hamlet")
hamlet.speak()