#!/usr/bin/python3
# Simple geomancy shield chart generator

import platform
import sys
import random
from time import strftime

######################################################
########## These strings are safe to modify ##########
######################################################
log_file = "geomancy.log"
# p and k are used to display the figures. p=1; k=2
p = " x "
k = "x x"
# They can be changed to whatever symbol you like, e.g.
#p = " o "
#k = "o o"
######################################################
# Be careful modifying things beyond this point!

#######################################
########## Geomantic Figures ##########
#######################################
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

#####################################
########## Correspondences ##########
#####################################
Fire = [Laetitia, FMinor, Amissio, Cauda]
Air = [Puer, Rubeus, Acquisitio, Conjunctio]
Water = [Via, Populus, Albus, Puella]
Earth = [Carcer, Tristitia, Caput, FMajor]

######################################
######### Special Characters #########
######################################
Color = True

fg_white = "\u001b[37m"
fg_red = "\u001b[31m"
fg_redbright = "\u001b[31;1m"
fg_yellow = "\u001b[33m"
fg_yellowbright = "\u001b[33;1m"
fg_green = "\u001b[32m"
fg_greenbright = "\u001b[32;1m"
fg_cyan = "\u001b[36m"
fg_blue = "\u001b[34m"
fg_magenta = "\u001b[35m"
fg_gray = "\u001b[30;1m"
bg_red = "\u001b[41m"
bg_yellow = "\u001b[43m"
bg_blue = "\u001b[44m"
bg_green = "\u001b[42m"
bold = "\u001b[1m"
underline = "\u001b[4m"
reversal = "\u001b[7m"
reset = "\u001b[0m"

s = " " # whitespace character for layout
nl = "\n" # newline
FatalError = "[ERROR] Judge is invalid figure! The script is broken :("

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
            result.append(fg_yellowbright + line + reset)
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
##############################
######### Help Text ##########
##############################
Help = """ NAME

    geomancy.py         Python script to generate geomantic charts.

 SYNOPSIS

    geomancy.py [option1] [option2] [option3]

 DESCRIPTION

    By default, this script generates a geomantic shield chart and logs it into
    a plain text file named 'geomancy.log' along with time stamp.

    -i, --interactive   Ask user prompt before generating charts.
    -m, --medieval      Generate house chart with medieval arrangement.
    -a, --agrippa       Generate house chart with Pseudo-Agrippa's arrangement.
    -d, --dual          Generate both shield chart and house chart.
    -n, --no-color      Disable color output in terminal.
    -q, --quiet         Disable logging except for errors.
    -h, --help          Show this help screen.

    HOUSE CHART LAYOUT

        (11) (10) ( 9)                (B)   (A)
    (12)              ( 8)               (C)
    ( 1)              ( 7)               (D)
    ( 2)              ( 6)
        ( 3) ( 4) ( 5)

    1-12: Astrological houses           C: Judge
    A   : Right Witness                 D: Reconciler
    B   : Left Witness
    
    Medieval method of geomancy placess the figures in the astrological houses
    in order of their generation. Mothers go to Houses 1-4, Daughters go to
    Houses 5-8, and Nieces go to Houses 9-12.
    
    In the 'Fourth Book of Occult Philosophy' Pseudo-Agrippa gives a different
    method of placement. The Mothers are placed in angular houses (1, 10, 7, 4)
    the Daughters in succedent houses (2, 11, 8, 5); and the Nieces are placed
    in cadent houses (3, 12, 9, 6). This is the method used by Hermetic Order
    of Golden Dawn.

    COLOR SCHEME

    Planet          Color                          Element         Color
    Saturn          Gray                           Fire            Red
    Jupiter         Blue                           Air             Yellow
    Mars            Red                            Water           Blue
    Sun             Yellow                         Earth           Green
    Venus           Green
    Mercury         Cyan
    Moon            Magenta
    Lunar nodes     Gray
"""

