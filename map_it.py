import webbrowser
import sys
import pyperclip


# check if command line arguments were passed
if len(sys.argv) > 1:
    # ['map_it.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/{address}'.format(address=address))
