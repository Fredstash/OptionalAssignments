# Data stored [name, number of siblings, birth year]
data = ["Ryan", 7, 1998, "Steve", 2, 2000, "Bill", 3, 1993, "Lucas", 6, 2003, "Greg", 5, 1965]

# Store the location of the data list
track_location = 1

# Storage for each type of data
name = []
siblings = []
birth_year = []

# Loop through data list
for track_location in range(len(data)):

    # Sort the data using modulus into the correct list
    # Sort into name:
    if track_location % 3 == 0:
        name.append(data[track_location])
        track_location += 1

    # Sort into siblings
    if track_location % 3 == 1:
        siblings.append(data[track_location])
        track_location += 1

    # Sort into birth year
    if track_location % 3 == 2:
        birth_year.append(data[track_location])
        track_location += 1


# Display the lists
print(name)
print(siblings)
print(birth_year)