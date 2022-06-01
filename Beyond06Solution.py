import random
########################################################################
# Loops Beginner
########################################################################

# Adk the user what they want to do until they type in quit
# display what they want to (make sure it doesn't)
#########################################################

action = ''
while action.lower() != "quit":
    action = input("What do you want to do (Type QUIT to end): ")
    if action != "quit":
        print(f"I want to {action}")

# Take this list and print each number multiplied by 2
#########################################################
numbers = [0,1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    print(x * 2, end=" ")
print()

########################################################################
# Loops Intermediate
########################################################################

    # Create a minesweep board (5X5)
    # The O's are the mines and they should be randomly spread 
    # between the X's
    # Expected Output:
    # XXOOX
    # OXXXX
    # OXXXX
    # OOXOX
    # XXOXX
    #########################################################

for x in range(5):
    for y in range(5):
        row = []
        if random.randint(1, 10) in (1,2,3):
            print("O", end='')
        else:
            print("X", end='')
    print()



########################################################################
# Loops Advanced
########################################################################



