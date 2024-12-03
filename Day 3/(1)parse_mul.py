# File of corrupted mul instructions. Pattern SHOULD look like:
# mul(num,num), where num can be 1-3 digits long
# Parse out all correct mul instructions, calculate total
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

# Get a list of all occurances of the regex expression needed
instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", corrupted)

# Parse the numbers in the mul instruction, mul them and return the result,
# for each instruction
# Add these together for result
result = 0
for instr in instructions:
    result += parse_mul(instr)

print(result)
