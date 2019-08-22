#!/usr/bin/python3

# Module for terminal display

class ANSI:
    
    reset = "\u001b[0m"
    
    Style = {"bold":"\u001b[1m",
             "underline":"\u001b[4m",
             "reverse":"\u001b[7m",
             "none":""}
    
    Front = {"black":"\u001b[30m", "light_black":"\u001b[30;1m",
             "red":"\u001b[31m", "light_red":"\u001b[31;1m",
             "green":"\u001b[32m", "light_green":"\u001b[32;1m",
             "yellow":"\u001b[33m", "light_yellow":"\u001b[33;1m",
             "blue":"\u001b[34m", "light_blue":"\u001b[34;1m",
             "magenta":"\u001b[35m", "light_magenta":"\u001b[35;1m",
             "cyan":"\u001b[36m", "light_cyan":"\u001b[36;1m",
             "white":"\u001b[37m", "light_white":"\u001b[37;1m",
             "none":""}
    
    Back = {"black":"\u001b[40m", "light_black":"\u001b[40;1m",
             "red":"\u001b[41m", "light_red":"\u001b[41;1m",
             "green":"\u001b[42m", "light_green":"\u001b[42;1m",
             "yellow":"\u001b[43m", "light_yellow":"\u001b[43;1m",
             "blue":"\u001b[44m", "light_blue":"\u001b[44;1m",
             "magenta":"\u001b[45m", "light_magenta":"\u001b[45;1m",
             "cyan":"\u001b[46m", "light_cyan":"\u001b[46;1m",
             "white":"\u001b[47m", "light_white":"\u001b[47;1m",
             "none":""}
    
    def color(text, fg="none", bg="none", st="none"):
        return ANSI.Front[fg] + ANSI.Back[bg] + ANSI.Style[st] + text + ANSI.reset
    
    def color_ext(text, fg=7, bg=0, st="none"):
        esc_fg = "\u001b[38;5;{};m".format(str(fg))
        esc_bg = "\u001b[48;5;{};m".format(str(bg))
        return esc_fg + esc_bg + ANSI.Style[st] + text + ANSI.reset
