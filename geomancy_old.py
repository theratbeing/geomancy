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
chart_override = False
significator = 7
sig_override = False
Luddite = False
Double = False
Text = False
Color = True
Logging = True
log_override = False
log_file = "geomancy.log"

########## Command line arguments ##########

for cmd in sys.argv[1:]:
    if cmd == sys.argv[0]:
        print("[error] Can't write log to self.")
        sys.exit()
    elif cmd == "-m" or cmd == "--medieval":
        Chart = "Medieval"
        chart_override = True
    elif cmd == "-a" or cmd == "--agrippa":
        Chart = "Agrippa"
        chart_override = True
    elif cmd == "-s" or cmd == "--shield":
        Chart = "Shield"
        chart_override = True
    elif cmd == "-i" or cmd == "--interactive":
        Interactive = True
    elif cmd == "-I" or cmd == "--instant":
        Interactive = False
    elif cmd == "-d" or cmd == "--dual":
        Double = True
    elif cmd == "-q" or cmd == "--quiet":
        Logging = False
    elif cmd == "-r" or cmd == "--record":
        Logging = True
    elif cmd == "-c" or cmd == "--color":
        Color = True
    elif cmd == "-n" or cmd == "--no-color":
        Color = False
    elif cmd == "-z" or cmd == "--analyze":
        Luddite = False
    elif cmd == "-l" or cmd == "--luddite":
        Luddite = True
    elif cmd == "-t" or cmd == "--text":
        Text = True
    elif cmd == "-g" or cmd == "--graphic":
        Text = False
    elif cmd[:2] == "s=":
        try:
            if 0 < int(cmd[2:]) < 13:
                significator = int(cmd[2:])
                sig_override = True
            else:
                print("[error] `s=` option requires a number from 1 to 12")
                sys.exit()
        except ValueError:
            print("[error] `s=` option requires a number from 1 to 12")
            sys.exit()
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
fatal_error = "[error] Judge is invalid figure! The script is broken :("
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

Populus = [k, k, k, k] #0000 0
Laetitia = [p, k, k, k] #1000 1
Rubeus = [k, p, k, k] #0100 2
FMinor = [p, p, k, k] #1100 3
Albus = [k, k, p, k] #0010 4
Amissio = [p, k, p, k] #1010 5
Conjunctio = [k, p, p, k] #0110 6
Cauda = [p, p, p, k] #1110 7
Tristitia = [k, k, k, p] #0001 8
Carcer = [p, k, k, p] #1001 9
Acquisitio = [k, p, k, p] #0101 10
Puer = [p, p, k, p] #1101 11
FMajor = [k, k, p, p] #0011 12
Puella = [p, k, p, p] #1011 13
Caput = [k, p, p, p] #0111 14
Via = [p, p, p, p] #1111 15
InvalidJudges = [Laetitia, Tristitia, Puer, Puella, Albus, Rubeus, Caput, Cauda]

FigName = ["Populus", "Laetitia", "Rubeus", "Fortuna Minor",
           "Albus", "Amissio", "Conjunctio", "Cauda Draconis",
           "Tristitia", "Carcer", "Acquisitio", "Puer",
           "Fortuna Major", "Puella", "Caput Draconis", "Via"]

FigMean = ["Crowd, multitude, assembly. Neutral figure.",
           "Happiness, good health.",
           "Passion, vice, hot temper. Unfavorable.",
           "Outside help, outer honor, quick result. Good for endings.",
           "Peace, wisdom, patience. Favorable but weak.",
           "Loss. Bad for wealth but good for love.",
           "Combination, mixed results.",
           "Endings, going away, descending. Unfavorable.",
           "Sorrow, illness. Bad except for land and agriculture.",
           "Restriction, obstacles.",
           "Gain.",
           "Male, power, reckless action. Bad except for love and war.",
           "Success through one's effort. Good for beginnings.",
           "Female, beauty. Good but fickle.",
           "Beginnings, moving in, ascending. Favorable.",
           "Road, journey, change of fortune."]

