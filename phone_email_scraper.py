#!/usr/bin/env python3

import re, pyperclip, pprint


# phone number regex
phone_regex = re.compile(r'''
(((\d{3})|(\(\d{3}\)))?  # area code (optional)
(\s|-)?      # first separator
\d{3}       # first 3 digits
-           # second separator
\d{4}       # last 4 digits
((\s(ext(\.)?\s)|x)     # extension word-part (optional)
(\d{2,5}))?)           # extension number-part (optional)
''', re.VERBOSE)

# email regex
email_regex = re.compile(r'''
([A-Z0-9.+_]+    # name part
@               # @ symbol
[A-Z0-9.+_]+    # domain part
(org|com|net|gov|edu))  # ending part
''', re.VERBOSE | re.I)

document = pyperclip.paste()

phone_match = phone_regex.findall(document)
email_match = email_regex.findall(document)

phone_numbers = []
email_addresses = []

for phone_number in phone_match:
    phone_numbers.append(phone_number[0])

for email_address in email_match:
    email_addresses.append(email_address[0])

pprint.pprint(phone_numbers)
pprint.pprint(email_addresses)
