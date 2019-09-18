#!/usr/bin/python3

# Menus and stuff

from time import strftime
from terminal import fg_16b, deco, Reset
import settings
import figures
import sys

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
              fg_16b(' [H] Help', 3),
              fg_16b(' [Q] Quit\n', 1)]
    
    print(f'\n{"Menu":^40}')
    print('─'*40)
    for line in window: print(line)
    
    expected = ('1', '2', '9', '0', 'h', 'H', 'q', 'Q')
    while True:
        selection = input('Type a character and press enter: ')
        if selection in expected: break
        else : continue
    
    return selection

def menu_chart_after():
    
    button = [deco(' S ', 'reverse'), deco(' X ', 'reverse'), deco(' R ', 'reverse'), deco(' Q ', 'reverse'), ' Enter ']
    expected = ('s', 'S', 'x', 'X', 'r', 'R', 'q', 'Q')
    
    while True:
        selection = input(f'|{button[0]} Save  |{button[1]} Explain meanings  |{button[2]} Return  |{button[3]} Quit  |{button[4]} command: ')
        if selection in expected: break
        else: continue
    
    return selection

def menu_chart_house():
    
    window = [fg_16b(' [ 1] The self.', 12),
              fg_16b(' [ 2] Money, movable wealth.', 6),
              fg_16b(' [ 3] Siblings, communication, neighborhood.', 12),
              fg_16b(' [ 4] Parents, land, house, lost item.', 6),
              fg_16b(' [ 5] Children and games.', 12),
              fg_16b(' [ 6] Health, employees, pets and small animals.', 6),
              fg_16b(' [ 7] Spouse, partner, relationship.', 12),
              fg_16b(' [ 8] Death, inheritance, the occult.', 6),
              fg_16b(' [ 9] Religion, philosophy, education, journeys.', 12),
              fg_16b(' [10] Career, government, superiors.', 6),
              fg_16b(' [11] Friends and dreams.', 12),
              fg_16b(' [12] Imprisonment, enemies, barn and large animals.', 6),
              ' ',
              fg_16b(' [R ] Return', 3),
              fg_16b(' [Q ] Quit\n', 1)]
    
    expected = ['r', 'R', 'q', 'Q']
    for i in range(1, 13):
        expected.append(str(i))
    
    print(f'\n{"The Astrological Houses":^53}')
    print('─'*53)
    for line in window: print(line)
    
    while True:
        selection = input('Select significator for quesited: ')
        if selection in expected: break
        else: continue
    
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

def name_table():
    
    number = ('1111', '1112', '1121', '1122', '1211', '1212', '1221', '1222',
              '2111', '2112', '2121', '2122', '2211', '2212', '2221', '2222')
    
    byname = ('2121', '2212', '1212', '2111', '1221', '1112', '2112', '2211',
              '1122', '1222', '2222', '1211', '1121', '2122', '2221', '1111')
    
    color = (6, 12, 6, 12, 6, 12, 6, 12, 6, 12, 6, 12, 6, 12, 6, 12)
    
    l_col, r_col = list(), list()
    
    for num in number: r_col.append(f' {num} {figures.Name[num]:<15}')
    for num in byname: l_col.append(f' {num} {figures.Name[num]:<15}')
    
    print(' ')
    for i in range(16): print(fg_16b(l_col[i] + ' '*4 + r_col[i], color[i]))
    print(' ')
    
    while True:
        
        command = input('Please enter the figure\'s number or `r` to return: ')
        if command in number:
            print(' ')
            fig = figures.Figure(command)
            fig.info(True)
            input('Press Enter to continue...')
            return
        elif command == 'r' or command == 'R': return
        else: continue

def element_table():
    
    fire = ('1112', '1122', '1212', '1222')
    air = ('1121', '2121', '2112', '2122')
    water = ('1111', '1211', '2212', '2222')
    earth = ('1221', '2111', '2211', '2221')
    
    clr_f = figures.Color.Element[figures.ELF]
    clr_a = figures.Color.Element[figures.ELA]
    clr_w = figures.Color.Element[figures.ELW]
    clr_e = figures.Color.Element[figures.ELE]
    
    col_f = [f'{clr_f}{figures.ELF:<22}{Reset}']
    col_a = [f'{clr_a}{figures.ELA:<22}{Reset}']
    col_w = [f'{clr_w}{figures.ELW:<22}{Reset}']
    col_e = [f'{clr_e}{figures.ELE:<22}{Reset}']
    
    for n in fire: col_f.append(f'{n} {figures.Name[n]:<17}')
    for n in air: col_a.append(f'{n} {figures.Name[n]:<17}')
    for n in water: col_w.append(f'{n} {figures.Name[n]:<17}')
    for n in earth: col_e.append(f'{n} {figures.Name[n]:<17}')
    
    print(' ')
    for l in range(5):print(col_f[l] + '  ' + col_a[l])
    print(' ')
    for l in range(5): print(col_w[l] + '  ' + col_e[l])
    print('\nNote: Under traditional system, Laetitia is Air and Rubeus is Fire.')
    
    input('Press Enter to continue...')

