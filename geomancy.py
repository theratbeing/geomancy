#!/usr/bin/python3
# Simple geomancy shield chart generator

import platform
import sys
import random
from time import strftime

########## Default settings ##########
# p and k are used to create and display the figures. p=1; k=2
p = " x "
k = "x x"
# They can be changed to whatever symbol you like, e.g.
#p = " o "
#k = "o o"
#p = " * "
#k = "* *"
Interactive = False
Chart = "Shield"
#Chart = "Medieval"
#Chart = "Agrippa"
significator = 7
Luddite = False
Double = False
Color = True
Logging = True
log_override = False
log_file = "geomancy.log"

########## Command line arguments ##########

for cmd in sys.argv:
    if cmd == "-m" or cmd == "--medieval":
        Chart = "Medieval"
    elif cmd == "-a" or cmd == "--agrippa":
        Chart = "Agrippa"
    elif cmd == "-d" or cmd == "--dual":
        Double = True
    elif cmd == "-q" or cmd == "--quiet":
        Logging = False
    elif cmd == "-n" or cmd == "--no-color":
        Color = False
    elif cmd == "-l" or cmd == "--luddite":
        Luddite = True
    elif cmd[:2] == "s=":
        try:
            if 0 < int(cmd[2:]) < 13:
                significator = int(cmd[2:])
        except:
            pass
    else:
        log_file = cmd
        log_override = True
    
######### Special characters and strings #########

fg_white = "\u001b[37m"
fg_red = "\u001b[31m"
fg_yellow = "\u001b[33m"
fg_green = "\u001b[32m"
fg_greenbright = "\u001b[32;1m"
fg_cyan = "\u001b[36m"
fg_blue = "\u001b[34m"
fg_magenta = "\u001b[35m"
fg_gray = "\u001b[30;1m"
bold = "\u001b[1m"
underline = "\u001b[4m"
reversal = "\u001b[7m"
reset = "\u001b[0m"

s = " " # whitespace character for layout
nl = "\n" # newline
fatal_error = "[ERROR] Judge is invalid figure! The script is broken :("
warning_rubeus = "1st Mother is Rubeus. Querent has ulterior motives."
warning_cauda = "1st Mother is Cauda Draconis. Querent won't listen to advice."

########## Windows-only settings ##########

if platform.system() == "Windows":
    nl = "\r\n"
    if Color:
        try:
            from colorama import init
            init()
        except:
            Color = False
            print("[Error] `colorama` is missing! Color is disabled.")

########## Monochrome mode ##########

if Color == False:
    fg_white = None
    fg_red = None
    fg_yellow = None
    fg_green = None
    fg_greenbright = None
    fg_cyan = None
    fg_blue = None
    fg_magenta = None
    fg_gray = None
    bold = None
    underline = None
    reversal = None
    reset = None

########## List of geomantic figures ##########

Via = [p, p, p, p]
Populus = [k, k, k, k]
FMajor = [k, k, p, p]
FMinor = [p, p, k, k]
Conjunctio = [k, p, p, k]
Carcer = [p, k, k, p]
Acquisitio = [k, p, k, p]
Amissio = [p, k, p, k]
Laetitia = [p, k, k, k]
Tristitia = [k, k, k, p]
Puer = [p, p, k, p]
Puella = [p, k, p, p]
Albus = [k, k, p, k]
Rubeus = [k, p, k, k]
Caput = [k, p, p, p]
Cauda = [p, p, p, k]
InvalidJudges = [Laetitia, Tristitia, Puer, Puella, Albus, Rubeus, Caput, Cauda]

########## Color correspondences ##########

Fire = [Laetitia, FMinor, Amissio, Cauda]
Air = [Puer, Rubeus, Acquisitio, Conjunctio]
Water = [Via, Populus, Albus, Puella]
Earth = [Carcer, Tristitia, Caput, FMajor]

def colorizeElement(figure):
    result = []
    if figure in Fire:
        for line in figure:
            result.append(fg_red + line + reset)
    elif figure in Air:
        for line in figure:
            result.append(fg_yellow + line + reset)
    elif figure in Water:
        for line in figure:
            result.append(fg_blue + line + reset)
    else:
        for line in figure:
            result.append(fg_green + line + reset)
    return result

