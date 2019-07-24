# geomancy.py
Python3 script to generate geomantic divination charts.

## How to use
Launch it from the terminal/command line with `python3 geomancy.py`.

Using `python3 geomancy.py -h` will show you the help screen (or just read the source code -- it's short!).

## Features
* Interactive mode

(Added in 2019-07-24) The script asks for querent name, the query, and chart type before generating a chart.

* Traditional shield chart including the Reconciler

* Medieval-style simple house chart

Figures are placed following the order of their generation.

* Agrippa/Golden Dawn house chart

Mothers are placed in angular houses, Daughters are placed in succedent houses, Nieces are placed in cadent houses.

* Automatic logging

Output will be automatically written to a file specified in `log_file`.

Note: this script does not provide interpretation for the reading.
