#!/usr/bin/python3

import figures
import charts
import settings

conjunction = ('1112', '2222', '1222', '2212')

NumberList = figures.generate_figures()

#Chart = charts.ShieldChart(NumberList)
#Chart.draw(settings.SHIELD_COLOR_SCHEME)

Chart = charts.HouseChart(NumberList)
Chart.draw(settings.HOUSE_COLOR_SCHEME)

#figures.figure_info(Chart.WR)
