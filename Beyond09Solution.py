########################################################################
# Lists Beginner
########################################################################



########################################################################
# Lists Intermediate
########################################################################




########################################################################
# Lists Advanced
########################################################################
user_information = []
username = ""

while username != "quit":
    username = input("Username: ")
    if username != "quit":
        password = input("Password: ")
        email = input("Email Address: ")

        user_information.append(username)
        user_information.append(password)
        user_information.append(email)

print(user_information)
# Change data in list 


########################################################################
# DEBUG
########################################################################

#Errors
# i is not being used in the if statement
# total shouldn't be a list

# Don't change list
########################################################################
myList = [1, "A", "b", 3, "THREE", "myString", 4]
########################################################################

total = 0
for i in myList:
    if i != str(i):
        total += i
print(total)


# len on myList (error list is not an integer)
# needs and if statement to prevent the code from: "IndexError: list index out of range"

myList = [0,1,2,3,4,5,6,7,8,9,10]

for x in range(0, len(myList), 2):
    if x < 10: #Remove this for assingment
        print(myList[x + 1])





# print the odd numbers from a list w/errors
x = 0
myList = [0,1,2,3,4,5,6,7,8,9,10]

for x in range(0, myList, 2):
        print(myList[x + 1])