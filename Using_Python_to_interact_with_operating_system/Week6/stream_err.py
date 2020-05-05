data = input("this will come from the STDIN: ")
print("now we write it to STDOUT:" + data)
raise ValueError("Now we are generating an error message to STDERR")