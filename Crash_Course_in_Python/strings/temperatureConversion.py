def to_Celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    # the {:>3} means that we want the numbers to be aligned to the 
    # right at 3 spaces
    # the {:>6.2f} means that we want the numbers to be rounded at 
    # 2 decimals and we want the numbers to be aligned to the right 
    # at 6 spaces
    print("{:>3} F | {:>6.2f} C".format(x, to_Celsius(x)))
    
list1 = [["Cats", "Worms"], ["Dogs", "Insects"]]
print(list1[1].index("Insects"))
