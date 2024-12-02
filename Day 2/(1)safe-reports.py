# List of reports, 5 numbers per line.
# Find number of safe records, safe records are ones which ONLY incriment or
# decriment, not both, and only by a maximum of 3
#
# Using no protection for types, and assuming input is ALWAYS sane
# ADBeta   02 Dec 2024


### Functions #################################################################
# @brief Reads an input file line by line, puts it into a nested list of reports
# @param infile, file input
# @return reports, nexted list of reports
def get_reports_from_file(infile):
    reports = []
    for line in infile:
        # Split reports by space, then convert to int
        curr_report = line.split(" ")
        curr_report = [ int(val) for val in curr_report ]
        # Append the current report to the reports list
        reports.append(curr_report)
    return reports

# @brief Checks if a given report is safe, returns true if so, false if not
# @param report, input report (5 length list)
# @return bool
MAX_JUMP = 3
def is_report_safe(report):
    # Figure out if the list should be ascending or descenting
    is_ascending = False
    if report[0] < report[1]:
        is_ascending = True

    # Go through all values in the report, comparing to prev value
    for index in range(1, len(report)):
        prev_val = report[index - 1]
        curr_val = report[index]

        # If ascending, make sure it keeps ascending
        if (curr_val <= prev_val) and (is_ascending == True):
            return False

        # If descending, make sure it keeps descending
        if (curr_val >= prev_val) and (is_ascending == False):
            return False

        # Make sure the jump is NOT too high
        diff = abs(curr_val - prev_val)
        if diff > MAX_JUMP: 
            return False
    
    return True
        



### Main ######################################################################
# Open the reports file
reports_file = open("./reports.txt", "r")

# Get all the reports in a nested list from the file
report_list = get_reports_from_file(reports_file)

# Check each report is safe. Incriment counter if it is
safe_count = 0
for report in report_list:
    if is_report_safe(report) == True:
        safe_count += 1

# Print how many are safe
print(safe_count)
