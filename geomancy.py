#!/usr/bin/python3

# Main program

import sys
import figures
import charts
import interface
import settings
from time import strftime
from terminal import fg_16b

# Greet the user
interface.header()

# Main loop
while True:
    
    # main menu
    command = interface.menu_main()
    
    
    # if help or exit
    if (command == 'h') or (command == 'H'): continue
    elif (command == 'q') or (command == 'Q'): sys.exit()
    else: pass
    
    # ask significator if applicable
    if (command == '3') or (command == '4'):
        sub_command = interface.menu_chart_house()
        if (sub_command == 'q') or (sub_command == 'Q'): sys.exit()
        elif (sub_command == 'r') or (sub_command == 'R'): continue
        # python counts from 0
        else: quesited = int(sub_command) - 1
    else: pass
    
    # ask for name and question
    print(' ')
    name = input('Name : ')
    question = input('Query: ')
    
    # automatic generation
    if (command == '1') or (command == '3'): raw_chart = figures.generate_figures()
    
    # manual input
    elif (command == '2') or (command == '4'):
        seed = interface.ask_four_figures()
        raw_chart = figures.generate_figures(seed)
    
    else: pass
    
    print(' ')
    
    # get and show the time
    date_time = strftime("%Y-%m-%d (%a) %H:%M:%S")
    print(f'╔{"═"*78}╗')
    print(f'║{date_time:^78}║')
    print(f'╚{"═"*78}╝')
    
    # build the chart
    if (command == '1') or (command == '2'):
        Chart = charts.ShieldChart(raw_chart)
        color = settings.SHIELD_COLOR_SCHEME
    
    elif (command == '3') or (command == '4'):
        Chart = charts.HouseChart(raw_chart, settings.HOUSE_SYSTEM, settings.HOUSE_QUERENT, quesited)
        color = settings.HOUSE_COLOR_SCHEME
    
    else: pass
    
    # draw the chart
    Chart.draw()
    
    # ask what to do next
    command = interface.menu_chart_after()
    # quit
    if (command == 'q') or (command == 'Q'): sys.exit()
    
    # return to main menu
    elif (command == 'r') or (command == 'R'): continue
    
    # save to file
    elif (command == 's') or (command == 'S'):
        while True:
            # ask for file name. Use default setting if empty
            try: filename = input('File name: ') or settings.LOG_DEFAULT_NAME
            except KeyboardInterrupt: break
            
            # set newline character
            if settings.LOG_NEWLINE == 'windows': nl = '\r\n'
            else: nl = '\n'
        
            # fetch chart data
            content = Chart.generate_log_string(nl)
        
            try:
                log = open(filename, 'a+')
                log.write(f'Name : {name}{nl}Query: {question}{nl}Time :{date_time}{nl}{nl}')
                log.write(content)
                log.write('='*80 + nl)
                log.close()
                break
        
            except IOError:
                print(fg16_b(f'Cannot write to file: {filename}.', 1))
                print('Please try another name or press Ctrl + C to cancel.')
                continue
        
    else: pass
