#!/usr/bin/python3

# Chart processing and output

from figures import Figure, link_figures
from terminal import Reset

court = ['RW', 'LW', 'Ju', 'Rc']

class ShieldChart(object):
    
    def __init__(self, numbers):
        
        self.CompleteFigures = list()
        for item in numbers:
            self.CompleteFigures.append(Figure(item))
        
        self.M1, self.M2, self.M3, self.M4 = self.CompleteFigures[0:4]
        self.D1, self.D2, self.D3, self.D4 = self.CompleteFigures[4:8]
        self.N1, self.N2, self.N3, self.N4 = self.CompleteFigures[8:12]
        self.WR = self.CompleteFigures[12]
        self.WL = self.CompleteFigures[13]
        self.Judge = self.CompleteFigures[14]
        self.Rc = self.CompleteFigures[15]

    def draw(self, cl='e'):
        
        print(f'┏{"━━━━━┯"*7}{"━"*5}┓ ╭{"─"*37}╮')
        
        print(f'┃{8:^5}│{7:^5}│{6:^5}│{5:^5}│{4:^5}│{3:^5}│{2:^5}│{1:^5}┃'\
            f' │{"Mothers":^37}│')
        for i in range(4):
            print(f'┃{self.D4.color[cl]}{self.D4.shape[i]:^5}{Reset}'\
                f'│{self.D3.color[cl]}{self.D3.shape[i]:^5}{Reset}'\
                f'│{self.D2.color[cl]}{self.D2.shape[i]:^5}{Reset}'\
                f'│{self.D1.color[cl]}{self.D1.shape[i]:^5}{Reset}'\
                f'│{self.M4.color[cl]}{self.M4.shape[i]:^5}{Reset}'\
                f'│{self.M3.color[cl]}{self.M3.shape[i]:^5}{Reset}'\
                f'│{self.M2.color[cl]}{self.M2.shape[i]:^5}{Reset}'\
                f'│{self.M1.color[cl]}{self.M1.shape[i]:^5}{Reset}┃', end='')
            cur_fig = self.CompleteFigures[i]
            print(f' │ {i+1:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        print(f'┠{"─────┴─────┼"*3}{"─"*5}┴{"─"*5}┨ │{" "*37}│')
        print(f'┃{12:^11}│{11:^11}│{10:^11}│{9:^11}┃ │{"Daughters":^37}│')
        
        for i in range(4):
            print(f'┃{self.N4.color[cl]}{self.N4.shape[i]:^11}{Reset}'\
                f'│{self.N3.color[cl]}{self.N3.shape[i]:^11}{Reset}'\
                f'│{self.N2.color[cl]}{self.N2.shape[i]:^11}{Reset}'\
                f'│{self.N1.color[cl]}{self.N1.shape[i]:^11}{Reset}┃', end ='')
            cur_fig = self.CompleteFigures[i+4]
            print(f' │ {i+5:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        print(f'┠{"─"*11}┴{"─"*11}┼{"─"*11}┴{"─"*11}┨ │{" "*37}│')
        print(f'┃{"LW":^23}│{"RW":^23}┃ │{"Nieces":^37}│')
        
        for i in range(4):
            print(f'┃{self.WL.color[cl]}{self.WL.shape[i]:^23}{Reset}'\
                f'│{self.WR.color[cl]}{self.WR.shape[i]:^23}{Reset}┃', end='')
            cur_fig = self.CompleteFigures[i+8]
            print(f' │ {i+9:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        print(f'┠{"─"*23}┴{"─"*17}┬{"─"*5}┨ │{" "*37}│')
        print(f'┃{"Ju":>24}{" "*17}│{"Rc":^5}┃ │{"Court":^37}│')
        
        for i in range(4):
            print(f'┃{self.Judge.color[cl]}{self.Judge.shape[i]:>25}{Reset}{" "*16}'\
                f'│{self.Rc.color[cl]}{self.Rc.shape[i]:^5}{Reset}┃', end='')
            cur_fig = self.CompleteFigures[i+12]
            print(f' │ {court[i]:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        print(f'┗{"━"*41}┷{"━"*5}┛ ╰{"─"*37}╯')

class HouseChart(object):
    
    def arrange_agrippa(self, numbers):
        self.Wheel = list()
        self.Wheel[0] = numbers[0]
        self.Wheel[9] = numbers[1]
        self.Wheel[6] = numbers[2]
        self.Wheel[3] = numbers[3]
        self.Wheel[1] = numbers[4]
        self.Wheel[10] = numbers[5]
        self.Wheel[7] = numbers[6]
        self.Wheel[4] = numbers[7]
        self.Wheel[2] = numbers[8]
        self.Wheel[11] = numbers[9]
        self.Wheel[8] = numbers[10]
        self.Wheel[5] = numbers[11]
    
    def __init__(self, numbers, mode='normal'):
        if mode == 'normal': self.Wheel = numbers[0:12]
        else: arrange_agrippa(numbers)
        self.CompleteFigures = link_figures(self.Wheel + numbers[12:16])
        self.H01, self.H02, self.H03 = self.CompleteFigures[0:3]
        self.H04, self.H05, self.H06 = self.CompleteFigures[3:6]
        self.H07, self.H08, self.H09 = self.CompleteFigures[6:9]
        self.H10, self.H11, self.H12 = self.CompleteFigures[9:12]
        self.WR = self.CompleteFigures[12]
        self.WL = self.CompleteFigures[13]
        self.Judge = self.CompleteFigures[14]
        self.Rc = self.CompleteFigures[15]
    
    def draw(self, cl='p'):
        
        print(f'┏{"━━━━━━━┯"*4}{"━"*7}┓ ╭{"─"*37}╮')
        print(f'┃{" "*7}│{"11":^7}│{"10":^7}│{"9":^7}│{" "*7}┃ │{" "*37}│')
        for i in range(4):
            print(f'┃{" "*7}│{self.H11.color[cl]}{self.H11.shape[i]:^7}{Reset}'\
                f'│{self.H10.color[cl]}{self.H10.shape[i]:^7}{Reset}'\
                f'│{self.H09.color[cl]}{self.H09.shape[i]:^7}{Reset}│{" "*7}┃', end='')
            cur_fig = self.CompleteFigures[i]
            print(f' │ {i+1:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        print(f'┠{"─"*7}┼{"─"*7}┴{"─"*7}┴{"─"*7}┼{"─"*7}┨ │{" "*37}│')
        
        print(f'┃{"12":^7}│{"LW":^11} {"RW":^11}│{"8":^7}┃ │{" "*37}│')
        for i in range(4):
            print(f'┃{self.H12.color[cl]}{self.H12.shape[i]:^7}{Reset}'\
                f'│{self.WL.color[cl]}{self.WL.shape[i]:^11}{Reset}'\
                f' {self.WR.color[cl]}{self.WR.shape[i]:^11}{Reset}'\
                f'│{self.H08.color[cl]}{self.H08.shape[i]:^7}{Reset}┃', end='')
            cur_fig = self.CompleteFigures[i+4]
            print(f' │ {i+5:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        print(f'┠{"─"*7}┤{" "*23}├{"─"*7}┨ │{" "*37}│')
        print(f'┃{"1":^7}│{"Judge":^23}│{"7":^7}┃ │{" "*37}│')
        for i in range(4):
            print(f'┃{self.H01.color[cl]}{self.H01.shape[i]:^7}{Reset}│'\
                f'{self.Judge.color[cl]}{self.Judge.shape[i]:^23}{Reset}'\
                f'│{self.H07.color[cl]}{self.H07.shape[i]:^7}{Reset}┃', end='')
            cur_fig = self.CompleteFigures[i+8]
            print(f' │ {i+9:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        print(f'┠{"─"*7}┤{" "*23}├{"─"*7}┨ │{" "*37}│')
        print(f'┃{"2":^7}│{"Reconciler":^23}│{"6":^7}┃ │{" "*37}│')
        for i in range(4):
            print(f'┃{self.H02.color[cl]}{self.H02.shape[i]:^7}{Reset}│'\
                f'{self.Rc.color[cl]}{self.Rc.shape[i]:^23}{Reset}'\
                f'│{self.H06.color[cl]}{self.H06.shape[i]:^7}{Reset}┃', end='')
            cur_fig = self.CompleteFigures[i+12]
            print(f' │ {court[i]:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        print(f'┠{"─"*7}┼{"─"*7}┬{"─"*7}┬{"─"*7}┼{"─"*7}┨ ╰{"─"*37}╯')
        print(f'┃{" "*7}│{"3":^7}│{"4":^7}│{"5":^7}│{" "*7}┃')
        
        for i in range(4):
            print(f'┃{" "*7}│{self.H03.color[cl]}{self.H03.shape[i]:^7}{Reset}'\
                f'│{self.H04.color[cl]}{self.H04.shape[i]:^7}{Reset}'\
                f'│{self.H05.color[cl]}{self.H05.shape[i]:^7}{Reset}│{" "*7}┃')
        
        print(f'┗{"━━━━━━━┷"*4}{"━"*7}┛')