def id_fig(f):
    if f == Populus:
        return 0
    elif f == Laetitia:
        return 1
    elif f == Rubeus:
        return 2
    elif f == FMinor:
        return 3
    elif f == Albus:
        return 4
    elif f == Amissio:
        return 5
    elif f == Conjunctio:
        return 6
    elif f == Cauda:
        return 7
    elif f == Tristitia:
        return 8
    elif f == Carcer:
        return 9
    elif f == Acquisitio:
        return 10
    elif f == Puer:
        return 11
    elif f == FMajor:
        return 12
    elif f == Puella:
        return 13
    elif f == Caput:
        return 14
    else:
        return 15

def name_fig(f):
    i = id_fig(f)
    return FigName[i]

########## Color correspondences ##########

Fire = [Laetitia, FMinor, Amissio, Cauda]
Air = [Puer, Rubeus, Acquisitio, Conjunctio]
Water = [Via, Populus, Albus, Puella]
Earth = [Carcer, Tristitia, Caput, FMajor]

def colorizeElement(figure):
    result = []
    if figure[0:4] in Fire:
        for line in figure:
            result.append(fg_red + line + reset)
    elif figure[0:4] in Air:
        for line in figure:
            result.append(fg_yellow + line + reset)
    elif figure[0:4] in Water:
        for line in figure:
            result.append(fg_blue + line + reset)
    else:
        for line in figure:
            result.append(fg_green + line + reset)
    return result

def colorizePlanet(figure):
    result = []
    if figure[0:4] == Carcer or figure[0:4] == Tristitia:
        for line in figure:
            result.append(fg_gray + line + reset)
    elif figure[0:4] == Laetitia or figure[0:4] == Acquisitio:
        for line in figure:
            result.append(fg_blue + line + reset)
    elif figure[0:4] == Puer or figure[0:4] == Rubeus:
        for line in figure:
            result.append(fg_red + line + reset)
    elif figure[0:4] == FMajor or figure[0:4] == FMinor:
        for line in figure:
            result.append(fg_yellow + line + reset)
    elif figure[0:4] == Amissio or figure[0:4] == Puella:
        for line in figure:
            result.append(fg_green + line + reset)
    elif figure[0:4] == Conjunctio or figure[0:4] == Albus:
        for line in figure:
            result.append(fg_cyan + line + reset)
    elif figure[0:4] == Via or figure[0:4] == Populus:
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
    
    {2}GENERAL OPTIONS{0}

    -i, --interactive   Ask questions before generating charts.
    -I, --instant       Skip questions and generate chart (default).
    -c, --color         Enable color (default).
    -n, --no-color      Disable color.
    -r, --record        Write output to file (default).
    -q, --quiet         Disable logging.
    -h, --help          Show this help screen.
    file                Name of log file to use.

    {2}CHART OPTIONS{0}

    -g, --graphic       Draw figures (default).
    -t, --text          Show only figure names.
    -S, --shield        Generate shield chart (default).
    -m, --medieval      Generate house chart with medieval arrangement.
    -a, --agrippa       Generate house chart with Pseudo-Agrippa's arrangement.
    -d, --dual          Generate both shield chart and house chart.
    s=n, s=1, s=12      Set the house of quesited to house n (default: 7).
    -z, --analyze       Analyze the chart (default).
    -l, --luddite       Disable chart analysis.

    {2}SHIELD CHART LAYOUT{0}
    
    {5}(D4)  (D3)  {6}(D2)  (D1)  {4}(M4)  (M3)  {3}(M2)  (M1)
       {5}(N4)        {6}(N3)        {4}(N2)        {3}(N1)
             {7}(LW)                    {9}(RW){0}
                         (JD)                 (RC)
    
    M : Mothers                         RW: Right Witness
    D : Daughters                       LW: Left Witness
    N : Nieces                          JD: Judge
                                        RC: Reconciler

    {2}HOUSE CHART LAYOUT{0}

        {4}(11) {5}(10) {3}( 9)
    {6}(12)              ( 8)           {7}(B)   {9}(A)
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

