########################################################################
# Lists Beginner
########################################################################



########################################################################
# Lists Intermediate
########################################################################

my_palindrome = [1,2,3,4,3,2,1]
my_palindrome2 = ["h", "a", "n", "n", "a", "h"]
my_palindrome3 = [1,2,3,3,2,1]
my_palindrome4 = [1,2,4,3,2,1]
my_palindrome5 = ["h", "a", "n", "n", "a"]
my_palindrome6 = [1,2,3,4,3,2,2]

my_list_palindrome = [my_palindrome, my_palindrome2, my_palindrome3, my_palindrome4, my_palindrome5, my_palindrome6]

is_palindrome = True

for palindrome_test in my_list_palindrome:

    for index, num in enumerate(palindrome_test):
        compare_index = len(palindrome_test) - index - 1
        print(num, palindrome_test[compare_index])
        if num != palindrome_test[compare_index]:
            is_palindrome = False


    if is_palindrome == True:
        for data in palindrome_test:
            print(data, end="")
        print(f" is a palindrome")
    else:
        for data in palindrome_test:
            print(data, end="")
        print(" is not a palindrome")

########################################################################
# Lists Advanced
########################################################################
# username = []
# password = []
# email = []
# username = ""

# while username != "quit":
#     username = input("Username: ")
#     if username != "quit":
#         password = input("Password: ")
#         email = input("Email Address: ")

#         username.append(username)
#         password.append(password)
#         email.append(email)


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
    # This is a little weird, I compare i from myList with the 
    # string version to determine if it is a number
    if i != str(i):
        total += i
print(total)


# len on myList (error list is not an integer)
# needs and if statement to prevent the code from: "IndexError: list index out of range"

myList = [0,1,2,3,4,5,6,7,8,9,10]

for x in range(0, len(myList), 2): #Remove len for assignment
    if x < 10: #Remove this for assingment
        print(myList[x + 1])





# print the odd numbers from a list w/errors
x = 0
myList = [0,1,2,3,4,5,6,7,8,9,10]

for x in range(0, myList, 2):
        print(myList[x + 1])