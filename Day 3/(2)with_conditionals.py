# File of corrupted mul instructions. parse all muls.
# Conditional do() and dont() statements now need to  be taken into account
# in order 
#
# Using no protection for types, and assuming input is ALWAYS sane
# ADBeta   03 Dec 2024

# regex
import re

### Functions #################################################################
# @brief parses the mul instruction, and returns the result
# @param instr, instruction string (single)
# @return result, result from the mul
def parse_mul(instr):
    # find all numbers, convert to int
    nums = re.findall(r"\d+", instr)
    nums = [ int(num) for num in nums ]

    return nums[0] * nums[1]
    


### Main ######################################################################
# Open the instructons file
instructions_file = open("./instructions.txt", "r")

# Remove all whitespace from the file, and comcat it as a single string
corrupted = ""
for line in instructions_file:
    corrupted += line.strip()


# Go through the string looking for do() dont() and mul()
# enable mul by default
# Add to result when enabled
result = 0
enabled = True
offset = 0

while True:
    # Find the next match of any of the strings
    match = re.search(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", corrupted[offset:])
    # If no match was found, exit
    if match is None:
        break

    # Incriment the offset position
    offset += match.end()
    
    # Get the match string
    instr = match.group(0)

    # If the instruction was do(), enable
    if instr == "do()":
        enabled = True
    # If it's dont(), disable
    elif instr == "don't()":
        enabled = False
    # If it is anything else, and enabled is True, calculate it
    else:
        if enabled is True:
            result += parse_mul(instr)

print(result)
