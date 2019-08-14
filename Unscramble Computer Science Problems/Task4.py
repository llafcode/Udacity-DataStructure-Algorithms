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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


if __name__ == '__main__':
    numbers_with_texts_receive_calls = set()
    numbers_make_calls = set()

    suspect_telemarketers = set()

    for record in texts:
        sender, recipient = record[0], record[1]

        numbers_with_texts_receive_calls.add(sender)
        numbers_with_texts_receive_calls.add(recipient)

    for record in calls:
        caller, called = record[0], record[1]

        numbers_make_calls.add(caller)
        numbers_with_texts_receive_calls.add(called)

    suspect_telemarketers = sorted(numbers_make_calls.difference(numbers_with_texts_receive_calls))

    print('These numbers could be telemarketers: ')
    for number in suspect_telemarketers:
        print(number)
