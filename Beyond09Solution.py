########################################################################
# Loops Beginner
########################################################################



########################################################################
# Loops Intermediate
########################################################################



########################################################################
# Loops Advanced
########################################################################



########################################################################
# DEBUG
########################################################################

#Errors
# i is not being used in the if statement
# total shouldn't be a list


myList = [1, "A", "b", 3, "THREE", "myString", 4]

total = 0
for i in myList:
    if i != str(i):
        total += i
print(total)