def planet_table():
    
    clr_sat = figures.Color.Planet[figures.SAT]
    clr_jup = figures.Color.Planet[figures.JUP]
    clr_mar = figures.Color.Planet[figures.MAR]
    clr_sun = figures.Color.Planet[figures.SUN]
    clr_ven = figures.Color.Planet[figures.VEN]
    clr_mer = figures.Color.Planet[figures.MER]
    clr_mon = figures.Color.Planet[figures.MON]
    clr_nno = figures.Color.Planet[figures.NNO]
    clr_sno = figures.Color.Planet[figures.SNO]
    
    print(' ')
    print(f'{clr_sat}{figures.SAT:<13} 1221 Carcer           2221 Tristitia')
    print(f'{clr_jup}{figures.JUP:<13} 1222 Laetitia         2121 Acquisitio')
    print(f'{clr_mar}{figures.MAR:<13} 1121 Puer             2122 Rubeus')
    print(f'{clr_sun}{figures.SUN:<13} 1122 Fortuna Minor    2211 Fortuna Major')
    print(f'{clr_ven}{figures.VEN:<13} 1212 Amissio          1211 Puella')
    print(f'{clr_mer}{figures.MER:<13} 2112 Conjunctio       2122 Albus')
    print(f'{clr_mon}{figures.MON:<13} 1111 Via              2222 Populus')
    print(f'{clr_nno}{figures.NNO:<13} 2111 Caput Draconis')
    print(f'{clr_sno}{figures.SNO:<13} 1112 Cauda Draconis{Reset}\n')
    
    input('Press Enter to continue...')

def zodiac_table():
    
    # Create the zodiac column
    clr_f = figures.Color.Element[figures.ELF]
    clr_a = figures.Color.Element[figures.ELA]
    clr_w = figures.Color.Element[figures.ELW]
    clr_e = figures.Color.Element[figures.ELE]
    
    clr_z = list()
    for i in range(3):
        clr_z.append(clr_f)
        clr_z.append(clr_e)
        clr_z.append(clr_a)
        clr_z.append(clr_w)
    
    zodiac = [figures.ZARI, figures.ZTAU, figures.ZGEM, figures.ZCAN,
              figures.ZLEO, figures.ZVIR, figures.ZLIB, figures.ZSCO,
              figures.ZSAG, figures.ZCAP, figures.ZAQU, figures.ZPIS]
    
    col_z = list()
    for i in range(12):
        col_z.append(f'{clr_z[i]}{zodiac[i]:<15}')
    
    # Figure collumn for Gerardus system
    col_g = ['2121 Acquisitio'                  ,
             '1222 Laetitia     1122 F. Minor'  ,
             '1121 Puer         2122 Rubeus'    ,
             '2212 Albus'                       ,
             '1111 Via'                         ,
             '2112 Conjunctio   2111 Caput D.'  ,
             '1211 Puella'                      ,
             '1212 Amissio      2221 Tristitia' ,
             '1112 Cauda D.'                    ,
             '2222 Populus'                     ,
             '2211 F. Major'                    ,
             '1221 Carcer'                      ]
    
    # Agrippa system
    col_a = ['1121 Puer'                        ,
             '1212 Amissio'                     ,
             '2212 Albus'                       ,
             '1111 Via          2222 Populus'   ,
             '2211 F. Major     1122 F. Minor'  ,
             '2112 Conjunctio   2111 Caput D.   1112 Cauda D.',
             '1211 Puella'                      ,
             '2122 Rubeus'                      ,
             '2121 Acquisitio'                  ,
             '1221 Carcer'                      ,
             '2221 Tristitia'                   ,
             '1222 Laetitia'                    ]
    
    # Print Gerardus table
    print('\n  Gerardus of Cremona')
    print('─'*40)
    for i in range(12): print(col_z[i] + col_g[i])
    print(Reset)
    
    # Print Agrippa table
    print('  Heinrich Cornelius Agrippa')
    print('─'*40)
    for i in range(12): print(col_z[i] + col_a[i])
    print(Reset)
    
    input('Press Enter to continue...')

def menu_help():
    
    window = [fg_16b(' [1] List of figures by element', 2),
              fg_16b(' [2] List of figures by planet', 12),
              fg_16b(' [3] List of figures by zodiac',  2),
              fg_16b(' [4] Show detailed info of a figure', 12),
              '',
              fg_16b(' [R] Return', 3),
              fg_16b(' [Q] Quit\n', 1)]
    
    while True:
        print(f'\n{"Select topic":^40}')
        print('─'*40)
        for l in window: print(l)
        cmd = input('Type a character and press Enter: ')
        
        if cmd == '1'  : element_table()
        elif cmd == '2': planet_table()
        elif cmd == '3': zodiac_table()
        elif cmd == '4': name_table()
        elif cmd == 'q' or cmd == 'Q': sys.exit()
        elif cmd == 'r' or cmd == 'R': return
        else: continue
    
