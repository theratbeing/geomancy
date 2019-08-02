# geomancy.py
Python3 script to generate geomantic divination charts.

### Features
* Chart analysis: automatically detects modes of perfection (2019-08-02).

* Color output: figures have different color depending on its correspondence and the chart type. (2019-07-31)

* Interactive mode: the script asks for querent name, the query, and chart type before generating a chart (2019-07-24). Each querent will have their own log file (2019-08-01). 

* Automatic logging: output will be automatically written to a file.

* Agrippa/Golden Dawn house chart: Mothers are placed in angular houses, Daughters are placed in succedent houses, Nieces are placed in cadent houses.

* Medieval-style simple house chart: figures are placed following the order of their generation.

* Traditional shield chart including the Reconciler.

*Note: this script does not provide interpretation for the reading.*

### How to use
Launch it from the terminal/command line with `python3 geomancy.py`.

Using `python3 geomancy.py -h` will show you the help screen.

### Dependencies
Color support on Windows requires [colorama](https://pypi.org/project/colorama/) module.

### Screenshots
The help screen:

![Help screen](/screenshots/help.png)

Interactive mode:

![Interactive mode](/screenshots/interactive_mode.png)

Dual mode:

![Dual mode](/screenshots/double.png)
