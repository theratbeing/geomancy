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
######################################################

# List of figures unfit to be Judge
Laetitia = [p, k, k, k]
Tristitia = Laetitia.reverse()
Puer = [p, p, k, p]
Puella = Puer.reverse()
Albus = [k, k, p, k]
Rubeus = Albus.reverse()
Caput = [k, p, p, p]
Cauda = Caput.reverse()
InvalidJudges = [Laetitia, Tristitia, Puer, Puella, Albus, Rubeus, Caput, Cauda]

s = " " # whitespace character for layout
# Platform-dependent new line for log file
nl = "\n"
if platform.system() == "Windows":
    nl = "\r\n"

Help = """NAME
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
    -q, --quiet         Disable logging except for errors.
    -h, --help          Show this help screen.

HOUSE CHART LAYOUT

        (11) (10) ( 9)          |   (B)   (A)
    (12)              ( 8)      |      (C)
    ( 1)              ( 7)      |      (D)
    ( 2)              ( 6)      |
        ( 3) ( 4) ( 5)          |

    1-12: Astrological houses        C: Judge
    A   : Right Witness              D: Reconciler
    B   : Left Witness
    
    Medieval method of geomancy placess the figures in the astrological houses
    in order of their generation. Mothers go to Houses 1-4, Daughters go to
    Houses 5-8, and Nieces go to Houses 9-12.
    
    In the 'Fourth Book of Occult Philosophy' Pseudo-Agrippa gives a different
    method of placement. The Mothers are placed in angular houses (1, 10, 7, 4)
    the Daughters in succedent houses (2, 11, 8, 5); and the Nieces are placed
    in cadent houses (3, 12, 9, 6). This is the method used by Hermetic Order
    of Golden Dawn."""

# Command line arguments
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
if "-h" in sys.argv or "--help" in sys.argv:
    print(Help)
    quit()

######################################
########## Interactive mode ##########
######################################

if "-i" in sys.argv or "--interactive" in sys.argv:
    Interactive = True
    print("=========================\nGeomantic Chart Generator\n=========================\n")
    querent = input("Name  : ")
    query = input("Query : ")
    print("\nSelect chart type (default is 1):")
    print("1 Shield chart")
    print("2 Medieval house chart")
    print("3 Agrippa house chart")
    asktype = input("# ")
    if asktype == "2":
        Chart = "Medieval house"
    elif asktype == "3":
        Chart = "Agrippa house"
    else:
        Chart = "Shield"
    confirm_log = input("Write to log file? Default is y [y/n] ")
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

# Arrangement for house chart
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
        print(DaughterD[x] + s*5 + DaughterC[x] + s*5 + DaughterB[x] + s*5 + DaughterA[x] + s*5 + MotherD[x] + s*5 + MotherC[x] + s*5 + MotherB[x] + s*5 + MotherA[x])
    print("\n")
    for x in range(4):
        print(s*4 + NieceD[x] + s*13 + NieceC[x] + s*13 + NieceB[x] + s*13 + NieceA[x])
    print("\n")
    for x in range(4):
        print(s*12 + WitnessB[x] + s*29 + WitnessA[x])
    print("\n")
    for x in range(4):
        print(s*29 + Judge[x] + s*25 + Reconciler[x])

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
        print(s*7 + House11[x] + s*6 + House10[x] + s*6 + House9[x] + s*11 + " | " + s*4 + WitnessB[x] + s*8 + WitnessA[x])
    print(s*40 + "|")
    for x in range(4):
        print(House12[x] + s*29 + House8[x] + s*4 + " | " + s*10 + Judge[x])
    print(s*40 + "|")
    for x in range(4):
        print(House1[x] + s*29 + House7[x] + s*4 + " | " + s*10 + Reconciler[x])
    print(s*40 + "|")
    for x in range(4):
        print(House2[x] + s*29 + House6[x] + s*4 + " | ")
    print(s*40 + "|")
    for x in range(4):
        print(s*7 + House3[x] + s*6 + House4[x] + s*6 + House5[x] + s*11 + " | ")

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

# This error should be impossible to trigger.
if Judge in InvalidJudges:
    print("[ERROR] Judge is invalid figure! This script is broken :(")
    log = open(log_file, "a+")
    log.write(nl + "[ERROR] Judge is invalid figure! This script is broken :(" + nl)
    log.close()

# You should be able to memorize these warnings.
#if MotherA == Rubeus:
#    print("[Warning] 1st Mother is Rubeus. Querent has ulterior motives.")
#elif MotherA == Cauda:
#    print("[Warning] 1st Mother is Cauda Draconis. Querent won't listen to advice.")

#EOF