{1} ANALYSIS    {0}

    {3}Please note that chart analysis is experimental and unreliable.{0}

    {2}WAY OF THE POINTS{0}
    
    {4}Way of the Points{0} or {4}Via Puncti{0} is a method to seek hidden influences
    in a situation. Figures with the same top line as the Judge are traced until
    it reaches the top or stops midway. Which {4}triplicity{0} the way ended in shows
    the source of influence.
    
    {3}(*){0} 1st Triplicity (M1, M2, N1): querent's personality and habit.
    {4}(*){0} 2nd Triplicity (M3, M4, N2): events and actions around the querent.
    {6}(*){0} 3rd Triplicity (D1, D2, N3): places frequently visited by querent.
    {5}(*){0} 4th Triplicity (D3, D4, N4): people other than querent.
    
    The figures in each Triplicity are interpreted in the same way as the {4}Court{0}
    (Witnesses and Judge).

    {2}MODES OF PERFECTION{0}
    
    When using a house chart, {4}modes of perfection{0} take precedence over the
    Judge. The modes are:
    
    {5}Occupation :{0} the same figure occupies both houses of querent and quesited.
                 This is the most favorable answer possible.
    {5}Conjunction:{0} one significator moves next to the other significator.
                 This shows which party is (or should be) taking initiative.
    {5}Mutation   :{0} both significators appear together elsewhere in the chart.
                 The event will take place in a roundabout way.
    {5}Translation:{0} figure next to significator makes a conjunction.
                 Help from third party is necessary for success. 
    
