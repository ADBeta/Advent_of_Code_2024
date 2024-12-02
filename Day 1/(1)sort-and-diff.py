# Two lists of Location IDs, left and right.
# Need to sort lists by value, then diff the two lists to find the remainder.
# Add remainders up, and this is the solution
#
# Using no protection for types, and assuming input is ALWAYS sane
# ADBeta   01 Dec 2024


### Functions #################################################################
# @brief Reads an input file line by line, puts it into two lists (a, b)
# @param infile, input file object to read
# @param lista, list a output
# @param listb, list b output
# @return None
def read_file_to_lists(infile, lista, listb):
    for line in infile:
        # Split using the three spaces in the original input given
        numbers = line.split("   ")
        # Left number goes in lista, right into listb
        lista.append(int(numbers[0]))
        listb.append(int(numbers[1]))

# @brief Subtracts lista[x] from listb[x], and stores distance in listd
# NOTE Uses lista as legnth, make sure lista and listb are same length
# @param lista, list of numbers
# @param listb, list of numbers
# @return listr, list of distances
def distance_lista_from_listb(lista, listb):
    listd = []
    for index in range(0, len(lista)):
        listd.append(abs(lista[index] - listb[index]))

    return listd


### Main ######################################################################
# Open the lists file
list_file = open("./id_lists.txt", "r")


# Empty lists to append to
lista = []
listb = []
# Read from the file into the lists
read_file_to_lists(list_file, lista, listb)

# Sort lista and listb by value, smallest to largest
lista.sort()
listb.sort()

# Get distance from the two lists, return list of distances
listd = distance_lista_from_listb(lista, listb)

# Add all the distances up
result = sum(listd)

print(result)
