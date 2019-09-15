# geomancy.py
Python script to generate charts used in geomancy divination method.

### Features
* Create shield chart and house chart manually or automatically.

* Correspondence tables based on Gerardus of Cremona, H.C. Agrippa, and J.M. Greer.

* Chart analysis: automatically detects modes of perfection and way of points.

* Color output: figures have different color depending on its correspondence and the chart type.


**Avilable chart types:**

Agrippa/Golden Dawn house chart: Mothers are placed in angular houses, Daughters are placed in succedent houses, Nieces are placed in cadent houses.

Traditional house chart: figures are placed following the order of their generation.

Traditional shield chart including the Reconciler.

### How to use
Launch it from the terminal/command line with `python3 geomancy.py`.

### Dependencies
Python 3.6+
Terminal emulator with 16-bit ANSI color support

`geomancy_old.py` only requires Python 3.x with the `--no-color` option.

### Screenshots
Traditional shield chart with elemental colors:

![Shield chart](/screenshots/shield_chart.png)

House chart with Hermetic planetary colors:

![House chart](/screenshots/house_chart.png)

Explanation of figures:

![Explanations](/screenshots/explanations.png)

TODO: Clean up and consolidate the Python scripts
TODO: Write this in Rust (can be compiled to native binary format)