def colorizePlanet(figure):
    result = []
    if figure == Carcer or figure == Tristitia:
        for line in figure:
            result.append(fg_gray + line + reset)
    elif figure == Laetitia or figure == Acquisitio:
        for line in figure:
            result.append(fg_blue + line + reset)
    elif figure == Puer or figure == Rubeus:
        for line in figure:
            result.append(fg_red + line + reset)
    elif figure == FMajor or figure == FMinor:
        for line in figure:
            result.append(fg_yellow + line + reset)
    elif figure == Amissio or figure == Puella:
        for line in figure:
            result.append(fg_green + line + reset)
    elif figure == Conjunctio or figure == Albus:
        for line in figure:
            result.append(fg_cyan + line + reset)
    elif figure == Via or figure == Populus:
        for line in figure:
            result.append(fg_magenta + line + reset)
    else:
        for line in figure:
            result.append(fg_white + line + reset)
    return result

######### Help Text ##########

Help = """{1} NAME       {0}

    geomancy.py         Python script to generate geomantic charts.

{1} SYNOPSIS   {0}

    geomancy.py [options] [s=n] [file]

{1} DESCRIPTION {0}

    By default, this script generates a geomantic shield chart and logs it into
    a plain text file named {4}geomancy.log{0} along with time stamp. Interactive
    mode will log the chart into a file named after the querent unless the file
    was explicitly mentioned in the command.

    -i, --interactive   Ask user prompt before generating charts.
    -l, --luddite       Disable automatic chart analysis.
    -m, --medieval      Generate house chart with medieval arrangement.
    -a, --agrippa       Generate house chart with Pseudo-Agrippa's arrangement.
    -d, --dual          Generate both shield chart and house chart.
    -n, --no-color      Disable color output in terminal.
    -q, --quiet         Disable logging except for errors.
    -h, --help          Show this help screen.
    s=1 ... s=12        The house number of the quesited.
    file                Name of log file to use.

    {2}HOUSE CHART LAYOUT{0}

        {4}(11) {5}(10) {3}( 9)
    {6}(12)              ( 8){0}           (B)   (A)
    {3}( 1)              {4}( 7){0}              (C)
    {5}( 2)              {5}( 6){0}              (D)
        {4}( 3) {6}( 4) {3}( 5){0}

    1-12: Astrological houses           C: Judge
    A   : Right Witness                 D: Reconciler
    B   : Left Witness
    
    Medieval method of geomancy placess the figures in the astrological houses
    in order of their generation. Mothers go to Houses 1-4, Daughters go to
    Houses 5-8, and Nieces go to Houses 9-12.
    
    In the {4}Fourth Book of Occult Philosophy{0}, Pseudo-Agrippa gives a different
    method of placement. The Mothers are placed in angular houses (1, 10, 7, 4)
    the Daughters in succedent houses (2, 11, 8, 5); and the Nieces are placed
    in cadent houses (3, 12, 9, 6). This is the method used by {4}Hermetic Order
    of Golden Dawn.{0}

    {2}MODES OF PERFECTION{0}
    
    When using a house chart, {4}modes of perfection{0} take precedence over the
    Judge. The modes are:
    
    {4}Occupation :{0} the same figure occupies both houses of querent and quesited.
                 This is the most favorable answer possible.
    {4}Conjunction:{0} one significator moves next to the other significator.
                 This shows which party is (or should be) taking initiative.
    {4}Mutation   :{0} both significators appear together elsewhere in the chart.
                 The event will take place in a roundabout way.
    {4}Translation:{0} figure next to significator makes a conjunction.
                 Help from third party is necessary for success. 
    
    {3}Please note that automatic analysis is experimental and unreliable.{0}

    {2}COLOR SCHEME{0}

    {1}Planet          Color                          Element         Color       {0}
    {9}Saturn          Gray                           {3}Fire            Red
    {6}Jupiter         Blue                           {4}Air             Yellow
    {3}Mars            Red                            {6}Water           Blue
    {4}Sun             Yellow                         {5}Earth           Green
    {5}Venus           Green
    {7}Mercury         Cyan
    {8}Moon            Magenta
    {10}Lunar nodes     White{0}
""".format(reset, reversal, underline, fg_red, fg_yellow, fg_green, fg_blue, fg_cyan, fg_magenta, fg_gray, fg_white)

########## Interactive mode ##########

if "-h" in sys.argv or "--help" in sys.argv:
    print(Help)
    quit()

