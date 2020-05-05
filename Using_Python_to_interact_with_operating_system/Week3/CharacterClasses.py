import re

# this matches the Python word with both uppercase and lowercase P
print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z ]way", "The end of the highway."))

# this will match the first space of the string
# the ^ symbol are used to match characters that are not in a group i.e. characters that we do NOT want to match
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces"))

# this will only match the dog particle in the string
print(re.search(r"cat|dog", "I like both cat and dogs"))

# this will return all the possible matches specified by the pattern
print(re.findall(r"cat|dog", "I like both cat and dogs"))