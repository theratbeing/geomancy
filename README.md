# geomancy.py
Python script to generate charts used in geomancy divination method.

### Features
* Chart analysis: automatically detects modes of perfection and way of points.

* Color output: figures have different color depending on its correspondence and the chart type.

* Interactive mode: the script asks for querent name, the query, and chart type before generating a chart. Each querent will have their own log file. 

* Automatic logging: output will be automatically written to a file.

**Avilable chart types:**

Agrippa/Golden Dawn house chart: Mothers are placed in angular houses, Daughters are placed in succedent houses, Nieces are placed in cadent houses.

Medieval-style simple house chart: figures are placed following the order of their generation.

Traditional shield chart including the Reconciler.

*You can tell the script to only output names of figures.*

### How to use
Launch it from the terminal/command line with `python3 geomancy.py`.

Using `python3 geomancy.py -h` will show you the help screen.

### Dependencies
Color support on Windows requires [colorama](https://pypi.org/project/colorama/) module.

### Screenshots
Text-only chart with simple analysis:

![Text-only analysis](/screenshots/shield_analysis.png)

Interactive mode:

![Interactive mode](/screenshots/interactive_mode.png)

Dual mode:

![Dual mode](/screenshots/double.png)
