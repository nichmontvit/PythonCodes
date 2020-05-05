import re

# this will display the . character => this can be used to escape any special character 
print(re.search(r"\.", "Mydomain.com"))

# the w special character will match letters, numbers and underscores

# in this example, python will match the first four letter until the space because spaces are not considered as a special 
# character
print(re.search(r"\w*", "This is an example"))

# # in this example, python will match the whole string because every word in the string is separated by an underscore 
# which is matched by the w special character
print(re.search(r"\w*", "This_is_an_example"))

# \d is used for matching digits, \s is used for matching whitespace characters like space, tabs and \b is for word boundaries

