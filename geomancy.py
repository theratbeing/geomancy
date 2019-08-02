#!/usr/bin/python3
# Simple geomancy shield chart generator

import platform
import sys
import random
from time import strftime

########## User settings ##########
log_file = "geomancy.log"
# p and k are used to create and display the figures. p=1; k=2
p = " x "
k = "x x"
# They can be changed to whatever symbol you like, e.g.
#p = " o "
#k = "o o"
#p = " * "
#k = "* *"
####################################

########## Command line arguments ##########
Color = True
Chart = "Shield"
Double = False
Logging = True
Interactive = False
log_override = False

Options = ["-m", "--medieval", "-a", "--agrippa",
           "-d", "--dual", "-q", "--quiet",
           "-n", "--no-color", "-h", "--help",
           "-i", "--interactive"]

if "-m" in sys.argv or "--medieval" in sys.argv:
    Chart = "Medieval house"
if "-a" in sys.argv or "--agrippa" in sys.argv:
    Chart = "Agrippa house"
if "-d" in sys.argv or "--dual" in sys.argv:
    Double = True
if "-q" in sys.argv or "--quiet" in sys.argv:
    Logging = False
if "-n" in sys.argv or "--no-color" in sys.argv:
    Color = False
if sys.argv[-1] in Options:
    pass
else:
    log_file = sys.argv[-1]
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
warning_rubeus = "[Warning] 1st Mother is Rubeus. Querent has ulterior motives."
warning_cauda = "[Warning] 1st Mother is Cauda Draconis. Querent won't listen to advice."

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

    geomancy.py [options] [file]

{1} DESCRIPTION {0}

    By default, this script generates a geomantic shield chart and logs it into
    a plain text file named {4}geomancy.log{0} along with time stamp. Interactive
    mode will log the chart into a file named after the querent unless the file
    was explicitly mentioned in the command.

    -i, --interactive   Ask user prompt before generating charts.
    -m, --medieval      Generate house chart with medieval arrangement.
    -a, --agrippa       Generate house chart with Pseudo-Agrippa's arrangement.
    -d, --dual          Generate both shield chart and house chart.
    -n, --no-color      Disable color output in terminal.
    -q, --quiet         Disable logging except for errors.
    -h, --help          Show this help screen.
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
    querent = input(fg_greenbright + "Name  : " + reset)
    if log_override == False:
        log_file = querent + ".log"
    query = input(fg_greenbright + "Query : " + reset)
    print(fg_yellow + underline + "\nSelect chart type:\n" + reset)
    print("1. Shield chart\n2. Medieval house chart\n3. Agrippa house chart\n")
    asktype = input(fg_greenbright + "[1/2/3] " + reset)
    if asktype == "2":
        Chart = "Medieval house"
    elif asktype == "3":
        Chart = "Agrippa house"
    else:
        Chart = "Shield"
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

if Chart == "Agrippa house":
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
    header_text = Chart + " chart generated at " + CurrentTime
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
    if Interactive:
        log.write("="*72 + nl)
        log.write("Name  : " + querent + nl)
        log.write("Query : " + query + nl)
    log.write("-"*72 + nl)
    header_text = Chart + " chart generated at " + CurrentTime
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
    Chart = "Medieval house"

if Chart == "Medieval house" or Chart == "Agrippa house":
    drawHouse()
    if Logging:
        logHouse()

########## Warnings for the geomancer ##########

if MotherA == Rubeus:
    print(fg_yellow + warning_rubeus + reset)
    if Logging:
        log.write(warning_rubeus + nl)
elif MotherA == Cauda:
    print(fg_yellow + warning_cauda + reset)
    if Logging:
        log.write(warning_cauda + nl)

if Logging:
    log.close()

#EOF
