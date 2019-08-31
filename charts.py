#!/usr/bin/python3

# Chart processing and output

from figures import Figure, link_figures, figure_info
from terminal import Reset, Fore

court = ['RW', 'LW', 'Ju', 'Rc']

class ShieldChart(object):
    
    def __init__(self, numbers):
        'Make Figure object from a list of numbers and assign them position names in the chart.'
        
        self.CompleteFigures = list()
        for item in numbers:
            self.CompleteFigures.append(Figure(item))
        
        self.M1, self.M2, self.M3, self.M4 = self.CompleteFigures[0:4]
        self.D1, self.D2, self.D3, self.D4 = self.CompleteFigures[4:8]
        self.N1, self.N2, self.N3, self.N4 = self.CompleteFigures[8:12]
        self.WR = self.CompleteFigures[12]
        self.WL = self.CompleteFigures[13]
        self.JU = self.CompleteFigures[14]
        self.RC = self.CompleteFigures[15]
        
        # Via Puncti
        self.VP_SCORE = 0
        self.VP_TABLE = list()
        for i in range(15): self.VP_TABLE.append(False)
        
        # Right witness score +1
        if self.JU.number[0] == self.WR.number[0]:
            self.VP_SCORE += 1
            self.VP_TABLE[0] = True
            
            # Niece 1 score +3
            if self.JU.number[0] == self.N1.number[0]:
                self.VP_SCORE += 3
                self.VP_TABLE[2] = True
                
                # Mother 1
                if self.JU.number[0] == self.M1.number[0]:
                    self.VP_SCORE += 15
                    self.VP_TABLE[6] = True
                
                # Mother 2
                if self.JU.number[0] == self.M2.number[0]:
                    self.VP_SCORE += 15
                    self.VP_TABLE[7] = True
            
            # Niece 2 score +3
            if self.JU.number[0] == self.N2.number[0]:
                self.VP_SCORE += 3
                self.VP_TABLE[3] = True
                
                # Mother 3
                if self.JU.number[0] == self.M3.number[0]:
                    self.VP_SCORE += 15
                    self.VP_TABLE[8] = True
                
                # Mother 4
                if self.JU.number[0] == self.M4.number[0]:
                    self.VP_SCORE += 15
                    self.VP_TABLE[9] = True
        
        # Left witness
        if self.JU.number[0] == self.WL.number[0]:
            self.VP_SCORE += 1
            self.VP_TABLE[1] = True
            
            # Niece 3
            if self.JU.number[0] == self.N3.number[0]:
                self.VP_SCORE += 3
                self.VP_TABLE[4] = True
                
                # Daughter 1
                if self.JU.number[0] == self.D1.number[0]:
                    self.VP_SCORE += 15
                    self.VP_TABLE[10] = True
                
                # Daughter 2
                if self.JU.number[0] == self.D2.number[0]:
                    self.VP_SCORE += 15
                    self.VP_TABLE[11] = True
            
            # Niece 4
            if self.JU.number[0] == self.N4.number[0]:
                self.VP_SCORE += 3
                self.VP_TABLE[5] = True
                
                # Daughter 3
                if self.JU.number[0] == self.D3.number[0]:
                    self.VP_SCORE += 15
                    self.VP_TABLE[12] = True
                
                # Daughter 4
                if self.JU.number[0] == self.D4.number[0]:
                    self.VP_SCORE += 15
                    self.VP_TABLE[13] = True


    def draw(self, cl='element'):
        'Draw a shield chart on the screen'
        
        # Left Window and Right Window printed in parallel
        print(f'┏{"━━━━━┯"*7}{"━"*5}┓╭{"─"*29}╮')
        
        # First row: LW - Mothers and Daughters
        print(f'┃{8:^5}│{7:^5}│{6:^5}│{5:^5}│{4:^5}│{3:^5}│{2:^5}│{1:^5}┃│{"Mothers":^29}│')
        for i in range(4):
            print(f'┃{self.D4.color[cl]}{self.D4.shape[i]:^5}{Reset}'\
                f'│{self.D3.color[cl]}{self.D3.shape[i]:^5}{Reset}'\
                f'│{self.D2.color[cl]}{self.D2.shape[i]:^5}{Reset}'\
                f'│{self.D1.color[cl]}{self.D1.shape[i]:^5}{Reset}'\
                f'│{self.M4.color[cl]}{self.M4.shape[i]:^5}{Reset}'\
                f'│{self.M3.color[cl]}{self.M3.shape[i]:^5}{Reset}'\
                f'│{self.M2.color[cl]}{self.M2.shape[i]:^5}{Reset}'\
                f'│{self.M1.color[cl]}{self.M1.shape[i]:^5}{Reset}┃', end='')
            
            # RW - name and virtues of mothers
            cur_fig = self.CompleteFigures[i]
            print(f'│ {i+1:>2} {cur_fig.color[cl]}{cur_fig.name:<18}{cur_fig.syms}{Reset} │')
        print(f'┠{"─────┴─────┼"*3}{"─"*5}┴{"─"*5}┨│{" "*29}│')
        
        # Second row: LW Nieces
        print(f'┃{12:^11}│{11:^11}│{10:^11}│{9:^11}┃│{"Daughters":^29}│')
        
        for i in range(4):
            print(f'┃{self.N4.color[cl]}{self.N4.shape[i]:^11}{Reset}'\
                f'│{self.N3.color[cl]}{self.N3.shape[i]:^11}{Reset}'\
                f'│{self.N2.color[cl]}{self.N2.shape[i]:^11}{Reset}'\
                f'│{self.N1.color[cl]}{self.N1.shape[i]:^11}{Reset}┃', end ='')
            
            # RW daughters
            cur_fig = self.CompleteFigures[i+4]
            print(f'│ {i+5:>2} {cur_fig.color[cl]}{cur_fig.name:<18}{cur_fig.syms}{Reset} │')
        
        print(f'┠{"─"*11}┴{"─"*11}┼{"─"*11}┴{"─"*11}┨│{" "*29}│')
        
        # Third row: LW witness
        print(f'┃{"LW":^23}│{"RW":^23}┃│{"Nieces":^29}│')
        
        for i in range(4):
            print(f'┃{self.WL.color[cl]}{self.WL.shape[i]:^23}{Reset}'\
                f'│{self.WR.color[cl]}{self.WR.shape[i]:^23}{Reset}┃', end='')
            
            # RW nieces
            cur_fig = self.CompleteFigures[i+8]
            print(f'│ {i+9:>2} {cur_fig.color[cl]}{cur_fig.name:<18}{cur_fig.syms}{Reset} │')
        
        print(f'┠{"─"*23}┴{"─"*17}┬{"─"*5}┨│{" "*29}│')
        
        # Fourth row: LW judge & reconciler
        print(f'┃{"Ju":>24}{" "*17}│{"Rc":^5}┃│{"Court":^29}│')
        
        for i in range(4):
            print(f'┃{self.JU.color[cl]}{self.JU.shape[i]:>25}{Reset}{" "*16}'\
                f'│{self.RC.color[cl]}{self.RC.shape[i]:^5}{Reset}┃', end='')
            
            # RW court figures
            cur_fig = self.CompleteFigures[i+12]
            print(f'│ {court[i]:>2} {cur_fig.color[cl]}{cur_fig.name:<18}{cur_fig.syms}{Reset} │')
        
        print(f'┗{"━"*41}┷{"━"*5}┛╰{"─"*29}╯')
        
        # Bottom panel for Via Puncti
        print(f'╭{"─"*78}╮')
        print(f'│{"Way of the Points":^78}│')
        
        col_1 = [f'│{Fore["black"]} {"Right W.":<14}{Reset}', f'│{" "*15}',
                 f'│{Fore["black"]} {"Left W.":<14}{Reset}', f'│{" "*15}']
        
        if self.VP_TABLE[0]: col_1[0] = '│ Right Witness '
        if self.VP_TABLE[1]: col_1[2] = '│ Left Witness  '
        
        col_2 = [f'{Fore["black"]}  9{Reset} ',
                 f'{Fore["black"]} 10{Reset} ',
                 f'{Fore["black"]} 11{Reset} ',
                 f'{Fore["black"]} 12{Reset} ']
        
        if self.VP_TABLE[2]: col_2[0] = f'{Fore["bright_red"]}  9{Reset} '
        if self.VP_TABLE[3]: col_2[1] = f'{Fore["bright_yellow"]} 10{Reset} '
        if self.VP_TABLE[4]: col_2[2] = f'{Fore["bright_blue"]} 11{Reset} '
        if self.VP_TABLE[5]: col_2[3] = f'{Fore["bright_green"]} 12{Reset} '
        
        col_3 = [f'{Fore["black"]}  2{Reset} ',
                 f'{Fore["black"]}  4{Reset} ',
                 f'{Fore["black"]}  6{Reset} ',
                 f'{Fore["black"]}  8{Reset} ']
        
        if self.VP_TABLE[7]: col_3[0] = f'{Fore["bright_red"]}  2{Reset} '
        if self.VP_TABLE[9]: col_3[1] = f'{Fore["bright_yellow"]}  4{Reset} '
        if self.VP_TABLE[11]: col_3[2] = f'{Fore["bright_blue"]}  6{Reset} '
        if self.VP_TABLE[13]: col_3[3] = f'{Fore["bright_green"]}  8{Reset} '
        
        col_4 = [f'{Fore["black"]}  1{Reset} ',
                 f'{Fore["black"]}  3{Reset} ',
                 f'{Fore["black"]}  5{Reset} ',
                 f'{Fore["black"]}  7{Reset} ']
        
        if self.VP_TABLE[6]: col_4[0] = f'{Fore["bright_red"]}  1{Reset} '
        if self.VP_TABLE[8]: col_4[1] = f'{Fore["bright_yellow"]}  3{Reset} '
        if self.VP_TABLE[10]: col_4[2] = f'{Fore["bright_blue"]}  5{Reset} '
        if self.VP_TABLE[12]: col_4[3] = f'{Fore["bright_green"]}  7{Reset} '
        
        col_5 = [f'{Fore["black"]} 1st Trip.{Reset}{" "*41}│',
                 f'{Fore["black"]} 2nd Trip.{Reset}{" "*41}│',
                 f'{Fore["black"]} 3rd Trip.{Reset}{" "*41}│',
                 f'{Fore["black"]} 4th Trip.{Reset}{" "*41}│']
        
        # If via puncti reaches the end of chart
        if self.VP_TABLE[6] or self.VP_TABLE[7]: col_5[0] = f'{Fore["bright_red"]} 1st Triplicity:{Reset} {"personality and habits":<34}│'
        if self.VP_TABLE[8] or self.VP_TABLE[9]: col_5[1] = f'{Fore["bright_yellow"]} 2nd Triplicity:{Reset} {"events and influences":<34}│'
        if self.VP_TABLE[10] or self.VP_TABLE[11]: col_5[2] = f'{Fore["bright_blue"]} 3rd Triplicity:{Reset} {"frequently visited places":<34}│'
        if self.VP_TABLE[12] or self.VP_TABLE[13]: col_5[3] = f'{Fore["bright_green"]} 4th Triplicity:{Reset} {"other people":<34}│'
        
        # If stops at niece
        if self.VP_TABLE[2] and (self.VP_SCORE < 15): col_5[0] = f'{Fore["bright_red"]} 1st Triplicity:{Reset} {"personality and habits":<34}│'
        if self.VP_TABLE[3] and (self.VP_SCORE < 15): col_5[1] = f'{Fore["bright_yellow"]} 2nd Triplicity:{Reset} {"events and influences":<34}│'
        if self.VP_TABLE[4] and (self.VP_SCORE < 15): col_5[2] = f'{Fore["bright_blue"]} 3rd Triplicity:{Reset} {"frequently visited places":<34}│'
        if self.VP_TABLE[5] and (self.VP_SCORE < 15): col_5[3] = f'{Fore["bright_green"]} 4th Triplicity:{Reset} {"other people":<34}│'
        
        # Merge the collumns
        for i in range(4): print(col_1[i] + col_2[i] + col_3[i] + col_4[i] + col_5[i])
        print(f'╰{"─"*78}╯')
        # End of function
    
    def generate_log_string(self, end='\n'):
        'Generate a string to be written into a plain text file'
        
        output = ''
        template = [f'Chart type : Shield chart',
                    f'-------------------------',
                    f'1st Mother : {self.M1.number} {self.M1.name:<17} 1st Niece  : {self.N1.number} {self.N1.name}',
                    f'2nd Mother : {self.M2.number} {self.M2.name:<17} 2nd Niece  : {self.N2.number} {self.N2.name}',
                    f'3rd Mother : {self.M3.number} {self.M3.name:<17} 3rd Niece  : {self.N3.number} {self.N3.name}',
                    f'4th Mother : {self.M4.number} {self.M4.name:<17} 4th Niece  : {self.N4.number} {self.N4.name}',
                    f'1st Daught.: {self.D1.number} {self.D1.name:<17} R. Witness : {self.WR.number} {self.WR.name}',
                    f'2nd Daught.: {self.D2.number} {self.D2.name:<17} L. Witness : {self.WL.number} {self.WL.name}',
                    f'3rd Daught.: {self.D3.number} {self.D3.name:<17} Judge      : {self.JU.number} {self.JU.name}',
                    f'4th Daught.: {self.D4.number} {self.D4.name:<17} Reconciler : {self.RC.number} {self.RC.name}']
        
        for line in template: output += line + end
        return output
    
    def explain(self):
        
        print('\nThe answer to your question is:')
        figure_info(self.JU)
        
        print('The past is described by:')
        figure_info(self.WR)
        
        print('The future is described by:')
        figure_info(self.WL)
        
        print('The final result is described by:')
        figure_info(self.RC)


