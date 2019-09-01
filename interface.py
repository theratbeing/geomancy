#!/usr/bin/python3

# Menus and stuff

from time import strftime
from terminal import fg_16b, deco
import settings

def header():
    pass

def menu_main():
    ' The main menu '
    
    window = [fg_16b(' [1] Create shield chart (automatic)', 6),
              fg_16b(' [2] Create shield chart (manual input)', 12),
              ' ',
              fg_16b(' [9] Create house chart  (automatic)', 6),
              fg_16b(' [0] Create house chart  (manual input)', 12),
              ' ',
              ' [H] Help',
              ' [Q] Quit\n']
    
    print(f'\n{"Menu":^40}')
    print('─'*40)
    for line in window: print(line)
    
    expected = ('1', '2', '9', '0', 'h', 'H', 'q', 'Q')
    while True:
        selection = input('Type a character and press enter: ')
        if selection in expected: break
        elif selection == '': pass
        else: print(fg_16b(f'Unrecognized command: {selection}. Please retry.', 1))
    
    return selection

def menu_chart_after():
    
    button = [deco(' S ', 'reverse'), deco(' X ', 'reverse'), deco(' R ', 'reverse'), deco(' Q ', 'reverse'), ' Enter ']
    expected = ('s', 'S', 'x', 'X', 'r', 'R', 'q', 'Q')
    
    while True:
        selection = input(f'|{button[0]} Save  |{button[1]} Explain meanings  |{button[2]} Return  |{button[3]} Quit  |{button[4]} command: ')
        if selection in expected: break
        elif selection == '': pass
        else: print(fg_16b(f'Unrecognized command: {selection}. Please retry.', 1))
    
    return selection

def menu_chart_house():
    
    window = [fg_16b(' [ 1] The self.', 12),
              fg_16b(' [ 2] Money, movable wealth.', 2),
              fg_16b(' [ 3] Siblings, communication, neighborhood.', 12),
              fg_16b(' [ 4] Parents, land, house, lost item.', 2),
              fg_16b(' [ 5] Children and games.', 12),
              fg_16b(' [ 6] Health, employees, pets and small animals.', 2),
              fg_16b(' [ 7] Spouse, partner, relationship.', 12),
              fg_16b(' [ 8] Death, inheritance, the occult.', 2),
              fg_16b(' [ 9] Religion, philosophy, education, journeys.', 12),
              fg_16b(' [10] Career, government, superiors.', 2),
              fg_16b(' [11] Friends and dreams.', 12),
              fg_16b(' [12] Imprisonment, enemies, barn and large animals.', 2),
              ' ',
              ' [R ] Return',
              ' [Q ] Quit\n',]
    
    expected = ['r', 'R', 'q', 'Q']
    for i in range(1, 13):
        expected.append(str(i))
    
    print(f'\n{"The Astrological Houses":^53}')
    print('─'*53)
    for line in window: print(line)
    
    while True:
        selection = input('Select significator for quesited: ')
        if selection in expected: break
        elif selection == '': pass
        else: print(fg_16b(f'Unrecognized command: {selection}. Please retry.', 1))
    
    return selection

def ask_four_figures():
    print('\nEnter 4 figures in numeric form separated by space e.g. 1122 2212 2112 2111')
    print('Type `r` or `random` without quotes to generate random numbers.')
    
    while True:
        seed = input('> ')
        
        # user types empty string so ask again
        if seed == '': continue
        # let them use random seed
        elif (seed == 'random') or (seed == 'r'):
            output = list()
            break
        else: pass
        
        # sanitize user input with pattern recognition
        pattern = [1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1]
        test = list()
        for char in seed:
            if (char == '1') or (char == '2'): test.append(1)
            elif char == ' ': test.append(0)
            else: test.append(2)
        
        if test != pattern: print(fg_16b('Invalid input. Please retry.', 1))
        else:
            output = seed.split()
            break
    
    return output

def save_dialogue(nm, qn, dt, ch):
    while True:
        # ask for file name. Use default setting if empty
        try: filename = input('\nFile name: ') or settings.LOG_DEFAULT_NAME
        except KeyboardInterrupt: return
        
        # set newline character
        if settings.LOG_NEWLINE == 'windows': nl = '\r\n'
        else: nl = '\n'
        
        # fetch chart data
        content = ch.generate_log_string(nl)
        
        try:
            log = open(filename, 'a+')
            log.write(f'Name : {nm}{nl}Query: {qn}{nl}Time :{dt}{nl}{nl}')
            log.write(content)
            log.write('='*80 + nl)
            log.close()
            print('File saved successfully.')
            return
        
        except IOError:
            print(fg_16b(f'Cannot write to file: {filename}.', 1))
            print('Please try another name or press Ctrl + C to cancel.')
            continue

def correspondence_table(sort_by='number'):
    
    number = ('1111', '1112', '1121', '1122', '1211', '1212', '1221', '1222',
              '2111', '2112', '2121', '2122', '2211', '2212', '2221', '2222')
    
    byname = ('2121', '2212', '1212', '2111', '1221', '1112', '2112', '2211',
              '1122', '1222', '2222', '1211', '1121', '2122', '2221', '1111')
    
    planet = ('1221', '2221', '2121', '1222', '1121', '2122', '2211', '1122',
              '1212', '1211', '2212', '2112', '2222', '1111', '2111', '1112')
    
    element_trad = ('1212')
