# this code converts a string into piglatin

def pig_latin(sentence):
    result = ""
    for word in sentence.split():
        result += word[1:] + word[0] + "ay "
    return result	
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay