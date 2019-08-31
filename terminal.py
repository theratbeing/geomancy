#!/usr/bin/python3

# Module for terminal display

Reset = '\u001b[0m'

Style = {'reset':'\u001b[0m',
         'bold':'\u001b[1m',
         'dim':'\u001b[2m',
         'italic':'\u001b[3m',
         'underline':'\u001b[4m',
         'blink':'\u001b[5m',
         'reverse':'\u001b[7m',
         'conceal':'\u001b[8m',
         'strike':'\u001b[9m',
         'overline':'\u001b[53m',
         'none':''}

Fore = {'black':'\u001b[30m', 'bright_black':'\u001b[90m',
        'red':'\u001b[31m', 'bright_red':'\u001b[91m',
        'green':'\u001b[32m', 'bright_green':'\u001b[92m',
        'yellow':'\u001b[33m', 'bright_yellow':'\u001b[93m',
        'blue':'\u001b[34m', 'bright_blue':'\u001b[94m',
        'magenta':'\u001b[35m', 'bright_magenta':'\u001b[95m',
        'cyan':'\u001b[36m', 'bright_cyan':'\u001b[96m',
        'white':'\u001b[37m', 'bright_white':'\u001b[97m',
        'none':''}

Back = {'black':'\u001b[40m', 'bright_black':'\u001b[100m',
        'red':'\u001b[41m', 'bright_red':'\u001b[101m',
        'green':'\u001b[42m', 'bright_green':'\u001b[102m',
        'yellow':'\u001b[43m', 'bright_yellow':'\u001b[103m',
        'blue':'\u001b[44m', 'bright_blue':'\u001b[104m',
        'magenta':'\u001b[45m', 'bright_magenta':'\u001b[105m',
        'cyan':'\u001b[46m', 'bright_cyan':'\u001b[106m',
        'white':'\u001b[47m', 'bright_white':'\u001b[107m',
        'none':''}

def make_256_table():
    start = (16, 52, 88, 124, 160, 196,
             34, 70, 106, 142, 178, 214)
    
    for i in range(8):
        print(f'\u001b[38;5;{i}m{i:>3} ', end='')
    print('')
    
    for i in range(8, 16):
        print(f'\u001b[38;5;{i}m{i:>3} ', end='')
    print('\n')
    
    for row in start:
        if row == 34: print('')
        for i in range(18):
            print(f'\u001b[38;5;{row+i}m{row+i:>3} ', end='')
        print('')
    
    print('')
    for i in range(232, 244):
        print(f'\u001b[38;5;{i}m{i:>3} ', end='')
    print('')
    for i in range(244, 256):
        print(f'\u001b[38;5;{i}m{i:>3} ', end='')
    print(Reset)

def color_palette():
    
    print('Decorations')
    for name in Style:
        print(f'{Style[name]}{name}{Reset} ', end='')
    
    print('\n\nStandard Colors')
    for name in Fore:
        print(f'{Fore[name]}{name} {Reset}', end='')
    print('\n')
    
    for name in Back:
        print(f'{Back[name]} {name} {Reset}', end='')
    print('')
    
    print('\n16-bit Colors')
    make_256_table()
    print(Style['reverse'])
    make_256_table()

def color_8b(text, fg='none', bg='none', st='none'):
    return Fore[fg] + Back[bg] + Style[st] + text + Reset

def fg_16b(text, fg):
    return f'\u001b[38;5;{fg}m{text}{Reset}'

def bg_16b(text, bg):
    return f'\u001b[48;5;{bg}m{text}{Reset}'

def deco(text, style):
    return Style[style] + text + Reset

def esc_16b(number, mode='f'):
    if mode == 'f': return f'\u001b[38;5;{number}m'
    elif mode == 'b': return f'\u001b[48;5;{number}m'
    elif mode == 'x': return f'\u001b[{number}m'
    else: raise ValueError('`mode` must be set to either `f`, `b`, or `x`!')

if __name__ == '__main__':
    color_palette()