class HouseChart(object):
    
    def arrange_agrippa(self, numbers):
        # We will use the Wheel to check for modes of perfection
        self.Mode = 'Agrippa'
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
    
    def __init__(self, numbers, mode='normal', qr=0, qs=6):
        '''
        Create a HouseChart object with complete data of the figures.
        numbers : a list containing 16 strings of geomantic figure's number of points e.g. '1121'
        mode    : select chart arrangement system, 'normal' or 'agrippa'
        qr      : significator house of Querent -1
        qd      : significator house of Quesited -1
        '''
        
        # Select the house arrangement system.
        if mode == 'normal': self.Mode, self.Wheel = 'normal', numbers[0:12]
        else: arrange_agrippa(numbers)
        
        # Make Figure object from number list.
        self.CompleteFigures = link_figures(self.Wheel + numbers[12:16])
        self.H01, self.H02, self.H03 = self.CompleteFigures[0:3]
        self.H04, self.H05, self.H06 = self.CompleteFigures[3:6]
        self.H07, self.H08, self.H09 = self.CompleteFigures[6:9]
        self.H10, self.H11, self.H12 = self.CompleteFigures[9:12]
        self.WR = self.CompleteFigures[12]
        self.WL = self.CompleteFigures[13]
        self.JU = self.CompleteFigures[14]
        self.RC = self.CompleteFigures[15]
    
        # Querent and Quesited are strings from Wheel
        self.Querent, self.QuerentPos = self.Wheel[qr], qr
        self.Quesited, self.QuesitedPos = self.Wheel[qs], qs
        
        # Querent
        if qr == 11: right = 0
        else: right = qr + 1
        self.QuerentRight = self.Wheel[right]
        self.QuerentRightPos = right
        
        if qr == 0: left = 11
        else: left = qr - 1
        self.QuerentLeft = self.Wheel[left]
        self.QuerentLeftPos = left
        
        # Quesited
        if qs == 11: right = 0
        else: right = qs + 1
        self.QuesitedRight = self.Wheel[right]
        self.QuesitedRightPos = right
        
        if qs == 0: left = 11
        else: left = qs - 1
        self.QuesitedLeft = self.Wheel[left]
        self.QuesitedLeftPos = left
        
        # Check modes of perfection
        self.PERFECTION = 0
        
        # 1. Occupation
        if self.Querent == self.Quesited:
            self.OCCUPATION = True
            self.PERFECTION += 1
        else: self.OCCUPATION = False
        
        # 2. Conjunction
        # Querent or Quesited move next to their counterpart
        self.CONJUNCTION, self.CONJUNCTION_ACTIVE, self.CONJUNCTION_PASSIVE = False, False, False
        
        if (self.QuerentRight == self.Quesited) or (self.QuerentLeft == self.Quesited):
            self.CONJUNCTION, self.CONJUNCTION_PASSIVE = True, True
        
        if (self.QuesitedRight == self.Querent) or (self.QuesitedLeft == self.Querent):
            self.CONJUNCTION, self.CONJUNCTION_ACTIVE = True, True
        
        if self.CONJUNCTION: self.PERFECTION += 1
        
        # Show who approaches whom
        if self.CONJUNCTION_ACTIVE and self.CONJUNCTION_PASSIVE and True:
            self.CONJUNCTION_SOURCE, self.CONJUNCTION_ACTIVE, self.CONJUNCTION_PASSIVE = 'both sides', False, False
        
        if self.CONJUNCTION_ACTIVE: self.CONJUNCTION_SOURCE = "querent's side"
        if self.CONJUNCTION_PASSIVE: self.CONJUNCTION_SOURCE = "quesited's side"
        
        # 3. Mutation
        # Querent and quesited meet somewhere in the chart
        self.MUTATION = False
        # Skip certain positions
        ignore = (self.QuerentPos, self.QuerentLeftPos, self.QuerentRightPos, self.QuesitedPos, self.QuesitedLeftPos, self.QuesitedRightPos)
        
        for pos in range(11):
            if pos in ignore:
                pass
            
            else:
                if (self.Wheel[pos] == self.Querent) and (self.Wheel[pos+1] == self.Quesited):
                    self.MUTATION, self.MUTATION_POS = True, pos+1
                
        if self.MUTATION: self.PERFECTION += 1
        
        # 4. Translation
        # Querent and quesited have the same neighbor
        self.TRANSLATION, self.TRANSLATION_LEFT, self.TRANSLATION_RIGHT = False, False, False
        self.TRANSLATION_POS = ''
        
        houses = list()
        
        if (self.QuerentLeft == self.QuesitedLeft) or (self.QuerentLeft == self.QuesitedRight):
            self.TRANSLATION = True
            houses.append(self.QuerentLeftPos+1)
        
        if (self.QuerentRight == self.QuesitedLeft) or (self.QuerentRight == self.QuesitedRight):
            self.TRANSLATION = True
            houses.append(self.QuerentRightPos+1)
            
        if (self.QuesitedLeft == self.QuerentLeft) or (self.QuesitedLeft == self.QuerentRight):
            self.TRANSLATION = True
            houses.append(self.QuesitedLeftPos+1)
        
        if (self.QuesitedRight == self.QuerentLeft) or (self.QuesitedRight == self.QuerentRight):
            self.TRANSLATION = True
            houses.append(self.QuesitedRightPos+1)
        
        houses.sort()
        for pos in range(len(houses)):
            # see if we're at the last item
            if pos == (len(houses) - 1):
                self.TRANSLATION_POS += f'{houses[pos]}.'
            
            # not last item
            else:
                self.TRANSLATION_POS += f'{houses[pos]}, '
        
        if self.TRANSLATION: self.PERFECTION += 1
    
    def draw(self, cl='planet'):
        
        # Place the strings into a list before printing them to screen.
        output = list()
        
        # Left window (figures and houses)
        window_l = list()
        window_l.append(f'┏{"━━━━━━━┯"*4}{"━"*7}┓')
        
        # First row
        window_l.append(f'┃{" "*7}│{"11":^7}│{"10":^7}│{"9":^7}│{" "*7}┃')
        for i in range(4):
            window_l.append(f'┃{" "*7}│{self.H11.color[cl]}{self.H11.shape[i]:^7}{Reset}'\
                f'│{self.H10.color[cl]}{self.H10.shape[i]:^7}{Reset}'\
                f'│{self.H09.color[cl]}{self.H09.shape[i]:^7}{Reset}│{" "*7}┃')
        window_l.append(f'┠{"─"*7}┼{"─"*7}┴{"─"*7}┴{"─"*7}┼{"─"*7}┨')
        
        # Second row
        window_l.append(f'┃{"12":^7}│{"LW":>9} {"RW":>7}{" "*6}│{"8":^7}┃')
        for i in range(4):
            window_l.append(f'┃{self.H12.color[cl]}{self.H12.shape[i]:^7}{Reset}'\
                f'│{self.WL.color[cl]}{self.WL.shape[i]:>9}{Reset}'\
                f' {self.WR.color[cl]}{self.WR.shape[i]:>7}{Reset}{" "*6}'\
                f'│{self.H08.color[cl]}{self.H08.shape[i]:^7}{Reset}┃')
        window_l.append(f'┠{"─"*7}┤{" "*23}├{"─"*7}┨')
        
        # Third row
        window_l.append(f'┃{"1":^7}│{"Judge":^23}│{"7":^7}┃')
        for i in range(4):
            window_l.append(f'┃{self.H01.color[cl]}{self.H01.shape[i]:^7}{Reset}│'\
                f'{self.JU.color[cl]}{self.JU.shape[i]:^23}{Reset}'\
                f'│{self.H07.color[cl]}{self.H07.shape[i]:^7}{Reset}┃')
        window_l.append(f'┠{"─"*7}┤{" "*23}├{"─"*7}┨')
        
        # Fourth row
        window_l.append(f'┃{"2":^7}│{"Reconciler":^23}│{"6":^7}┃')
        for i in range(4):
            window_l.append(f'┃{self.H02.color[cl]}{self.H02.shape[i]:^7}{Reset}│'\
                f'{self.RC.color[cl]}{self.RC.shape[i]:^23}{Reset}'\
                f'│{self.H06.color[cl]}{self.H06.shape[i]:^7}{Reset}┃')
        window_l.append(f'┠{"─"*7}┼{"─"*7}┬{"─"*7}┬{"─"*7}┼{"─"*7}┨')
        
        # Fifth row
        window_l.append(f'┃{" "*7}│{"3":^7}│{"4":^7}│{"5":^7}│{" "*7}┃')
        for i in range(4):
            window_l.append(f'┃{" "*7}│{self.H03.color[cl]}{self.H03.shape[i]:^7}{Reset}'\
                f'│{self.H04.color[cl]}{self.H04.shape[i]:^7}{Reset}'\
                f'│{self.H05.color[cl]}{self.H05.shape[i]:^7}{Reset}│{" "*7}┃')
        window_l.append(f'┗{"━━━━━━━┷"*4}{"━"*7}┛')
        
        # Top window
        window_r = list()
        window_r.append(f' ╭{"─"*37}╮')
        window_r.append(f' │ {self.QuerentPos+1:>2} Significator of querent {" "*9}│')
        window_r.append(f' │ {self.QuesitedPos+1:>2} Significator of quesited {" "*8}│')
        
        # Middle right window
        window_r.append(f' ├{"─"*37}┤')
        window_r.append(f' │{"Houses":^37}│')
        
        for i in range(12):
            cur_fig = self.CompleteFigures[i]
            window_r.append(f' │ {i+1:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        window_r.append(f' ├{"─"*37}┤')
        window_r.append(f' │{"Court":^37}│')
        
        for i in range(4):
            cur_fig = self.CompleteFigures[i+12]
            window_r.append(f' │ {court[i]:>2} {cur_fig.color[cl]}{cur_fig.name:<16}{cur_fig.symbols}{Reset} │')
        
        # Bottom right window
        window_r.append(f' ├{"─"*37}┤')
        window_r.append(f' │{"Modes of Perfection":^37}│')
        
        
        if self.OCCUPATION: window_r.append(f' │{Fore["bright_green"]}{"✓ Occupation":<37}{Reset}│')
        else: window_r.append(f' │{Fore["black"]}{"  Occupation":<37}{Reset}│')
        
        if self.CONJUNCTION: window_r.append(f' │{Fore["bright_green"]}✓ Conjunction from {self.CONJUNCTION_SOURCE:<18}{Reset}│')
        else: window_r.append(f' │{Fore["black"]}{"  Conjunction":<37}{Reset}│')
        
        if self.MUTATION: window_r.append(f' │{Fore["bright_green"]}✓ Mutation in house {self.MUTATION_POS:<17}{Reset}│')
        else: window_r.append(f' │{Fore["black"]}{"  Mutation":<37}{Reset}│')
        
        if self.TRANSLATION: window_r.append(f' │{Fore["bright_green"]}✓ Translation in houses {self.TRANSLATION_POS:<13}{Reset}│')
        else: window_r.append(f' │{Fore["black"]}{"  Translation":<37}{Reset}│')
        
        if self.PERFECTION > 0: window_r.append(f' │{Fore["bright_blue"]}{"✓ This chart perfects":<37}{Reset}│')
        else: window_r.append(f' │{Fore["red"]}{"  No perfection found":<37}{Reset}│')
        
        window_r.append(f' ╰{"─"*37}╯')
        
        # Combine the windows
        output = window_l
        for line in range(len(window_r)):
            output[line] += window_r[line]
        
        # Print the result
        for line in output:
            print(line)
    
    def generate_log_string(self, end='\n'):
        'Generates a string to be written into plain text file'
        
        output = ''
        template = [f'Chart type: House chart/{self.Mode}',
                    f'-------------------------------',
                    f'House  1: {self.H01.number} {self.H01.name:<17} R. Witness: {self.WR.number} {self.WR.name}',
                    f'House  2: {self.H02.number} {self.H02.name:<17} L. Witness: {self.WL.number} {self.WL.name}',
                    f'House  3: {self.H03.number} {self.H03.name:<17} Judge     : {self.JU.number} {self.JU.name}',
                    f'House  4: {self.H04.number} {self.H04.name:<17} Reconciler: {self.RC.number} {self.RC.name}',
                    f'House  5: {self.H05.number} {self.H05.name}',
                    f'House  6: {self.H06.number} {self.H06.name:<17} Querent in house {self.QuerentPos+1}',
                    f'House  7: {self.H07.number} {self.H07.name:<17} Quesited in house {self.QuesitedPos+1}',
                    f'House  8: {self.H08.number} {self.H08.name}',
                    f'House  9: {self.H09.number} {self.H09.name}',
                    f'House 10: {self.H10.number} {self.H10.name}',
                    f'House 11: {self.H11.number} {self.H11.name}',
                    f'House 12: {self.H12.number} {self.H12.name}',
                    ' ',
                    f'Modes of Perfection:']
        
        if self.PERFECTION == 0: template.append('None')
        if self.OCCUPATION: template.append('Translation')
        if self.CONJUNCTION: template.append('Conjunction')
        if self.MUTATION: template.append(f'Mutation in house {self.MUTATION_POS}')
        if self.TRANSLATION: template.append(f'Translation in houses {self.TRANSLATION_POS}')
        
        for line in template: output += line + end
        return output
    
    def explain(self):
        
        if self.PERFECTION > 0:
            print('\nThe answer to your question is "yes".')
        
        else:
            print('\nThe answer to your question is "no".')
        
        print('The querent is described by:')
        figure_info(Figure(self.Querent))
        
        print('The quesited is described by:')
        figure_info(Figure(self.Quesited))
        
