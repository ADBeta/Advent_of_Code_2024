# Wordsearch looking for "XMAS", can be forwards (XMAS) or backwards (SAMX).
# Can be horizontal, vertical, or diagonal
#
# Idea: Use a sliding window to search, the exact size of the search string in
# all directions, do a search in this space, then move onto the next chunk.
# Search each chunk in one go vert, horiz, diag_left and diag_right
#
# Using no protection for types, and assuming input is ALWAYS sane
# ADBeta   04 Dec 2024


# TODO: mask out any found so they do not count multiple times - but can still overlap

SEARCHWORD = "XMAS"

### Functions #################################################################
# @brief create a search window from the input, at given position. TODO: Add protection for sizes greater than the input
# @param input, input list of strings to be split into a window
# @param xpos, x position to create the window from
# @param ypos, y position to create the window from
# @param size, size of the searchword to be found
# @return window, list of strings the exact size square
def create_search_window(input, xpos, ypos, size):
    window = []

    # Get the needed substrings
    for index in range(0, size):
        window.append( input[ypos + index][ xpos : xpos + size ] )

    return window


# @brief simple macro type function to neaten code
def matches_search(string):
    # Search normal AND reverse ([::-1] reverses)
    if string == SEARCHWORD or string == SEARCHWORD[::-1]:
        return True
    
    return False

# @brief Horizontal matching checks
# @param window to be searched
# @return number of matches
def get_horz_matches(window):
    matches = 0
    for h_str in window:
        if matches_search(h_str):
            matches += 1
    
    return matches

# @brief Vertical matching checks
# @param window to be searched
# @return number of matches
def get_vert_matches(window):
    matches = 0
    # NOTE: Searching by known length rather than calculated to save time
    for v_line in range(0, 4):
        v_str = window[0][v_line] \
              + window[1][v_line] \
              + window[2][v_line] \
              + window[3][v_line]
        if matches_search(v_str):
            matches += 1
    
    return matches

# @brief Diagonal matching checks
# @param window to be searched
# @return number of matches
def get_diag_matches(window):
    matches = 0
    # NOTE: using known lengths to save time
    
    # Dearch Diagonal down & right
    dr_str = window[0][0] \
           + window[1][1] \
           + window[2][2] \
           + window[3][3]
    if matches_search(dr_str):
        matches += 1

    # Search Diagonally down & left
    dl_str = window[0][3] \
           + window[1][2] \
           + window[2][1] \
           + window[3][0]
    if matches_search(dl_str):
        matches += 1

    return matches



### Main ######################################################################
# Open the wordsearch file
wordsearch_file = open("./wordsearch.txt", "r")

# Create a list of strings from the input file
wordsearch = []
for line in wordsearch_file:
    wordsearch.append(line.strip())


# Keep track of how many matches were found
matches = 0

# Create a window for every position, in every line of the input
MAX_X = len(wordsearch[0]) - len(SEARCHWORD) + 1
MAX_Y = len(wordsearch)    - len(SEARCHWORD) + 1
WINDOW_SIZE = len(SEARCHWORD)
for xpos in range(0, MAX_X):
    for ypos in range(0, MAX_Y):

        window = create_search_window(wordsearch, xpos, ypos, WINDOW_SIZE)

        matches += get_horz_matches(window)
        matches += get_vert_matches(window)
        matches += get_diag_matches(window)

print("Total Matches:", matches)