if "-i" in sys.argv or "--interactive" in sys.argv:
    Interactive = True
    print(fg_magenta + "="*72)
    print("Geomantic Chart Generator".center(72))
    print("="*72 + reset + "\n")
    querent = input("{}Name  : {}".format(fg_greenbright, reset))
    if log_override == False and len(querent) > 0:
        log_file = querent + ".log"
    query = input("{}Query : {}".format(fg_greenbright, reset))
    print("\n{}{}Select chart type:\n{}".format(fg_yellow, underline, reset))
    print("1. Shield chart\n2. Medieval house chart\n3. Agrippa house chart\n")
    asktype = input("{}[1/2/3] {}".format(fg_greenbright, reset))
    if asktype == "2":
        Chart = "Medieval"
    elif asktype == "3":
        Chart = "Agrippa"
    else:
        Chart = "Shield"
    if Chart != "Shield":
        print("\n{}{}Please select a House to signify the question:{}".format(fg_yellow, underline, reset))
        print(" 1. The querent.")
        print(" 2. Movable wealth, personal belongings, finance.")
        print(" 3. Communication, neighborhood, siblings, short trip.")
        print(" 4. House, parents and inheritance, land and agriculture, lost items.")
        print(" 5. Children and games.")
        print(" 6. Health, employees, servitude, pets and other small animals.")
        print(" 7. Relationship, spouse, partner, other people.")
        print(" 8. Death, inheritance from others, magic and occultism.")
        print(" 9. Religion, spirituality, philosophy, education, art, long journey.")
        print("10. Career, social standing, government, authority figures, weather.")
        print("11. Friends, benefactors, luck, desired things.")
        print("12. Imprisonment, hardships, enemies, conscpiracy.\n")
        while True:
            sign = input("{}[1-12] {}".format(fg_greenbright, reset))
            try:
                if 0 < int(sign) < 13:
                    significator = sign
                    break
                else:
                    print("{}Please enter a number between 1 to 12!{}".format(fg_red, reset))
            except:
                print("{}Please enter a number between 1 to 12!{}".format(fg_red, reset))
    print(" ")

########## Chart processing starts here ##########

log = None
if Logging:
    log = open(log_file, "a+")

CurrentTime = strftime("%Y-%m-%d (%a) %H:%M:%S")
RawData = []
for x in range(16):
    RawData.append(random.choice([p, k]))

MotherA = RawData[0:4]
MotherB = RawData[4:8]
MotherC = RawData[8:12]
MotherD = RawData[12:16]

DaughterA = [MotherA[0], MotherB[0], MotherC[0], MotherD[0]]
DaughterB = [MotherA[1], MotherB[1], MotherC[1], MotherD[1]]
DaughterC = [MotherA[2], MotherB[2], MotherC[2], MotherD[2]]
DaughterD = [MotherA[3], MotherB[3], MotherC[3], MotherD[3]]

# Function to process the figures
def xorFigures(fig1, fig2):
    result = []
    for line in range(4):
        if fig1[line] == fig2[line]:
            result.append(k)
        else:
            result.append(p)
    return result

# Create the rest of the chart
NieceA = xorFigures(MotherA, MotherB)
NieceB = xorFigures(MotherC, MotherD)
NieceC = xorFigures(DaughterA, DaughterB)
NieceD = xorFigures(DaughterC, DaughterD)
WitnessA = xorFigures(NieceA, NieceB)
WitnessB = xorFigures(NieceC, NieceD)
Judge = xorFigures(WitnessA, WitnessB)
Reconciler = xorFigures(Judge, MotherA)

########## Integrity check ##########
if Judge in InvalidJudges:
    print(fg_red + fatal_error + reset)
    log.write(nl + fatal_error + nl)
######################################

# Arrangements for log file
FigureShield = [MotherA, MotherB, MotherC, MotherD,
                DaughterA, DaughterB, DaughterC, DaughterD,
                NieceA, NieceB, NieceC, NieceD,
                WitnessA, WitnessB, Judge, Reconciler]

FigureHouse = [MotherA, MotherB, MotherC, MotherD,
                DaughterA, DaughterB, DaughterC, DaughterD,
                NieceA, NieceB, NieceC, NieceD,
                WitnessA, WitnessB, Judge, Reconciler]

if Chart == "Agrippa":
    FigureHouse = [MotherA, DaughterA, NieceA,
                   MotherD, DaughterD, NieceD,
                   MotherC, DaughterC, NieceC,
                   MotherB, DaughterB, NieceB,
                   WitnessA, WitnessB, Judge, Reconciler]

# Screen output and color
OutputShield = []
OutputHouse = []

for figure in FigureShield:
    OutputShield.append(colorizeElement(figure))
