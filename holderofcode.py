# FIRST: Prompt user for grade: assign value to number
number = input("enter the percent grade:  ")
.75

#you need to initalize a message, okay maybe not need but it's good practice
message = "not run"

#whenever you print ANYTHING i suppose it converts it to a string; ALSO, simply doing a statement like Float(blank) DOESN'T modify original value
number = float(number)

#decision tree: the important part is the fact that ranges will contain an upper and lower bound
if (number > 1.0):
    message = "number larger than 1; smaller num; not valid grade"
elif (number > .90 and number <= 1.0):
    message = "A"
elif (number > .80 and number <= .90):
    message = "B"
elif (number > .70 and number <= .80):
    message = "C"
elif (number > .60 and number <= .70):
    message = "D"
elif (number > .00 and number <= .60):
    message = "E"
elif (number < 0):
    message = "Enter at least 0"
else:
    message = "I don't understandd"

#spit out the result.
print(message)


#how ranged is it?
number = 15
message = "current Null"

if (number > 30):
    message = "enter a smaller number"
elif (number > 20 and number < 30):
    message = "number is between 20 and 30"
else:
    message = "number smaller than 20"

print(message)
