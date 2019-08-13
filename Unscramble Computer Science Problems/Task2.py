"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone_time = {}

for record in calls:
    caller, called_number, time = record[0], record[1], float(record[-1])

    if caller not in phone_time:
        phone_time[caller] = time
    else:
        phone_time[caller] += time

    if called_number not in phone_time:
        phone_time[called_number] = time
    else:
        phone_time[called_number] += time

true_phone_lover = max(phone_time, key=lambda key: phone_time[key])

print(f'{true_phone_lover} spent the longest time, {phone_time[true_phone_lover]} seconds, on the phone during September 2016.')
