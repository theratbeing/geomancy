#!/usr/bin/python3

# Geomantic Figure Data

from random import choice
from terminal import esc_16b, Reset, Style
import settings

VIA, POP = '1111', '2222'
LAE, TRI = '1222', '2221'
RUB, ALB = '2122', '2212'
PUA, PUR = '1211', '1121'
ACQ, AMI = '2121', '1212'
CON, CAR = '2112', '1221'
CAP, CAU = '2111', '1112'
MAJ, MIN = '2211', '1122'

FIGURES = (VIA, POP, LAE, TRI, RUB, ALB, PUA, PUR,
           ACQ, AMI, CON, CAR, CAP, CAU, MAJ, MIN)

ELF, ELA, ELW, ELE = '🜂 Fire', '🜁 Air', '🜄 Water', '🜃 Earth'

SAT, JUP, MAR = '♄ Saturn', '♃ Jupiter', '♂ Mars'
SUN, VEN, MER = '☉ Sun', '♀ Venus', '☿ Mercury'
MON, NNO, SNO = '☽ Moon', '☊ North Node', '☋ South Node'

ZARI, ZTAU, ZGEM = '♈ Aries', '♉ Taurus', '♊ Gemini'
ZCAN, ZLEO, ZVIR = '♋ Cancer', '♌ Leo', '♍ Virgo'
ZLIB, ZSCO, ZSAG = '♎ Libra', '♏ Scorpio', '♐ Sagittarius'
ZCAP, ZAQU, ZPIS = '♑ Capricorn', '♒ Aquarius', '♓ Pisces'

Name = {VIA:'Via', POP:'Populus', LAE:'Laetitia', TRI:'Tristitia',
        RUB:'Rubeus', ALB:'Albus', PUA:'Puella', PUR:'Puer',
        ACQ:'Acquisitio', AMI:'Amissio', CON:'Conjunctio', CAR:'Carcer',
        CAP:'Caput Draconis', CAU:'Cauda Draconis', MAJ:'Fortuna Major', MIN:'Fortuna Minor'}

Meaning = {VIA:'Road, journey, change of fortune.',
           POP:'Crowd, multitude, assembly. Neutral figure.',
           LAE:'Happiness and good health.',
           TRI:'Sorrow, illness. Bad except for land and agriculture.',
           RUB:'Passion, vice, hot temper. Unfavorable. In 1st position it means the querent is dishonest.',
           ALB:'Peace, wisdom, patience. Favorable but weak.',
           PUA:'Female, beauty. Good figure but fickle.',
           PUR:'Male, power, reckless action. Bad except for love and war.',
           ACQ:'Gain.',
           AMI:'Loss. Bad for wealth but good for love.',
           CON:'Combination, mixed results.',
           CAR:'Restriction, obstacle.',
           CAP:'Beginnings, ascending movement. Favorable.',
           CAU:"Endings, descending movement. Unfavorable. In 1st position it means the querent won't change his/her view.",
           MAJ:"Success through one's own effort. Good for beginnings.",
           MIN:'Outside help, outer honor, quick result. Good for endings.'}

s, d = ' ● ', '● ●'

Shape = {VIA:(s, s, s, s), POP:(d, d, d, d), LAE:(s, d, d, d), TRI:(d, d, d, s),
         RUB:(d, s, d, d), ALB:(d, d, s, d), PUA:(s, d, s, s), PUR:(s, s, d, s),
         ACQ:(d, s, d, s), AMI:(s, d, s, d), CON:(d, s, s, d), CAR:(s, d, d, s),
         CAP:(d, s, s, s), CAU:(s, s, s, d), MAJ:(d, d, s, s), MIN:(s, s, d, d)}

class Virtue:
    
    Element = {VIA:ELW, POP:ELW, LAE:ELA, TRI:ELE,
               RUB:ELF, ALB:ELW, PUA:ELW, PUR:ELA,
               ACQ:ELA, AMI:ELF, CON:ELA, CAR:ELE,
               CAP:ELE, CAU:ELF, MAJ:ELE, MIN:ELF}
    
    if settings.ELEMENT_SYSTEM == 'modern':
        Element[RUB], Element[LAE] = ELA, ELF

    Planet = {VIA:MON, POP:MON, LAE:JUP, TRI:SAT,
              RUB:MAR, ALB:MER, PUA:VEN, PUR:MAR,
              ACQ:JUP, AMI:VEN, CON:MER, CAR:SAT,
              CAP:NNO, CAU:SNO, MAJ:SUN, MIN:SUN}
    
    Zodi_G = {VIA:ZLEO, POP:ZCAP, LAE:ZTAU, TRI:ZSCO,
              RUB:ZGEM, ALB:ZCAN, PUA:ZLIB, PUR:ZGEM,
              ACQ:ZARI, AMI:ZSCO, CON:ZVIR, CAR:ZPIS,
              CAP:ZVIR, CAU:ZSAG, MAJ:ZAQU, MIN:ZTAU}
    
    Zodi_A = {VIA:ZCAN, POP:ZCAN, LAE:ZPIS, TRI:ZAQU,
              RUB:ZSCO, ALB:ZGEM, PUA:ZLIB, PUR:ZARI,
              ACQ:ZSAG, AMI:ZTAU, CON:ZVIR, CAR:ZCAP,
              CAP:ZVIR, CAU:ZVIR, MAJ:ZLEO, MIN:ZLEO}
    
    if settings.ZODIAC_SYSTEM == 'agrippa':
        Zodiac = Zodi_A
    else: Zodiac = Zodi_G
    
    Mansion = {VIA:"10. Al-Jab'hah", POP:'20. An-Na‘āʾam',
               LAE:'4. Ad-Dabarān', TRI:'19. Ash-Shawlah',
               RUB:'6. Al-Han‘ah', ALB:'8. An-Nathrah, 9. Aṭ-Ṭarf',
               PUA:'5. Al-Haq‘ah', PUR:'15. Al-Ghafr, 16. Az-Zubānā',
               ACQ:'1. An-Naṭḥ, 2. Al-Buṭayn', AMI:'17. Al-Iklīl',
               CON:'14. As-Simāk', CAR:'28. Ar-Rashāʾ',
               CAP:'13. Al-‘Awwāʾ', CAU:'21. Al-Baldah',
               MAJ:'3. Ath-Thurayyā',
               MIN:'25. Al-ʾAkhbiyyah, 26. Al-Muqdim, 27. Al-Muʾkhar'}

