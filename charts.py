#!/usr/bin/python3

# Chart processing and output

import figures
import terminal

class ShieldChart(object):
    
    def __init__(self, numbers):
        
        self.Figure = list()
        for item in numbers:
            self.Figure.append(figures.Figure(item))
        
        self.M1, self.M2, self.M3, self.M4 = self.Figure[0:4]
        self.D1, self.D2, self.D3, self.D4 = self.Figure[4:8]
        self.N1, self.N2, self.N3, self.N4 = self.Figure[8:12]
        self.WR = self.Figure[12]
        self.WL = self.Figure[13]
        self.Judge = self.Figure[14]
        self.Rec = self.Figure[15]

    def draw(self, cl='e'):
        
        print('┏', end='')
        for i in range(7):
            print('━'*5 + '┯', end='')
        print('━'*5 + '┓')
        
        print(f'┃{8:^5}│{7:^5}│{6:^5}│{5:^5}│{4:^5}│{3:^5}│{2:^5}│{1:^5}┃ Mothers:')
        for i in range(4):
            print(f'┃{self.D4.color[cl]}{self.D4.shape[i]:^5}{terminal.Reset}', end='')
            print(f'│{self.D3.color[cl]}{self.D3.shape[i]:^5}{terminal.Reset}', end='')
            print(f'│{self.D2.color[cl]}{self.D2.shape[i]:^5}{terminal.Reset}', end='')
            print(f'│{self.D1.color[cl]}{self.D1.shape[i]:^5}{terminal.Reset}', end='')
            print(f'│{self.M4.color[cl]}{self.M4.shape[i]:^5}{terminal.Reset}', end='')
            print(f'│{self.M3.color[cl]}{self.M3.shape[i]:^5}{terminal.Reset}', end='')
            print(f'│{self.M2.color[cl]}{self.M2.shape[i]:^5}{terminal.Reset}', end='')
            print(f'│{self.M1.color[cl]}{self.M1.shape[i]:^5}{terminal.Reset}┃', end='')
            cur_fig = self.Figure[i]
            print(f' {i+1:>2} {cur_fig.color[cl]}{cur_fig.name}{terminal.Reset}')
        
        print('┠', end='')
        for i in range(3):
            print('─'*5 + '┴', end='')
            print('─'*5 + '┼', end='')
        print('─'*5 + '┴' + '─'*5 + '┨')
        print(f'┃{12:^11}│{11:^11}│{10:^11}│{9:^11}┃ Daughters:')
        
        for i in range(4):
            print(f'┃{self.N4.color[cl]}{self.N4.shape[i]:^11}{terminal.Reset}', end='')
            print(f'│{self.N3.color[cl]}{self.N3.shape[i]:^11}{terminal.Reset}', end='')
            print(f'│{self.N2.color[cl]}{self.N2.shape[i]:^11}{terminal.Reset}', end='')
            print(f'│{self.N1.color[cl]}{self.N1.shape[i]:^11}{terminal.Reset}┃', end ='')
            cur_fig = self.Figure[i+4]
            print(f' {i+5:>2} {cur_fig.color[cl]}{cur_fig.name}{terminal.Reset}')
        
        print('┠' + '─'*11 + '┴' + '─'*11 + '┼' + '─'*11 + '┴' + '─'*11 + '┨')
        print(f'┃{14:^23}│{13:^23}┃ Nieces:')
        
        for i in range(4):
            print(f'┃{self.WL.color[cl]}{self.WL.shape[i]:^23}{terminal.Reset}', end='')
            print(f'│{self.WR.color[cl]}{self.WR.shape[i]:^23}{terminal.Reset}┃', end='')
            cur_fig = self.Figure[i+8]
            print(f' {i+9:>2} {cur_fig.color[cl]}{cur_fig.name}{terminal.Reset}')
        
        print('┠' + '─'*23 + '┴' + '─'*17 + '┬' + '─'*5 + '┨')
        print(f'┃{15:>25}{" "*16}│{16:^5}┃ Court:')
        
        for i in range(4):
            print(f'┃{self.Judge.color[cl]}{self.Judge.shape[i]:>25}{terminal.Reset}', end='')
            print(' '*16, end='')
            print(f'│{self.Rec.color[cl]}{self.Rec.shape[i]:^5}{terminal.Reset}┃', end='')
            cur_fig = self.Figure[i+12]
            print(f' {i+13:>2} {cur_fig.color[cl]}{cur_fig.name}{terminal.Reset}')
        
        print('┗' + '━'*41 + '┷' + '━'*5 + '┛')

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
        self.H01, self.H02, self.H03 = figures.link_figures(self.Wheel[0:3])
        self.H04, self.H05, self.H06 = figures.link_figures(self.Wheel[3:6])
        self.H07, self.H08, self.H09 = figures.link_figures(self.Wheel[6:9])
        self.H10, self.H11, self.H12 = figures.link_figures(self.Wheel[9:12])
        self.WitnessR = figures.Figure(numbers[12])
        self.WitnessL = figures.Figure(numbers[13])
        self.Judge = figures.Figure(numbers[14])
        self.Rec = figures.Figure(numbers[15])
