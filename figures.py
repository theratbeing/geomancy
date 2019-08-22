#!/usr/bin/python3

# Geomantic Figure Data

import terminal
import random

VIA, POP = "1111", "2222"
LAE, TRI = "1222", "2221"
RUB, ALB = "2122", "2212"
PUA, PUR = "1211", "1121"
ACQ, AMI = "2121", "1212"
CON, CAR = "2112", "1221"
CAP, CAU = "2111", "1112"
MAJ, MIN = "2211", "1122"

FIGURES = (VIA, POP, LAE, TRI, RUB, ALB, PUA, PUR,
           ACQ, AMI, CON, CAR, CAP, CAU, MAJ, MIN)

ELF, ELA = "Fire", "Air"
ELW, ELE = "Water", "Earth"

SAT, JUP = "Saturn", "Jupiter"
MAR, SUN = "Mars", "Sun"
VEN, MER = "Venus", "Mercury"
MON, NNO = "Moon", "North Node"
SNO = "South Node"

Name = {VIA:"Via", POP:"Populus", LAE:"Laetitia", TRI:"Tristitia",
        RUB:"Rubeus", ALB:"Albus", PUA:"Puella", PUR:"Puer",
        ACQ:"Acquisitio", AMI:"Amissio", CON:"Conjunctio", CAR:"Carcer",
        CAP:"Caput Draconis", CAU:"Cauda Draconis", MAJ:"Fortuna Major", MIN:"Fortuna Minor"}

Meaning = {VIA:"", 
           POP:"", 
           LAE:"", 
           TRI:"",
           RUB:"", 
           ALB:"", 
           PUA:"", 
           PUR:"",
           ACQ:"", 
           AMI:"", 
           CON:"", 
           CAR:"",
           CAP:"", 
           CAU:"", 
           MAJ:"", 
           MIN:""}

class Generator:
    
    def process_figures(fig_a, fig_b):
        result = ""
        for i in range(4):
            if fig_a[i] == fig_b[i]: result = result + "2"
            else: result = result + "1"
            
        return result
    
    def generate_figures():
        result = list()
        for i in range(4):
            result.append(random.choice(FIGURES))
        
        for i in range(4):
            result.append(result[0][i] + result[1][i] + result[2][i] + result[3][i])
        
        for i in range(7):
            fi, la = i*2, i*2+1
            result.append(Generator.process_figures(result[fi], result[la]))
        
        result.append(Generator.process_figures(result[0], result[14]))
        
        return result

class Shape:

    Horizontal = {VIA:"----", POP:"::::", LAE:"-:::", TRI:":::-",
                  RUB:":-::", ALB:"::-:", PUA:"-:--", PUR:"--:-",
                  ACQ:":-:-", AMI:"-:-:", CON:":--:", CAR:"-::-",
                  CAP:":---", CAU:"---:", MAJ:"::--", MIN:"--::"}

    s, d = " x ", "x x"

    Vertical = {VIA:[s, s, s, s], POP:[d, d, d, d], LAE:[s, d, d, d], TRI:[d, d, d, s],
                RUB:[d, s, d, d], ALB:[d, d, s, d], PUA:[s, d, s, s], PUR:[s, s, d, s],
                ACQ:[d, s, d, s], AMI:[s, d, s, d], CON:[d, s, s, d], CAR:[s, d, d, s],
                CAP:[d, s, s, s], CAU:[s, s, s, d], MAJ:[d, d, s, s], MIN:[s, s, d, d]}

class Virtue:

    Element = {VIA:ELW, POP:ELW, LAE:ELF, TRI:ELE,
               RUB:ELA, ALB:ELW, PUA:ELW, PUR:ELA,
               ACQ:ELA, AMI:ELF, CON:ELA, CAR:ELE,
               CAP:ELE, CAU:ELF, MAJ:ELE, MIN:ELF}

    Planet = {VIA:MON, POP:MON, LAE:JUP, TRI:SAT,
              RUB:MAR, ALB:MER, PUA:VEN, PUR:MAR,
              ACQ:JUP, AMI:VEN, CON:MER, CAR:SAT,
              CAP:NNO, CAU:SNO, MAJ:SUN, MIN:SUN}

class ColorAssignment:
    
    Element = {ELF:"red", ELA:"yellow", ELW:"blue", ELE:"green"}
    
    Planet = {SAT:"light_black", JUP:"blue", MAR:"red",
              SUN:"yellow", VEN:"green", MER:"cyan",
              MON:"magenta", NNO:"white", SNO:"white"}
    
    All = {**Element, **Planet}

class ColorTable:
    
    def make_table(mode):
        
        if mode == "e": source = Virtue.Element
        else: source = Virtue.Planet
        
        output = dict()
        for code in source:
            value = source[code]
            output[code] = ColorAssignment.All[value]
        
        return output
    
    Element = make_table("e")
    Planet = make_table("p")

class Output:
    
    def make_color(source, mode):
        
        if mode == "e": table = ColorTable.Element
        else: table = ColorTable.Planet
        
        output = dict()
        for code in source:
            text = terminal.ANSI.color(source[code], fg=table[code])
            output[code] = text
        
        return output
    
    def make_vertical_color(source, mode):
        
        if mode == "e": table = ColorTable.Element
        else: table = ColorTable.Planet
        
        output = dict()
        for code in source:
            content = list()
            for line in source[code]:
                text = terminal.ANSI.color(line, fg=table[code])
                content.append(text)
            output[code] = content
        
        return output
    
    NameElement = make_color(Name, "e")
    NamePlanet = make_color(Name, "p")
    HorizontalElement = make_color(Shape.Horizontal, "e")
    HorizontalPlanet = make_color(Shape.Horizontal, "p")
    VerticalElement = make_vertical_color(Shape.Vertical, "e")
    VerticalPlanet = make_vertical_color(Shape.Vertical, "p")
