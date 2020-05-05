# Capturing groups are portions of the pattern that are enclosed in parantheses

import re

# if given a list, this command displays every person's full name if it matches the "result" regular expression pattern
# otherwise the command displays None as value
result = re.search(r"^(\w*), (\w*)", "Lovelace, Ada")
print(result)

# this will return a tuple cointaining the 2 elements matched by the pattern
print(result.groups())

# the first element of the result contains the text matched by the entire regular expression
print(result[0])

# the second element of the result contains only the first name matched by the entire regular expression
print(result[1])

# the third element of the result contains only the last name matched by the entire regular expression
print(result[2])

print("{} {}".format(result[2], result[1]))

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return result
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada M."))    

