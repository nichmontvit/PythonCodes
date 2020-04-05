def format_address(address_string):
    # Declare variables
    splitString = address_string.split(' ',1)
    houseNumber = splitString[0]
    streetName = splitString[1]
  
    # Return the formatted string  
    return "house number {} on street named {}".format(houseNumber,streetName)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"