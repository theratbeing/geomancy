#!/usr/bin/python3

import figures
import charts

NumberList = figures.generate_figures()

Chart = charts.ShieldChart(NumberList)
Chart.draw()