""".format(reset, reversal, underline, fg_red, fg_yellow, fg_green, fg_blue, fg_cyan, fg_magenta, fg_gray, fg_white)

########## Interactive mode ##########

if "-h" in sys.argv or "--help" in sys.argv:
    print(Help)
    sys.exit()

if Interactive:
    print(fg_magenta + "="*72)
    print("Geomantic Chart Generator".center(72))
    print("="*72 + reset + "\n")
    querent = input("{}Name  : {}".format(fg_greenbright, reset))
    if log_override == False and len(querent) > 0:
        log_file = querent + ".log"
    query = input("{}Query : {}".format(fg_greenbright, reset))
    if chart_override == False:
        print("\n{}{}Select chart type:\n{}".format(fg_yellow, underline, reset))
        print("1. Shield chart\n2. Medieval house chart\n3. Agrippa house chart\n")
        asktype = input("{}[1/2/3] {}".format(fg_greenbright, reset))
        if asktype == "2":
            Chart = "Medieval"
        elif asktype == "3":
            Chart = "Agrippa"
        else:
            Chart = "Shield"
    if Chart != "Shield" and sig_override == False:
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
        print("12. Imprisonment, hardships, enemies, large animals.\n")
        while True:
            sign = int(input("{}[1-12] {}".format(fg_greenbright, reset)))
            try:
                if 0 < sign < 13:
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
rawShield = [MotherA, MotherB, MotherC, MotherD,
                DaughterA, DaughterB, DaughterC, DaughterD,
                NieceA, NieceB, NieceC, NieceD,
                WitnessA, WitnessB, Judge, Reconciler]

rawHouse = [MotherA, MotherB, MotherC, MotherD,
                DaughterA, DaughterB, DaughterC, DaughterD,
                NieceA, NieceB, NieceC, NieceD,
                WitnessA, WitnessB, Judge, Reconciler]

if Chart == "Agrippa":
    rawHouse = [MotherA, DaughterA, NieceA,
                   MotherD, DaughterD, NieceD,
                   MotherC, DaughterC, NieceC,
                   MotherB, DaughterB, NieceB,
                   WitnessA, WitnessB, Judge, Reconciler]

def addNameFigures(arrg):
    result = []
    for fig in arrg:
        tmp = fig
        tmp.append(name_fig(fig))
        result.append(tmp)
    return result

FigureShield = addNameFigures(rawShield)
FigureHouse = addNameFigures(rawHouse)

# Screen output and color
OutputShield = []
OutputHouse = []

for figure in FigureShield:
    OutputShield.append(colorizeElement(figure))
for figure in FigureHouse:
    OutputHouse.append(colorizePlanet(figure))

########## Chart-drawing functions ##########

ShieldLabel = ["1st Mother  :", "2nd Mother  :", "3rd Mother  :", "4th Mother  :",
               "1st Daughter:", "2nd Daughter:", "3rd Daughter:", "4th Daughter:",
               "1st Niece   :", "2nd Niece   :", "3rd Niece   :", "4th Niece   :",
               "R. Witness  :", "L. Witness  :", "Judge       :", "Reconciler  :"]

def drawShieldText():
    print("-"*72)
    print("Shield chart generated at " + CurrentTime)
    print("-"*72)
    for x in range(16):
        print("{} {}".format(ShieldLabel[x], OutputShield[x][4]))

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

def logShieldText():
    if Logging:
        log.write("-"*72 + nl)
        log.write("Shield chart generated at " + CurrentTime + nl)
        log.write("-"*72 + nl)
        for x in range(16):
            log.write("{} {}{}".format(ShieldLabel[x], FigureShield[x][4], nl))

def logShield():
    if Logging:
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

def drawHouseText():
    print("-"*72)
    print(Chart + " house chart generated at " + CurrentTime)
    print("-"*72)
    for i in range(12):
        if i == 0 or rawHouse[i] == rawHouse[0]:
            print("House {}: {} *".format(str(i+1), OutputHouse[i][4]))
        elif (i+1) == significator or rawHouse[i] == rawHouse[significator-1]:
            print("House {}: {} #".format(str(i+1), OutputHouse[i][4]))
        else:
            print("House {}: {}".format(str(i+1), OutputHouse[i][4]))
    print("R. Witness: " + OutputHouse[12][4])
    print("L. Witness: " + OutputHouse[13][4])
    print("Judge     : " + OutputHouse[14][4])
    print("Reconciler: " + OutputHouse[15][4])

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

def logHouseText():
    if Logging:
        log.write("-"*72 + nl)
        log.write(Chart + " house chart generated at " + CurrentTime + nl)
        log.write("-"*72 + nl)
        for i in range(12):
            if i == 0 or rawHouse[i] == rawHouse[0]:
                log.write("House {}: {} *{}".format(str(i+1), FigureHouse[i][4], nl))
            elif (i+1) == significator or rawHouse[i] == rawHouse[significator-1]:
                log.write("House {}: {} #{}".format(str(i+1), FigureHouse[i][4], nl))
            else:
                log.write("House {}: {}{}".format(str(i+1), FigureHouse[i][4], nl))
        log.write("R. Witness: " + FigureHouse[12][4] + nl)
        log.write("L. Witness: " + FigureHouse[13][4] + nl)
        log.write("Judge     : " + FigureHouse[14][4] + nl)
        log.write("Reconciler: " + FigureHouse[15][4] + nl)

def logHouse():
    if Logging:
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

def prynt(msg):
    if Logging:
        log.write(msg + nl)

if Logging:
    log.write("="*72 + nl)
    if Interactive:
        log.write("Name : {}{}".format(querent, nl))
        log.write("Query: {}{}".format(query, nl))
    if Chart != "Shield":
        log.write("Quesited: House {}{}".format(significator, nl))

if Double or Chart == "Shield":
    if Text:
        drawShieldText()
        logShieldText()
    else:
        drawShield()
        logShield()

if Double and Chart == "Shield":
    Chart = "Medieval"

if Chart == "Medieval" or Chart == "Agrippa":
    if Text:
        drawHouseText()
        logHouseText()
    else:
        drawHouse()
        logHouse()

########## Analysis ##########

if Luddite == False:
    print("-"*72)
    print("{}{}Analysis of the chart:{}".format(fg_magenta, underline, reset))
    prynt("-"*72)
    prynt("Analysis of the chart:")
    if MotherA[0:4] == Rubeus:
        print("\n" + warning_rubeus)
        prynt(nl + warning_rubeus)
    elif MotherA[0:4] == Cauda:
        print("\n" + warning_cauda)
        prynt(nl + warning_cauda)

# Court figures and Way of Points

PointMap = [0,
            0,0,0,0,0,0,0,0,
            0,0,0,0,
            0,0]
flag_1 = False
flag_2 = False
flag_a = False
flag_b = False
flag_c = False

def msg_trp(n):
    message = ["There is no hidden influence in this reading.",
               "{}(1){} Personality and habit.".format(fg_red, reset),
               "{}(2){} Events and actions.".format(fg_yellow, reset),
               "{}(3){} Frequently visited places.".format(fg_blue, reset),
               "{}(4){} Other people".format(fg_green, reset)]
    rmessage = ["There is no hidden influence in this reading.",
               "(1) Personality and habit.",
               "(2) Events and actions.",
               "(3) Frequently visited places.",
               "(4) Other people."]
    print(message[n])
    if Logging:
        log.write(rmessage[n] + nl)

def explain_shield(n):
    i = id_fig(FigureShield[n-1][0:4])
    return "{}:\n{}{}".format(OutputShield[n-1][4], s*4, FigMean[i])

def l_explain_shield(n):
    i = id_fig(FigureShield[n-1][0:4])
    return "{}:{}{}{}".format(FigureShield[n-1][4], nl, s*4, FigMean[i])

def explain_house(n):
    i = id_fig(FigureHouse[n-1][0:4])
    return "{}:\n{}{}".format(OutputHouse[n-1][4], s*4, FigMean[i])

def l_explain_house(n):
    i = id_fig(FigureHouse[n-1][0:4])
    return "{}:{}{}{}".format(FigureHouse[n-1][4], nl, s*4, FigMean[i])

if Luddite == False:
    if Double or Chart == "Shield":
        # Analysis of the Court
        print("\n{}The answer{} to your question is {}".format(fg_magenta, reset, explain_shield(15)))
        prynt("{}The answer to your question is {}".format(nl, l_explain_shield(15)))
        print("\n{}The past{}, or internal factor is {}".format(fg_magenta, reset, explain_shield(13)))
        prynt("{}The past, or internal factor is {}".format(nl, l_explain_shield(13)))
        print("\n{}The future{}, or external factor is {}".format(fg_magenta, reset, explain_shield(14)))
        prynt("{}The future, or external factor is {}".format(nl, l_explain_shield(14)))
        # Way of the Points
        print("\n{}Way of the Points{} leads to:".format(fg_magenta, reset))
        if WitnessA[0] == WitnessB[0]:
            if WitnessA[0] != Judge[0]:
                print("    (none)")
                prynt("    (none)")
                msg_trp(0)
        # First branch
        if WitnessA[0] == Judge[0]:
            print("    {}Right Witness{}".format(fg_yellow, reset))
            prynt("    Right Witness")
            PointMap[13] = 1
            flag_a = True
            if NieceA[0] == Judge[0]:
                print("        {}1st Niece (1){}".format(fg_green, reset))
                prynt("        1st Niece (1)")
                PointMap[9] = 1
                flag_b = True
                if MotherA[0] == Judge[0]:
                    print("            {}1st Mother (1){}".format(fg_cyan, reset))
                    prynt("            1st Mother (1)")
                    PointMap[1] = 1
                    flag_c = True
                if MotherB[0] == Judge[0]:
                    print("            {}2nd Mother (1){}".format(fg_cyan, reset))
                    prynt("            2nd Mother (1)")
                    PointMap[2] = 1
                    flag_c = True
            if NieceB[0] == Judge[0]:
                print("        {}2nd Niece (2){}".format(fg_green, reset))
                prynt("        2nd Niece (2)")
                PointMap[10] = 1
                flag_b = True
                if MotherC[0] == Judge[0]:
                    print("            {}3rd Mother (2){}".format(fg_cyan, reset))
                    prynt("            3rd Mother (2)")
                    PointMap[3] = 1
                    flag_c = True
                if MotherD[0] == Judge[0]:
                    print("            {}4th Mother (2){}".format(fg_cyan, reset))
                    prynt("            4th Mother (2)")
                    PointMap[4] = 1
                    flag_c = True
        # Second branch
        if WitnessB[0] == Judge[0]:
            print("    {}Left Witness{}".format(fg_yellow, reset))
            prynt("    Left Witness")
            PointMap[14] = 1
            flag_a = True
            if NieceC[0] == Judge[0]:
                print("        {}3rd Niece (3){}".format(fg_green, reset))
                prynt("        3rd Niece (3)")
                PointMap[11] = 1
                flag_b = True
                if DaughterA[0] == Judge[0]:
                    print("            {}1st Daughter (3){}".format(fg_cyan, reset))
                    prynt("            1st Daughter (3)")
                    PointMap[5] = 1
                    flag_c = True
                if DaughterB[0] == Judge[0]:
                    print("            {}2nd Daughter (3){}".format(fg_cyan, reset))
                    prynt("            2nd Daughter (3)")
                    PointMap[6] = 1
                    flag_c = True
            if NieceD[0] == Judge[0]:
                print("        {}4th Niece (4){}".format(fg_green, reset))
                prynt("        4th Niece (4)")
                PointMap[12] = 1
                flag_b = True
                if DaughterC[0] == Judge[0]:
                    print("            {}3rd Daughter (4){}".format(fg_cyan, reset))
                    prynt("            3rd Daughter (4)")
                    PointMap[7] = 1
                    flag_c = True
                if DaughterD[0] == Judge[0]:
                    print("            {}4th Daughter (4){}".format(fg_cyan, reset))
                    prynt("            4th Daughter (4)")
                    PointMap[8] = 1
                    flag_c = True
        # Triplicity check
        if flag_c:
            flag_b = False
            flag_a = False
            if PointMap[1] == 1 or PointMap[2] == 1:
                msg_trp(1)
            if PointMap[3] == 1 or PointMap[4] == 1:
                msg_trp(2)
            if PointMap[5] == 1 or PointMap[6] == 1:
                msg_trp(3)
            if PointMap[7] == 1 or PointMap[8] == 1:
                msg_trp(4)
        else:
            flag_2 = True
        if flag_b and flag_2:
            flag_a = False
            if PointMap[9] == 1:
                msg_trp(1)
                
            if PointMap[10] == 1:
                msg_trp(2)
            if PointMap[11] == 1:
                msg_trp(3)
            if PointMap[12] == 1:
                msg_trp(4)
        else:
            flag_1 = True
        if flag_a and flag_1:
            if PointMap[13] == 1:
                print("{}Right Witness{}: the past or internal factors.".format(fg_gray, reset))
                prynt("Right Witness: the past or internal factors.")
            if PointMap[14] == 1:
                print("{}Left Witness{}: the unknown or external factors.".format(fg_cyan, reset))
                prynt("Left Witness: the unknown or external factors.")

########## Modes of Perfection ##########

mode_p = 0
CheckHouse = rawHouse[:12]

if Chart != "Shield" and Luddite == False:
    print("\nThe querent is described by {}".format(explain_house(1)))
    prynt("{}The querent is described by {}".format(nl, l_explain_house(1)))
    print("\nThe quesited is described by {}".format(explain_house(significator)))
    prynt("{}The quesited is described by {}".format(nl, l_explain_house(significator)))
    print("\n{}Modes of Perfection:{}".format(fg_magenta, reset))
    prynt(nl + "Modes of Perfection:")
    print("The significator of quesited is " + fg_blue + "House " + str(significator) + reset)
    significator -= 1
    # Occupation
    if CheckHouse[0] == CheckHouse[significator]:
        mode_p += 1
        print("{}Occupation found!{}".format(fg_green, reset))
        prynt("Occupation found!")
    # Conjunction
    # One of the significators moves to a house directly beside the house of the other significator.
    if 1 < significator < 11:
        if CheckHouse[0] == CheckHouse[significator-1] or CheckHouse[0] == CheckHouse[significator+1]:
            mode_p += 1
            print("{}Conjunction found!{} Querent is the active party.".format(fg_green, reset))
            prynt("Conjunction found! Querent is the active party.")
        elif CheckHouse[1] == CheckHouse[significator] or CheckHouse[-1] == CheckHouse[significator]:
            mode_p += 1
            print("{}Conjunction found!{} Quesited is the active party.".format(fg_green, reset))
            prynt("Conjunction found! Quesited is the active party.")
        # Mutation
        # The two significators appear next to each other elsewhere in the chart.
        for house_num in range(3, 10):
            if CheckHouse[house_num] == CheckHouse[0]:
                if CheckHouse[house_num+1] == CheckHouse[significator] or CheckHouse[house_num-1] == CheckHouse[significator]:
                    print("{}Mutation found!{} Please check House {}.".format(fg_green, reset, str(house_num+1)))
                    mode_p += 1
                    prynt("Mutation found! Please check House {}.".format(str(house_num+1)))
        # Translation
        # The same figure appears in houses directly beside the houses of the significators.
        if CheckHouse[1] == CheckHouse[significator-1] or CheckHouse[1] == CheckHouse[significator-1]:
            mode_p += 1
            print("{}Translation found!{} See House 2.".format(fg_green, reset))
            prynt("Translation found! See House 2.")
        elif CheckHouse[-1] == CheckHouse[significator-1] or CheckHouse[1] == CheckHouse[significator-1]:
            mode_p += 1
            print("{}Translation found!{} See House 12.".format(fg_green, reset))
            prynt("Translation found! See House 12.")
    # No perfection
    if mode_p < 1:
        print("{}No perfection found.{}".format(fg_red, reset))
        prynt("No perfection found.")

########## Close log ##########

if Logging:
    log.close()

#EOF
