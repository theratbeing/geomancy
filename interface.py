#!/usr/bin/python3

# Menus and stuff

from time import strftime
from terminal import fg_16b, deco
import settings

def header():
    print(f'╔{"═"*78}╗')
    print(f'║{"Geomancy Chart Generator":^78}║')
    print(f'╚{"═"*78}╝')

def menu_main():
    ' The main menu '
    
    window = [f'┌{"─"*40}┐',
              f'│ [1] Create shield chart (automatic   ) │',
              f'│ [2] Create shield chart (manual input) │',
              f'│ {" ":<38} │',
              f'│ [3] Create house chart  (automatic   ) │',
              f'│ [4] Create house chart  (manual input) │',
              f'│ {" ":<38} │',
              f'│ {"[H] Help":<38} │',
              f'│ {"[Q] Quit":<38} │',
              f'└{"─"*40}┘']
    
    expected = ('1', '2', '3', '4', 'h', 'H', 'q', 'Q')
    
    print(f'\n{"Menu":^80}')
    for line in window: print(f'{line:^80}')
    
    while True:
        selection = input('Type a character and press enter: ')
        if selection in expected: break
        elif selection == '': pass
        else: print(fg_16b(f'Unrecognized command: {selection}. Please retry.', 1))
    
    return selection

def menu_chart_after():
    
    button = [deco(' S ', 'reverse'), deco(' X ', 'reverse'), deco(' R ', 'reverse'), deco(' Q ', 'reverse'), deco(' Enter ', 'reverse')]
    selection = input(f'|{button[0]} Save  |{button[1]} Explain meanings  |{button[2]} Return  |{button[3]} Quit  |{button[4]} command: ')
    
    expected = ('s', 'S', 'x', 'X', 'r', 'R', 'q', 'Q')
    
    while True:
        if selection in expected: break
        else: print(fg_16b(f'Unrecognized command: {selection}. Please retry.', 1))
    
    return selection

def menu_chart_house():
    
    window = [f'┌{"─"*55}┐',
              f'│ {"[ 1] The self.":<53} │',
              f'│ {"[ 2] Money, movable wealth.":<53} │',
              f'│ {"[ 3] Siblings, communication, neighborhood.":<53} │',
              f'│ {"[ 4] Parents, land, house, lost item.":<53} │',
              f'│ {"[ 5] Children and games.":<53} │',
              f'│ {"[ 6] Health, employees, pets and small animals.":<53} │',
              f'│ {"[ 7] Spouse, partner, relationship.":<53} │',
              f'│ {"[ 8] Death, inheritance, the occult.":<53} │',
              f'│ {"[ 9] Religion, philosophy, education, journeys.":<53} │',
              f'│ {"[10] Career, government, superiors.":<53} │',
              f'│ {"[11] Friends and dreams.":<53} │',
              f'│ {"[12] Imprisonment, enemies, barn and large animals.":<53} │',
              f'│ {" ":<53} │',
              f'│ {"[R ] Return":<53} │',
              f'│ {"[Q ] Quit":<53} │',
              f'└{"─"*55}┘', ' ']
    
    expected = ['r', 'R', 'q', 'Q']
    for i in range(1, 13):
        expected.append(str(i))
    
    print(f'\n{"The Astrological Houses":^80}')
    for line in window: print(f'{line:^80}')
    
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