ColorHelp = """\u001b[7m NAME       \u001b[0m

    geomancy.py         Python script to generate geomantic charts.

\u001b[7m SYNOPSIS   \u001b[0m

    geomancy.py [option1] [option2] [option3]

\u001b[7m DESCRIPTION \u001b[0m

    By default, this script generates a geomantic shield chart and logs it into
    a plain text file named \u001b[33mgeomancy.log\u001b[0m along with time stamp.

    -i, --interactive   Ask user prompt before generating charts.
    -m, --medieval      Generate house chart with medieval arrangement.
    -a, --agrippa       Generate house chart with Pseudo-Agrippa's arrangement.
    -d, --dual          Generate both shield chart and house chart.
    -n, --no-color      Disable color output in terminal.
    -q, --quiet         Disable logging except for errors.
    -h, --help          Show this help screen.

    \u001b[4mHOUSE CHART LAYOUT\u001b[0m

        \u001b[33m(11)\u001b[0m \u001b[32m(10)\u001b[0m \u001b[31m( 9)\u001b[0m                (B)   (A)
    \u001b[34m(12)              ( 8)\u001b[0m               (C)
    \u001b[31m( 1)\u001b[0m              \u001b[33m( 7)\u001b[0m               (D)
    \u001b[32m( 2)\u001b[0m              \u001b[32m( 6)\u001b[0m
        \u001b[33m( 3)\u001b[0m \u001b[34m( 4)\u001b[0m \u001b[31m( 5)\u001b[0m

    1-12: Astrological houses           C: Judge
    A   : Right Witness                 D: Reconciler
    B   : Left Witness
    
    Medieval method of geomancy placess the figures in the astrological houses
    in order of their generation. Mothers go to Houses 1-4, Daughters go to
    Houses 5-8, and Nieces go to Houses 9-12.
    
    In the \u001b[33mFourth Book of Occult Philosophy\u001b[0m, Pseudo-Agrippa gives a different
    method of placement. The Mothers are placed in angular houses (1, 10, 7, 4)
    the Daughters in succedent houses (2, 11, 8, 5); and the Nieces are placed
    in cadent houses (3, 12, 9, 6). This is the method used by \u001b[33mHermetic Order
    of Golden Dawn.\u001b[0m

    \u001b[4mCOLOR SCHEME\u001b[0m

    \u001b[7mPlanet          Color                          Element         Color       \u001b[0m
    \u001b[30;1mSaturn          Gray                           \u001b[31mFire            Red\u001b[0m
    \u001b[34mJupiter         Blue                           \u001b[33mAir             Yellow\u001b[0m
    \u001b[31mMars            Red                            \u001b[34mWater           Blue\u001b[0m
    \u001b[33;1mSun             Yellow                         \u001b[32mEarth           Green\u001b[0m
    \u001b[32mVenus           Green\u001b[0m
    \u001b[36mMercury         Cyan\u001b[0m
    \u001b[35mMoon            Magenta\u001b[0m
    Lunar nodes     White
"""
###########################################
########## Windows-only settings ##########
###########################################
if platform.system() == "Windows":
    Color = False
    nl = "\r\n"

############################################
########## Command line arguments ##########
############################################
Chart = "Shield"
Double = False
Logging = True
Interactive = False
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
if "-h" in sys.argv or "--help" in sys.argv:
    if Color:
        print(ColorHelp)
    else:
        print(Help)
    quit()

######################################
########## Interactive mode ##########
######################################

if "-i" in sys.argv or "--interactive" in sys.argv:
    Interactive = True
    print("=========================\nGeomantic Chart Generator\n=========================\n")
    if Color:
        querent = input(fg_greenbright + "Name  : " + reset)
        query = input(fg_greenbright + "Query : " + reset)
        print(fg_yellow + "\nSelect chart type:\n--------------------------" + reset)
        print("1 Shield chart\n2 Medieval house chart\n3 Agrippa house chart\n")
        asktype = input(fg_greenbright + "[1/2/3] " + reset)
    else:
        querent = input("Name  : ")
        query = input("Query : ")
        print("\nSelect chart type:\n--------------------------")
        print("1 Shield chart\n2 Medieval house chart\n3 Agrippa house chart\n")
        asktype = input("[1/2/3] ")
    if asktype == "2":
        Chart = "Medieval house"
    elif asktype == "3":
        Chart = "Agrippa house"
    else:
        Chart = "Shield"
    if Color:
        confirm_log = input("Write to log? " + fg_greenbright + "[Y/n] " + reset)
    else:
        confirm_log = input("Write to log? [Y/n] ")
    if confirm_log == "n" or confirm_log == "N":
        Logging = False
    else:
        Logging = True
    