class Color:
    
    'Color correspondences (Golden Dawn Queen Scale) in ANSI 256 color mode. See terminal.py for the palette'
    
    WHI_N, WHI_B, WHI_D = esc_16b(7), esc_16b(15), esc_16b(250)
    BLA_N, BLA_B, BLA_D = esc_16b(0), esc_16b(8), esc_16b(232)
    RED_N, RED_B, RED_D = esc_16b(1), esc_16b(9), esc_16b(52)
    YEL_N, YEL_B, YEL_D = esc_16b(3), esc_16b(11), esc_16b(214)
    BLU_N, BLU_B, BLU_D = esc_16b(4), esc_16b(12), esc_16b(17)
    ORA_N, ORA_B, ORA_D = esc_16b(202), esc_16b(208), esc_16b(130)
    GRN_N, GRN_B, GRN_D = esc_16b(2), esc_16b(10), esc_16b(22)
    PUR_N, PUR_B, PUR_D = esc_16b(128), esc_16b(200), esc_16b(56)

    Element = {ELF:RED_N, ELA:YEL_N, ELW:BLU_N, ELE:GRN_N}
    
    Planet = {SAT:BLA_B, JUP:BLU_B, MAR:RED_B,
              SUN:YEL_B, VEN:GRN_B, MER:ORA_B,
              MON:PUR_N, NNO:WHI_N, SNO:WHI_N}
    
    Zodiac = {ZARI:RED_N, ZLEO:RED_N, ZSAG:RED_N,
              ZLIB:YEL_N, ZAQU:YEL_N, ZGEM:YEL_N,
              ZCAN:BLU_N, ZSCO:BLU_N, ZPIS:BLU_N,
              ZCAP:GRN_N, ZTAU:GRN_N, ZVIR:GRN_N}
    
class Figure(object):
    
    def __init__(self, number):
        self.number = number
        self.name = Name[number]
        self.meaning = Meaning[number]
        self.shape = Shape[number]
        self.element = Virtue.Element[number]
        self.planet = Virtue.Planet[number]
        self.zodiac = Virtue.Zodiac[number]
        self.mansion = Virtue.Mansion[number]
        self.color = {'element':Color.Element[self.element],
                      'planet':Color.Planet[self.planet],
                      'zodiac':Color.Zodiac[self.zodiac]}
        self.symbols = f'{self.color["element"]}{self.element[0:3]} '\
            f'{self.color["planet"]}{self.planet[0:5]} '\
            f'{self.color["zodiac"]}{self.zodiac[0:5]}{Reset}'
        self.syms = f'{self.color["element"]}{self.element[0]} '\
            f'{self.color["planet"]}{self.planet[0]} '\
            f'{self.color["zodiac"]}{self.zodiac[0]}{Reset}'
    
    def info(self, expert=False):
        ' expects a Figure object to work'
        zod_a, zod_g = Virtue.Zodi_A[self.number], Virtue.Zodi_G[self.number]
    
        if expert:
            print(f'{" "*7}{Style["underline"]}{self.name} ({self.number}){Reset}')
            print(f' {self.shape[0]:^5} Element: {self.color["element"]}{self.element:<8}{Reset}')
            print(f' {self.shape[1]:^5} Planet : {self.color["planet"]}{self.planet}{Reset}')
            print(f' {self.shape[2]:^5} Zodiac : {Color.Zodiac[zod_g]}{zod_g}{Reset} (Gerardus), {Color.Zodiac[zod_a]}{zod_a}{Reset} (Agrippa)')
            print(f' {self.shape[3]:^5} Mansion: {self.mansion}')
            print(f'{" "*7}Meaning: {self.meaning}\n')
    
        else:
            print(f' {self.shape[0]:^5} {Style["underline"]}{self.name} ({self.number}){Reset}')
            print(f' {self.shape[1]:^5} Element: {self.color["element"]}{self.element:<8}{Reset}')
            print(f' {self.shape[2]:^5} Planet : {self.color["planet"]}{self.planet}{Reset}')
            print(f' {self.shape[3]:^5} Meaning: {self.meaning}\n')

def link_figures(iterable):
    result = list()
    for item in iterable:
        result.append(Figure(item))
    return result

def process_figures(fig_a, fig_b):
    result = ''
    for i in range(4):
        if fig_a[i] is fig_b[i]: result = result + '2'
        else: result = result + '1'
    return result
    
def generate_figures(mothers=list()):
    result = list()
    
    if len(mothers) == 4:
        for i in range(4): result.append(mothers[i])
    else:
        for i in range(4): result.append(choice(FIGURES))
    
    for i in range(4):
        result.append(result[0][i] + result[1][i] + result[2][i] + result[3][i])
    
    for i in range(7):
        fi, la = i*2, i*2+1
        result.append(process_figures(result[fi], result[la]))

    result.append(process_figures(result[0], result[14]))
    
    return result
    
def generate_complete_figures():
    numbers = generate_figures()
    result = list()
    for n in numbers:
        result.append(Figure(n))
    return result
