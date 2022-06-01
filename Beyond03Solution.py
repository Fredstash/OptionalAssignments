########################################################################
# Operators Beginner
########################################################################

    # Beginner Question 1
    # Get two numbers from the user and print the sum
    # make sure you get the right kind of data by
    # using float(input()) or float(variable)

y = float(input("What is the first number: "))
z = float(input("What is the second number: "))

x = y + z

print(f"{x} is the sum of {y} and {z}")

########################################################################
# Operators Intermediate
########################################################################

    # Intermediate Question 1
    # Ask user for the gas price (float), how many gallons they bought(float), 
    # how many gallons they have(float) and aproximate gas mileage (int)
    # display how much money they spent, and how far they can travel.
    # travel distance = total gallons of gas * gas mileage

gas_price = float(input("What is the gas price: "))
gallons_purchased = float(input("How many gallons of gas did you purchase: "))
current_gallons = float(input("How many gallons do you have currently: "))
gas_mileage = int(input("What is your gas mileage to the closest mile: "))

amount_spent = gas_price * gallons_purchased
distance_can_travel = (gallons_purchased + current_gallons) * gas_mileage

print(f"Amount you spent: {amount_spent:.2f}")
print(f"distance you can travel: {distance_can_travel:.2f}")

########################################################################
# Operators Advanced check WEEK 07 for how to make for loops
########################################################################

    # Advanced Question 1
    # Use a for loop to calculate any factorial
    # factorial:
    # 10! == 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 == 3628800
    ####################################################################

fact = 1
user_num = int(input("What integer would you like the factorial of: "))

for i in range(1, user_num + 1):
    fact *= i

print(f"The factorial of {user_num} is {fact}")



#################################################################
# DEBUG: Fix the code
#################################################################

    # DEBUG Question 1 
    # There are 3 errors
    # Expected output: My number is: 10
    ################################

num1 = "4"
num2 = "6"
Print(f"My number is: {num1 + num2}")


#################################################################
# DEBUG: Fix the code
#################################################################

    # DEBUG Question 1 
    # There are 3 errors
    # Expected output: My number is: 10
    ################################
    
#Solution#
# The numbers were being stored as strings,
# so this means that the + put the two strings
# together instead of adding the numbers
num1 = 4
num2 = 6

# print should not be capitalized
print(f"My number is: {num1 + num2}")