for figure in FigureHouse:
    OutputHouse.append(colorizePlanet(figure))

########## Chart-drawing functions ##########

def drawShield():
    header_text = "Shield chart generated at " + CurrentTime
    print("-"*72)
    print(header_text.center(72))
    print("-"*72)
    for x in range(4):
        print(s*6 + OutputShield[7][x] + s*5 + OutputShield[6][x] + s*5 + OutputShield[5][x] + s*5 + OutputShield[4][x] + s*5 + OutputShield[3][x] + s*5 + OutputShield[2][x] + s*5 + OutputShield[1][x] + s*5 + OutputShield[0][x])
    print("\n")
    for x in range(4):
        print(s*10 + OutputShield[11][x] + s*13 + OutputShield[10][x] + s*13 + OutputShield[9][x] + s*13 + OutputShield[8][x])
    print("\n")
    for x in range(4):
        print(s*18 + OutputShield[13][x] + s*29 + OutputShield[12][x])
    print("\n")
    for x in range(4):
        print(s*35 + OutputShield[14][x] + s*25 + OutputShield[15][x])

def logShield():
    if Interactive:
        log.write("="*72 + nl)
        log.write("Name  : " + querent + nl)
        log.write("Query : " + query + nl)
    log.write("-"*72 + nl)
    log.write(s*10 + "Shield chart generated at " + CurrentTime + nl)
    log.write("-"*72 + nl)
    for x in range(4):
        log.write(s*6 + DaughterD[x] + s*5 + DaughterC[x] + s*5 + DaughterB[x] + s*5 + DaughterA[x] + s*5 + MotherD[x] + s*5 + MotherC[x] + s*5 + MotherB[x] + s*5 + MotherA[x] + nl)
    log.write(nl)
    for x in range(4):
        log.write(s*10 + NieceD[x] + s*13 + NieceC[x] + s*13 + NieceB[x] + s*13 + NieceA[x] + nl)
    log.write(nl)
    for x in range(4):
        log.write(s*18 + WitnessB[x] + s*29 + WitnessA[x] + nl)
    log.write(nl)
    for x in range(4):
        log.write(s*35 + Judge[x] + s*25 + Reconciler[x] + nl)

def drawHouse():
    header_text = Chart + " house chart generated at " + CurrentTime
    print("-"*72)    
    print(header_text.center(72))
    print("-"*72)
    for x in range(4):
        print(s*13 + OutputHouse[10][x] + s*6 + OutputHouse[9][x] + s*6 + OutputHouse[8][x] + s*11 + " | ")
    print(s*46 + "|")
    for x in range(4):
        print(s*6 + OutputHouse[11][x] + s*29 + OutputHouse[7][x] + s*4 + " | " + s*4 + OutputHouse[13][x] + s*8 + OutputHouse[12][x])
    print(s*46 + "|")
    for x in range(4):
        print(s*6 + OutputHouse[0][x] + s*29 + OutputHouse[6][x] + s*4 + " | " + s*10 + OutputHouse[14][x])
    print(s*46 + "|")
    for x in range(4):
        print(s*6 + OutputHouse[1][x] + s*29 + OutputHouse[5][x] + s*4 + " | " + s*10 + OutputHouse[15][x])
    print(s*46 + "|")
    for x in range(4):
        print(s*13 + OutputHouse[2][x] + s*6 + OutputHouse[3][x] + s*6 + OutputHouse[4][x] + s*11 + " | ")

def logHouse():
    log.write("="*72 + nl)
    if Interactive:
        log.write("Name        : " + querent + nl)
        log.write("Query       : " + query + nl)
    log.write("Significator: House " + str(significator) + nl)
    log.write("-"*72 + nl)
    header_text = Chart + " house chart generated at " + CurrentTime
    log.write(header_text.center(72) + nl)
    log.write("-"*72 + nl)
    for x in range(4):
        log.write(s*13 + FigureHouse[10][x] + s*6 + FigureHouse[9][x] + s*6 + FigureHouse[8][x] + s*11 + " | " + nl)
    log.write(s*46 + "|" + nl)
    for x in range(4):
        log.write(s*6 + FigureHouse[11][x] + s*29 + FigureHouse[7][x] + s*4 + " | " + s*4 + WitnessB[x] + s*8 + WitnessA[x] + nl)
    log.write(s*46 + "|" + nl)
    for x in range(4):
        log.write(s*6 + FigureHouse[0][x] + s*29 + FigureHouse[6][x] + s*4 + " | " + s*10 + Judge[x] + nl)
    log.write(s*46 + "|" + nl)
    for x in range(4):
        log.write(s*6 + FigureHouse[1][x] + s*29 + FigureHouse[5][x] + s*4 + " | " + s*10 + Reconciler[x] + nl)
    log.write(s*46 + "|" + nl)
    for x in range(4):
        log.write(s*13 + FigureHouse[2][x] + s*6 + FigureHouse[3][x] + s*6 + FigureHouse[4][x] + s*11 + " | " + nl)

