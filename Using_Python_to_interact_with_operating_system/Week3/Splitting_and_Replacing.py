import re

# when working with regular expressions, the split function allows us to take a regular expression as a separator instead of 
# just a string 
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

# this includes the elements used to split the string in the result
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

# the sub command is used to create new strings by substitution all of part of them for a different string 
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nutz95@my.example.com"))

# the \2 represents the second capturing group while the \1 represents the first capturing group
print(re.sub(r"^([\w .-]*), ([\w .-]*)$" , r"\2 \1", "Lovelace Ace"))