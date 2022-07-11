########################################################################
# Functions advanced
########################################################################

# Prepare employee name tags.
# track the year they started, and if they have been employed more than
# 10 years the nametag should be listed as a gold nametag (otherwise plain)
# Do not send the intern data to the printer, because they won't be
# employed when the nametags are recieved from the printers

# There should be atleast 2 functions (one to read the file, one to write the
# to a new file for the printer)

# expected output:
# Gold
# Oliver - Lead Software Engineer
# 
# Plain
# Liam - Software Engineer

FILENAME = "employee_info.txt"
WRITEFILE = "printer.txt"

def main():
    data = readfile(FILENAME)
    writefile(WRITEFILE, data)

    pass


def readfile(file):
    new_data = []
    with open(file) as data:
        for item in data:
            print(item)
            new_data.append(item)
    return new_data

def writefile(file, data):
    pass
        



if __name__ == '__main__':
    main()