########## Chart output ##########

if Double or Chart == "Shield":
    drawShield()
    if Logging:
        logShield()

if Double and Chart == "Shield":
    Chart = "Medieval"

if Chart == "Medieval" or Chart == "Agrippa":
    drawHouse()
    if Logging:
        logHouse()

########## Analysis ##########

if Luddite == False:
    print("-"*72)
    print("{}{}Analysis of the chart:{}".format(fg_magenta, underline, reset))
    if Logging:
        log.write("-"*72 + nl)
        log.write("Analysis of the chart:" + nl)
    if MotherA == Rubeus:
        print(fg_yellow + warning_rubeus + reset)
        if Logging:
            log.write(warning_rubeus + nl)
    elif MotherA == Cauda:
        print(fg_yellow + warning_cauda + reset)
        if Logging:
            log.write(warning_cauda + nl)

########## Modes of Perfection ##########

mode_p = 0
CheckHouse = FigureHouse[:12]
CheckCourt = FigureShield[11:]

if Chart != "Shield" and Luddite == False:
    print(fg_blue + "The significator of quesited is House " + str(significator) + reset)
    significator -= 1
    # Occupation
    mode_occupation = False
    if CheckHouse[0] == CheckHouse[significator]:
        mode_occupation = True
        mode_p += 1
        print("{}Occupation found!{}".format(fg_green, reset))
        if Logging:
            log.write("Occupation found!" + nl)
    else:
        print("No occupation.")
    # Conjunction
    # One of the significators moves to a house directly beside the house of the other significator.
    mode_conjunction = False
    if 1 < significator < 11:
        if CheckHouse[0] == CheckHouse[significator-1] or CheckHouse[0] == CheckHouse[significator+1]:
            mode_conjunction = True
            mode_p += 1
            print("{}Conjunction found!{} Querent is the active party.".format(fg_green, reset))
            if Logging:
                log.write("Conjunction found! Querent is the active party." + nl)
        elif CheckHouse[1] == CheckHouse[significator] or CheckHouse[-1] == CheckHouse[significator]:
            mode_conjunction = True
            mode_p += 1
            print("{}Conjunction found!{} Quesited is the active party.".format(fg_green, reset))
            if Logging:
                log.write("Conjunction found! Quesited is the active party." + nl)
        else:
            print("No conjunction.")
    # Mutation
    # The two significators appear next to each other elsewhere in the chart.
    mode_mutation = False
    if mode_conjunction == False:
        for house_num in range(3, 10):
            if CheckHouse[house_num] == CheckHouse[0]:
                if CheckHouse[house_num+1] == CheckHouse[significator] or CheckHouse[house_num-1] == CheckHouse[significator]:
                    print(fg_green + "Mutation found!" + reset + " Please check House " + str(house_num+1) + ".")
                    mode_mutation = True
                    if Logging:
                        log.write("Mutation found! Please check House " + str(house_num+1) + "." + nl)
    if mode_mutation:
        mode_p += 1
    else:
        print("No mutation.")
    # Translation
    # The same figure appears in houses directly beside the houses of the significators.
    if 1 < significator < 11:
        if CheckHouse[1] == CheckHouse[significator-1] or CheckHouse[1] == CheckHouse[significator-1]:
            mode_p += 1
            print("{}Translation found!{} See House 2.".format(fg_green, reset))
            if Logging:
                log.write("Translation found! See House 2." + nl)
        elif CheckHouse[-1] == CheckHouse[significator-1] or CheckHouse[1] == CheckHouse[significator-1]:
            mode_p += 1
            print("{}Translation found!{} See House 12.".format(fg_green, reset))
            if Logging:
                log.write("Translation found! See House 12." + nl)
        else:
            print("No translation.")
    # No perfection
    if mode_p < 1:
        print("{}No perfection found.{}".format(fg_red, reset))
        if Logging:
            log.write("No perfection found." + nl)

########## Close log ##########

if Logging:
    log.close()

#EOF
