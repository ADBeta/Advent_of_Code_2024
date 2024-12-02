# Two lists of Location IDs, left and right.
# Find how many times each number from the left list appears in te right list,
# then multiple the left list number by that (eg if 4 appears 4 times, output is 16).
# Sum these up for final value
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

# @brief finds the number of occurances of each number in lista in listb
# @param lista, input list
# @param listb, input list
# @return listo, list of occurances
def find_occurances_lista_listb(lista, listb):
    listo = []
    for index in range(0, len(lista)):
        listo.append(listb.count(lista[index]))
    return listo

# @brief calculates similarity score of lista and occurances
# @param lista, input list
# @param listo, list of occurances
# @return lists, list of similarity scores
def calc_similarity_score(lista, listo):
    lists = []
    for index in range(0, len(lista)):
        lists.append(lista[index] * listo[index])
    return lists





### Main ######################################################################
# Open the lists file
list_file = open("./id_lists.txt", "r")


# Empty lists to append to
lista = []
listb = []
# Read from the file into the lists
read_file_to_lists(list_file, lista, listb)

# Find how many times each number in lista appears in listb
occur = find_occurances_lista_listb(lista, listb)

# Similarity score is lista * occurance at index
similarity = calc_similarity_score(lista, occur) 

# Result is the sum of similarity score
result = sum(similarity)
print(result)
