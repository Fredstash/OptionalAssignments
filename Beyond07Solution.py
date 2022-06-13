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

# Use a loop to multiply the numbers 1-10 by 2
#########################################################
for x in range(0, 11):
    print(x * 2, end=" ")
print()

########################################################################
# Loops Intermediate
########################################################################

    # Create a minesweep board (5X5)
    # The O's are the mines and they should be randomly spread 
    # between the X's
    # Expected Output (comparable to this):
    # XXOOX
    # OXXXX
    # OXXXX
    # OOXOX
    # XXOXX
    #########################################################

for x in range(5):
    for y in range(5):
        if random.randint(1, 10) in [1,2,3]:
            print("O", end='')
        else:
            print("X", end='')
    print()



########################################################################
# Loops Advanced Using Lists (WEEK 9)
########################################################################

my_list = [1, 2, 3, 4, 5 ,6 ,7 ,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
evens_list = []

for i in my_list:
    if i % 2 == 0:
        evens_list.append(i)

# Two solutions for sum

total = sum(evens_list)
print(total)

# Or

total = 0
for x in evens_list:
    total+=x
print(total)


########################################################################
# DEBUG (Loops are a very common issue to debug)
########################################################################

for i in range(10):
    results = 0
    results += i
print(results)