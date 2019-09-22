import re


phoneNumRegex = re.compile(r'(\(\d\d\d\) )?(\d\d\d)-(\d\d\d\d)')
phoneNumMatch = phoneNumRegex.search('My number is 111-1111')

print(phoneNumMatch.group())

# | separate OR options
batRegex = re.compile(r'Bat(wo)+(man|mobile|copter|bat)')
batMatch1 = batRegex.search('The Adventures of Batman')
batMatch2 = batRegex.search('The Adventures of Batwowowowowowowowowowowowoman')

# print(batMatch1.group(0))
print(batMatch2.group(0))

# ? is optional, + is 1 or more, * is 0 or more
escapeRegex = re.compile(r'(\*)*(\?)?(\+)+')
escapeMatch1 = escapeRegex.search('*****************?+')
escapeMatch2 = escapeRegex.search('?+')
escapeMatch3 = escapeRegex.search('*+')

print(escapeMatch1.group())
print(escapeMatch2.group())
print(escapeMatch3.group())

haRegex = re.compile(r'(Ha){3,}')  # unbounded with minimum 3, matches 3 or more, greedy match
haMatch = haRegex.search('HaHaHa')
print(haMatch.group())

digitsRegex = re.compile(r'(\d){3,5}?')  # bounded between 3-5, non-greedy match when using question mark after braces
digitsMatch = digitsRegex.search('123456')
print(digitsMatch.group())

catRegex = re.compile(r'(cat)')
catMatch = catRegex.findall('Catman is a cool cat, but he does not like other cats.')
print(catMatch)

catRegex2 = re.compile(r'(cat)+(cats)*')
catMatch2 = catRegex2.findall('catcatcat catcat catscatscats cats')
print(catMatch2)

# \d, \w, \s match characters that are digits, word characters, and spaces
# \D, \W, \S match characters that are not digits, word characters, and spaces (negative matching)
# re.IGNORECASE can also be put as re.I

vowels = re.compile(r'[aeiou]', re.IGNORECASE)  # matches the pattern of vowels (character class)
vowelsMatch = vowels.findall('Hello, I am a cool man and you are not cool.')
print(vowelsMatch)

consonants = re.compile(r'[^aeiou]', re.IGNORECASE)  # matches opposite the pattern of vowels (negative character class)
consonantsMatch = consonants.findall('Hello, I am a cool man and you are not cool.')
print(consonantsMatch)

beginsWithRegex = re.compile(r'^Hello')  # ^ symbol matches strings starting with Hello
beginsWithMatch = beginsWithRegex.search('Hello there!')
print(beginsWithMatch.group())
print(beginsWithRegex.search('He said "Hello"!') == None)

endsWithRegex = re.compile(r'world$')  # $ symbol matches strings ending with world
endsWithMatch = endsWithRegex.search('Hello world')
print(endsWithMatch.group())
print(endsWithRegex.search('Hello world!') == None)

allDigitsRegex = re.compile(r'^\d+$')
allDigitsMatch = allDigitsRegex.search('12345x12445435')  # won't work as needs to be only digits throughout the string

atRegex = re.compile(r'.{1,2}at')  # . symbol matches any 1 or 2 characters right before at, except newlines
atMatch = atRegex.findall('The cat in the hat sat on the flat mat')
print(atMatch)

starRegex = re.compile(r'First Name: (.*) Last Name: (.*)')  # match anything after the . symbol after seeing pre-text
starMatch = starRegex.findall('First Name: Zaid Last Name: Bhura')
print(starMatch)

dotStar = re.compile(r'.*', re.DOTALL)  # greedy . match with newlines
dotStarMatch = dotStar.search('Serve the public trust.\nProtect the innocent.\nUphold the law')
print(dotStarMatch.group())

namesRegex = re.compile(r'Agent (\w)\w+')  # \1 is used to substitute group 1, keeping part of the original string
namesMatch = namesRegex.sub(r'Agent \1****', 'Agent Bob gave the secret documents to Agent Cod.')
print(namesMatch)

verboseRegex = re.compile(r'''
                        (\d\d\d-) |     # area code (without parenthesis, with dash)
                        (\(\d\d\d\))    # -or- area code with parenthesis, without dash
                        \d\d\d      # first 3 digits
                        -           # second dash
                        \d\d\d\d    # last 4 digits
                        \sx\d{2,4}
                        ''', re.VERBOSE | re.I | re.DOTALL)  # use bitwise OR operator to combine arguments