##################################################
########## Chart processing starts here ##########
##################################################

CurrentTime = strftime("%Y-%m-%d (%a) %H:%M:%S")
RawData = []
for x in range(16):
    RawData.append(random.choice([p, k]))

MotherA = RawData[0:4]
MotherB = RawData[4:8]
MotherC = RawData[8:12]
MotherD = RawData[12:16]

Transpose = []
for x in range(4):
    Transpose.append(MotherA[x])
    Transpose.append(MotherB[x])
    Transpose.append(MotherC[x])
    Transpose.append(MotherD[x])

DaughterA = Transpose[0:4]
DaughterB = Transpose[4:8]
DaughterC = Transpose[8:12]
DaughterD = Transpose[12:16]

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

# This error should be impossible to trigger.
if Judge in InvalidJudges:
    if Color:
        print(bg_red + FatalError + reset)
    else:
        print(FatalError)
    log = open(log_file, "a+")
    log.write(nl + FatalError + nl)
    log.close()

# Copy figures for screen output and color
PMotherA = MotherA
PMotherB = MotherB
PMotherC = MotherC
PMotherD = MotherD
PDaughterA = DaughterA
PDaughterB = DaughterB
PDaughterC = DaughterC
PDaughterD = DaughterD
PNieceA = NieceA
PNieceB = NieceB
PNieceC = NieceC
PNieceD = NieceD
PWitnessA = WitnessA
PWitnessB = WitnessA
PJudge = Judge
PReconciler = Reconciler

# Arrangement for house chart in log file
House1 = MotherA
House2 = MotherB
House3 = MotherC
House4 = MotherD
House5 = DaughterA
House6 = DaughterB
House7 = DaughterC
House8 = DaughterD
House9 = NieceA
House10 = NieceB
House11 = NieceC
House12 = NieceD
# Screen output for house chart
PHouse1 = MotherA
PHouse2 = MotherB
PHouse3 = MotherC
PHouse4 = MotherD
PHouse5 = DaughterA
PHouse6 = DaughterB
PHouse7 = DaughterC
PHouse8 = DaughterD
PHouse9 = NieceA
PHouse10 = NieceB
PHouse11 = NieceC
PHouse12 = NieceD
PPWitnessA = WitnessA
PPWitnessB = WitnessB
PPJudge = Judge
PPReconciler = Reconciler

if Chart == "Agrippa house":
    House1 = MotherA #angular
    House2 = DaughterA #succedent
    House3 = NieceA #cadent
    House4 = MotherD #a
    House5 = DaughterD #s
    House6 = NieceD #c
    House7 = MotherC #a
    House8 = DaughterC #s
    House9 = NieceC #c
    House10 = MotherB #a
    House11 = DaughterB #s
    House12 = NieceB #c
    PHouse1 = MotherA #screen output
    PHouse2 = DaughterA #succedent
    PHouse3 = NieceA #cadent
    PHouse4 = MotherD #a
    PHouse5 = DaughterD #s
    PHouse6 = NieceD #c
    PHouse7 = MotherC #a
    PHouse8 = DaughterC #s
    PHouse9 = NieceC #c
    PHouse10 = MotherB #a
    PHouse11 = DaughterB #s
    PHouse12 = NieceB #c

