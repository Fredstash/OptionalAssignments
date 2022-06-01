#################################################################
# Print Information and Variable Beginner
#################################################################

    # Beginner Question 1
    # Type the variable username
    # Retrieve the users input: username = input()
    # Print Welcome, steve123 (whatever the username is storing)
    # Use an f-string to print data with a variable:
    #   print(f"Welcome, {username}")
    #
    # Expected output:
    ################################
    # Welcome, steve123
    #############################################################
#Solution#
username = input("What is your UserName: ")
print(f"Welcome, {username}")



#################################################################
# Print Information and Variable Intermediate
#################################################################

    # Intermediate Question 1
    # Get the user's name and address and say that the user lives
    # at their address. The name should start with a capital and 
    # the address should be displayed with all capitals
    #
    # Expected output:
    ################################
    # Steve lives at 959 S 49 W REXBURG, IDAHO
    #############################################################
#Solution#
name = input("What is your name: ")
address = input("What is your address: ")
print(f"{name.capitalize()} lives at {address.upper()}")



#################################################################
# Advanced (Operators (+,*,/) are explained in the WEEK 3 module)
#################################################################

    # Advanced Question 1
    # Make a program that takes 2 numbers from the user and display
    # the first number, the operator (first +, then *, then /), the
    # second number, and finally the result of the operation.
    #
    # Next make each section in a column
    # Expected output:
    ################################
    #What is the first number: 120
    # What is the second number: 3
    # First number: Operator: Second number: Sum:           
    # 120           +         3              123            
    # First number: Operator: Second number: Product:       
    # 120           *         3              360            
    # First number: Operator: Second number: Dividend:      
    # 120           /         3              40.0     
    #############################################################
#Solution#
first_number = int(input("What is the first number: "))
second_number = int(input("What is the second number: "))

sum = first_number + second_number
product = first_number * second_number
dividend = first_number / second_number

print(f'{"First number:":<14}{"Operator:":<10}{"Second number:":<15}{"Sum:":<15}')
print(f"{first_number:<14}{'+':<10}{second_number:<15}{sum:<15}")
print(f'{"First number:":<14}{"Operator:":<10}{"Second number:":<15}{"Product:":<15}')
print(f"{first_number:<14}{'*':<10}{second_number:<15}{product:<15}")
print(f'{"First number:":<14}{"Operator:":<10}{"Second number:":<15}{"Dividend:":<15}')
print(f"{first_number:<14}{'/':<10}{second_number:<15}{dividend:<15}")


