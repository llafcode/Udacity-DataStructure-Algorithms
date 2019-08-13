"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# For both sub-tasks, we need to know the total number of call records
# made by people in Bangalore, so we should define a function for that.
def find_records_by_area(calls, area='Bangalore'):
    """
    :param calls: list of call records
    :param area: string, specify the call area, default Bangalore for this task.

    :return records_to_find: list of call records made by people in a certain area
    """

    records_to_find = []
    # For future use, this function can be modified to a record filter by specifying call areas,
    # and mapping from area name to code,
    # using a dictionary or similar structure.
    # For now, we concentrate on only the calls made from Bangalore
    if area is not None:
        area_prefix = '080'

    for record in calls:
        caller = record[0]
        # We don't want the brackets in the area code, in order to better sort all codes
        if caller.split(')')[0][1:] == area_prefix:
            records_to_find.append(record)

    return records_to_find

# Define a function to check if the number is a fix line
def isfixline(number):
    """
    Fixed lines start with an area code enclosed in brackets. The area
    codes vary in length but always begin with 0.

    :param number: string of numbers
    :return: boolean, true if the given number is a fix line.
    """
    if number[0] == '(':
        return True
    return False

# Define a function to check if the number is a mobile phone
def ismobile(number):
    """
    Mobile numbers have no parentheses, but have a space in the middle
    of the number to help readability. The prefix of a mobile number
    is its first four digits, and they always start with 7, 8 or 9.

    :param number: string of numbers
    :return: boolean, true if the given number is a mobile number.
    """
    if number[0] in ['7', '8', '9']:
        return True
    return False

if __name__ == '__main__':

    calls_from_bangalore = find_records_by_area(calls, area='Bangalore')

    """Part A"""
    codes_to_find = []

    for record in calls_from_bangalore:
        called_number = record[1]

        if isfixline(called_number):
            prefix = called_number.split(')')[0][1:]
            codes_to_find.append(prefix)
        elif ismobile(called_number):
            prefix = called_number[:4]
            codes_to_find.append(prefix)

    codes_to_find.sort()
    print('The numbers called by people in Bangalore have codes:')
    for code in codes_to_find:
        print(code)

    """Part B"""
    bangalore_to_bangalore = 0
    bangalore_prefix = '080'

    for record in calls_from_bangalore:
        called_number = record[1]

        if isfixline(called_number):
            prefix = called_number.split(')')[0][1:]
            if prefix == bangalore_prefix:
                bangalore_to_bangalore += 1

    print(f"{bangalore_to_bangalore / len(calls_from_bangalore) * 100: .2f} "
          f"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
