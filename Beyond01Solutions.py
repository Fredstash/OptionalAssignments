########################################################################
# Print information beginner
########################################################################

    # Type print()
    # Inside of the parentheses type "" or ''
    # Inside of "" or '' type what you want the computer to display
    ########################################################################
#Solution#
print("String of information")

    # Declare a variable by typing a name (people)
    # Add an equal sign after the variable and place "" or '' with whatever you want to print
    # Type print()
    # Add variable in the parentheses of the print statement
    ########################################################################
#Solution#
info = "String of information in variable"
print(info)



########################################################################
# Print information intermediate
########################################################################

    # Ask the user how many people they know and print how many people they know
    ########################################################################
#Solution#
info = input("How many people do you know? ")
print("People you know: ")
print("info")



########################################################################
# Print information advanced (Find more about if statements in WEEK 05)
########################################################################

    # Ask the user for what which activty they like best- coding or gaming
    # If they like coding print "You must be pretty smart at coding"
    # If they like gaming print "You must have a lot of fun gaming"
    ########################################################################
#Solution#
activity = input("Do you like coding or gaming better [coding/gaming] ")
if activity == "coding":
    print(f"You must be pretty smart at {activity}")
if activity == "gaming":
    print(f"You must have a lot of fun {activity}")