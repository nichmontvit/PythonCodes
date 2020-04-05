# list comprehension allow us to create a list based on ranges or sequences

# before list comprehension

multiples = []

for x in range(1,11):
    multiples.append(x*7) 

print(multiples)

# with list comprehension
newMultiples = [x * 7 for x in range(1,11)] #this creates a list with elements that are multiples of 7 from 7 to 70

print(newMultiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]

lengths = [len(languages) for language in languages]

print(lengths)

numbers = [x for x in range(1,101) if x % 3 == 0] # this prints the numbers that are divisible by 3 between 1 and 101

print(numbers)

def highlight_word(sentence, word):
    if word in sentence:
        word.upper()
    return(word.upper())

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
