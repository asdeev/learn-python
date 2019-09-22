"""
******************
*                *
*                *
*                *
*                *
******************
"""

import traceback


def box_print(symbol, width, height):
    try:
        if len(symbol) != 1:
            raise Exception('"symbol" needs to be a length of 1.')

        if (width < 2) or (height < 2):
            raise Exception('"width" and "height" must be greater or equal to 2.')

        print(symbol * width)

        for i in range(height - 2):
            print(symbol + (' ' * (width - 2)) + symbol)

        print(symbol * width)
    except:
        error_file = open('error_log.txt', 'a')
        error_file.write(traceback.format_exc())
        error_file.close()
        print('The traceback info was written to error_log.txt')


box_print('*', 14, 4)
