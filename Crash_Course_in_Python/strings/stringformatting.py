name = "Manny"

number = len(name) * 3

print("Hello {}, you lucky number is {}".format(name,number)) # this is the string formatting => it works with any data type

print("Your lucky number is {number}, {name}".format(name=name, number=number))

price = 7.5

with_tax = price * 1.09

print("Base Price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax)) # this rounds the numbers up to 2 decimals

wheather = "Rainfall"

print(wheather[:4])

