# regualar expression is a search query that allow us to find a specific portion of a text on the basis of a defined pattern

# this script retrieves the process ID of the error log  
log = "July 31 07:51:48 my computer bad_process[123456]: ERROR Performing package upgrade" 
index = log.index("[")
print(log[index+1:index+6])

# this optimized script retrieves the process ID of the error log no matter how big or small the process ID is 
# NOTE: the script will work as long as we have a single sequence of numbers in the string marked by a square bracket
import re
log2 = "July 31 07:51:48 my computer bad_process[123456]: ERROR Performing package upgrade" 
regex = r"\[(\d+)\]"
result = re.search(regex,log2)
print(result[1])

# this command displays a list of all the words in the words file that have the term thon in them
# grep thon /usr/share/dict/words

log3 = "this is a test"
regex1 = r"thos"
result1 = re.search(regex1, log3)
print(result1)

# this command displays a list of all the words in the words file that have the term thon in them regardless of the query was 
# done with uppercase or lowercase letter
# grep -i thon /usr/share/dict/words

# this gives the words tha start with the term fruit
# grep ^fruit /usr/share/dict/words

# this gives the words that finishes with the term cat
# grep cat$ /usr/share/dict/words

# this returns a list of all matches for a predefined regular expression pattern
# re.findall()

# this command checks whehter the particle aza is contained in the word plaza,if it does, python returns a match object 
# with a span and the matching particle otherwise python returns a None value
print(re.search(r"aza","plaza"))

print(re.search(r"p.ng", "penguin"))

# this command checks wether the word penguin starts with the particle "peng", if it does, python returns a match object with a span and the 
# matching particle otherwise python returns a None value
print(re.search(r"^peng", "penguin"))

# this command checks wether the word penguin ends with the particle 'in', if it does, python returns a match object with a span and the 
# matching particle otherwise python returns a None value
print(re.search(r"in$", "penguin"))

# this command checks wether penguin starts with peng, if it does, python returns a match object with a span and the 
# matching particle otherwise python returns a None value. This commands is canse INSENSITIVE i.e. the user can use both 
# lowercase and uppercase when doing the query
print(re.search(r"in$", "penguin", re.IGNORECASE))

# this checks if the word Argentina begins and ends with the letter a
print(re.search(r"^A.*a$", "Argentina"))

print(re.search(r"^A.*a$", "Azerbajan"))

# the pattern variable checks if the created variable name is a valid. If it is, then the whole string is returned
# otherwise, python returns None as value

# the variable can start with a letter or an underscore so the regular expression starts with an ^ to indicate that we want to 
# start from the beginning

# the first character class will include all lowercase and uppercase letters plus an underscore [a-zA-Z_]

# the second character class, which represents the rest of the variable, will include all the numbers, underscores and letters 
# we add the * and the $ character to indicate we want to have the whole string 
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))

print(re.search(pattern, "2this_is_a_valid_variable_name"))

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))

print(extract_pid("99 elephants in a room"))