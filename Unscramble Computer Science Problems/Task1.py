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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_numbers = []

for record in texts + calls:
    first_number, second_number = record[0], record[1]
    if first_number not in unique_numbers:
        unique_numbers.append(first_number)
    if second_number not in unique_numbers:
        unique_numbers.append(second_number)

print(f'There are {len(unique_numbers)} different telephone numbers in the records.')