########################################
########## Colorize the chart ##########
########################################
if Color:
    PMotherA = colorizeElement(MotherA)
    PMotherB = colorizeElement(MotherB)
    PMotherC = colorizeElement(MotherC)
    PMotherD = colorizeElement(MotherD)
    PDaughterA = colorizeElement(DaughterA)
    PDaughterB = colorizeElement(DaughterB)
    PDaughterC = colorizeElement(DaughterC)
    PDaughterD = colorizeElement(DaughterD)
    PNieceA = colorizeElement(NieceA)
    PNieceB = colorizeElement(NieceB)
    PNieceC = colorizeElement(NieceC)
    PNieceD = colorizeElement(NieceD)
    PWitnessA = colorizeElement(WitnessA)
    PWitnessB = colorizeElement(WitnessA)
    PJudge = colorizeElement(Judge)
    PReconciler = colorizeElement(Reconciler)
    PHouse1 = colorizePlanet(MotherA)
    PHouse2 = colorizePlanet(MotherB)
    PHouse3 = colorizePlanet(MotherC)
    PHouse4 = colorizePlanet(MotherD)
    PHouse5 = colorizePlanet(DaughterA)
    PHouse6 = colorizePlanet(DaughterB)
    PHouse7 = colorizePlanet(DaughterC)
    PHouse8 = colorizePlanet(DaughterD)
    PHouse9 = colorizePlanet(NieceA)
    PHouse10 = colorizePlanet(NieceB)
    PHouse11 = colorizePlanet(NieceC)
    PHouse12 = colorizePlanet(NieceD)
    PPWitnessA = colorizePlanet(WitnessA)
    PPWitnessB = colorizePlanet(WitnessB)
    PPJudge = colorizePlanet(Judge)
    PPReconciler = colorizePlanet(Reconciler)
    if Chart == "Agrippa house":
        PHouse1 = colorizePlanet(MotherA)
        PHouse2 = colorizePlanet(DaughterA)
        PHouse3 = colorizePlanet(NieceA) #cadent
        PHouse4 = colorizePlanet(MotherD) #a
        PHouse5 = colorizePlanet(DaughterD) #s
        PHouse6 = colorizePlanet(NieceD) #c
        PHouse7 = colorizePlanet(MotherC) #a
        PHouse8 = colorizePlanet(DaughterC) #s
        PHouse9 = colorizePlanet(NieceC) #c
        PHouse10 = colorizePlanet(MotherB) #a
        PHouse11 = colorizePlanet(DaughterB) #s
        PHouse12 = colorizePlanet(NieceB) #c

# Shield chart design (rough sketch):
#
# DA4 DA3 DA2 DA1 MO4 MO3 MO2 MO1
# ---NI4---NI3------NI2-----NI1
# ------WI1--------------WI2
# --------------JUD-----------REC

def drawShield():
    print("="*60)
    print("Shield chart generated at " + CurrentTime)
    print("="*60)
    for x in range(4):
        print(PDaughterD[x] + s*5 + PDaughterC[x] + s*5 + PDaughterB[x] + s*5 + PDaughterA[x] + s*5 + PMotherD[x] + s*5 + PMotherC[x] + s*5 + PMotherB[x] + s*5 + PMotherA[x])
    print("\n")
    for x in range(4):
        print(s*4 + PNieceD[x] + s*13 + PNieceC[x] + s*13 + PNieceB[x] + s*13 + PNieceA[x])
    print("\n")
    for x in range(4):
        print(s*12 + PWitnessB[x] + s*29 + PWitnessA[x])
    print("\n")
    for x in range(4):
        print(s*29 + PJudge[x] + s*25 + PReconciler[x])

