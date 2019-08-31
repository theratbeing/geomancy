#!/usr/bin/python3

# Main program

import sys
import figures
import charts
import interface
import settings
from time import strftime

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
    date_time = strftime("%Y-%m-%d %A %H:%M:%S")
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
    
    while True:
        # ask what to do next
        command = interface.menu_chart_after()
        # quit
        if (command == 'q') or (command == 'Q'): sys.exit()
        # return to main menu
        elif (command == 'r') or (command == 'R'): break
        # explain figure meanings
        elif (command == 'x') or (command == 'X'):
            Chart.explain()
        # save to file
        elif (command == 's') or (command == 'S'):
            interface.save_dialogue(name, question, date_time, Chart)
        else: pass
