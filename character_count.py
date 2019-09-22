import pprint

message = 'It was a bright cold day and the clock striked thirteen.'

count = {}

for c in message.upper():
    count.setdefault(c, 0)
    count[c] += 1

text = pprint.pformat(count)

print(text)