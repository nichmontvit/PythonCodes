import re 

# this command will match any character repeated as many times as possible
print(re.search(r"Py.*n", "Pygmalion"))

# this will match the word "python programming up to the last character"
print(re.search(r"Py.*n", "Python Programming"))

print(re.search(r"Py[a-z]", "Python Programming"))

# the plus character matches one or more occurences of the character that comes before it 
# this will return a whole string that matches the specified condition
print(re.search(r"o+l", "Woolly"))

# NOTE: if there is a character between the o and the l, python will return None as value as it won't match the search pattern
print(re.search(r"o+l", "Boil"))

# the ? symbol means either zero or one occurence before it 
# this command will display the word "each"
# the word "each" does not have the letter p but the question mark symbol marks the letter p as optional so we are still 
# getting a match
print(re.search(r"P?each", "To each their own"))

# in this case, the letter p is present in the word "peaches" so the letter p will appear in the result
print(re.search(r"p?each", "I love peaches"))

# this command matches any word that contains AT LEAST 5 letters. 
print(re.search(r"[a-zA-Z]{5}", "ghost"))

# if we have 2 or more words that contain 5 characters, then the command will only return the first word
print(re.search(r"[a-zA-Z]{5}", "a scary ghost has appeared"))

# this returns all the words that have AT LEAST 5 characters 
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost has appeared"))

# this returns all the words that have EXACTLY 5 characters 
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost has appeared"))

print(re.findall(r"\w{5,10}", "I really liked Strawberries"))

# this returns all the words that have AT LEAST 5 characters 
print(re.findall(r"\w{5,}", "I really liked Strawberries"))


print(re.search(r"s\w{,20}", "I really liked strawberries"))