def logShield():
    log = open(log_file, "a+")
    if Interactive:
        log.write("="*60 + nl)
        log.write("Name  : " + querent + nl)
        log.write("Query : " + query + nl)
    log.write("="*60 + nl)
    log.write("Shield chart generated at " + CurrentTime + nl)
    log.write("="*60 + nl)
    for x in range(4):
        log.write(DaughterD[x] + s*5 + DaughterC[x] + s*5 + DaughterB[x] + s*5 + DaughterA[x] + s*5 + MotherD[x] + s*5 + MotherC[x] + s*5 + MotherB[x] + s*5 + MotherA[x] + nl)
    log.write(nl)
    for x in range(4):
        log.write(s*4 + NieceD[x] + s*13 + NieceC[x] + s*13 + NieceB[x] + s*13 + NieceA[x] + nl)
    log.write(nl)
    for x in range(4):
        log.write(s*12 + WitnessB[x] + s*29 + WitnessA[x] + nl)
    log.write(nl)
    for x in range(4):
        log.write(s*29 + Judge[x] + s*25 + Reconciler[x] + nl)
    log.close()

# House chart design
#
#---#NI3#NI2#NI1#---#|#WI2#---#WI1#
#NI4#---#---#---#DA4#|#---#JUD#---#
#MO1#---#---#---#DA3#|#-----------#
#MO2#---#---#---#DA2#|#---#REC#---#
#---#MO3#MO4#DA1#---#|

def drawHouse():
    print("="*60)
    print(Chart + " chart generated at " + CurrentTime)
    print("="*60)
    for x in range(4):
        print(s*7 + PHouse11[x] + s*6 + PHouse10[x] + s*6 + PHouse9[x] + s*11 + " | " + s*4 + PPWitnessB[x] + s*8 + PPWitnessA[x])
    print(s*40 + "|")
    for x in range(4):
        print(PHouse12[x] + s*29 + PHouse8[x] + s*4 + " | " + s*10 + PPJudge[x])
    print(s*40 + "|")
    for x in range(4):
        print(PHouse1[x] + s*29 + PHouse7[x] + s*4 + " | " + s*10 + PPReconciler[x])
    print(s*40 + "|")
    for x in range(4):
        print(PHouse2[x] + s*29 + PHouse6[x] + s*4 + " | ")
    print(s*40 + "|")
    for x in range(4):
        print(s*7 + PHouse3[x] + s*6 + PHouse4[x] + s*6 + PHouse5[x] + s*11 + " | ")

def logHouse():
    log = open(log_file, "a+")
    if Interactive:
        log.write("="*60 + nl)
        log.write("Name  : " + querent + nl)
        log.write("Query : " + query + nl)
    log.write("="*60 + nl)
    log.write(Chart + " chart generated at " + CurrentTime + nl)
    log.write("="*60 + nl)
    for x in range(4):
        log.write(s*7 + House11[x] + s*6 + House10[x] + s*6 + House9[x] + s*11 + " | " + s*4 + WitnessB[x] + s*8 + WitnessA[x] + nl)
    log.write(s*40 + "|" + nl)
    for x in range(4):
        log.write(House12[x] + s*29 + House8[x] + s*4 + " | " + s*10 + Judge[x] + nl)
    log.write(s*40 + "|" + nl)
    for x in range(4):
        log.write(House1[x] + s*29 + House7[x] + s*4 + " | " + s*10 + Reconciler[x] + nl)
    log.write(s*40 + "|" + nl)
    for x in range(4):
        log.write(House2[x] + s*29 + House6[x] + s*4 + " | " + nl)
    log.write(s*40 + "|" + nl)
    for x in range(4):
        log.write(s*7 + House3[x] + s*6 + House4[x] + s*6 + House5[x] + s*11 + " | " + nl)
    log.close()

###################################
########## Script output ##########
###################################

if Double:
    drawShield()
    if Logging:
        logShield()
    if Chart == "Shield":
        Chart = "Medieval house"
    drawHouse()
    if Logging:
        logHouse()
else:
    if Chart == "Medieval house" or Chart == "Agrippa house":
        drawHouse()
        if Logging:
            logHouse()
    else:
        drawShield()
        if Logging:
            logShield()

# You should be able to memorize these warnings.
#if MotherA == Rubeus:
#    print("[Warning] 1st Mother is Rubeus. Querent has ulterior motives.")
#elif MotherA == Cauda:
#    print("[Warning] 1st Mother is Cauda Draconis. Querent won't listen to advice.")

#EOF
