# CoverageVisualizer
![license](https://img.shields.io/github/license/Galtvam/CoverageVisualizer) ![pyversion](https://img.shields.io/pypi/pyversions/pytest)

The **CoverageVisualizer** is a **Pytest** plugin able to generate HTML reports about the statement coverage of an application extracted from **Coverage** library data.

## Requirements

To run the CoverageVisualizer pytest plugin you need:
- Python 3.7 or newer
- Pytest 6.0.0 or newer

## Installation

**For now you need to install the plugin locally.**

First you need to clone the repsoitory

```shell
git clone https://github.com/Galtvam/CoverageVisualizer.git
```
Open the project directory and install the pytest plugin as follow:

```shell
pip install .
```
or

```shell
pip install -e .
```

to use in **editable mode** for development purposes

## Running

To run the CoverageVisualizer plugin execute in the target application directory:

```shell
pytest --coverage-visualizer
```

after the execution a directory Output will be created with an index.html file.

### Chosing execution modes

The CoverageVisualizer plugin has two report modes, they are:

- **Project mode:** Generate a coverage report after all the test files have been executed. It shows all the test cases' final coverage percentage and individual file coverage. This mode is the default option.

- **Case mode:** Generates a report based on a test case perspective. The HTML report shows the coverage of all files reached by a specific test case, grouped per test file. The shown coverage considers the relative coverage per test case, therefore if a file is not reached by a test case it is not shown in the report. To use this mode use the following comand:

```shell
pytest --coverage-visualizer --case-mode=True
```

the following report will be genarate an **Output** directory.

## Testing

To run the CoverageVisualizer's tests go to the **/tests** directory and execute:

```shell
pytest
```

the test cases will compare the coverage results of our plugin's observation with the **Coverage** library results. 


**OBS:** For execution purposes the coverage values from **Coverage** lib were stored within the **test_plugin.py** file. This decision was made because of the **pytest.main()** behavior, it shares session information through subsequent calls of the fanction, what breaks the test cases. If the test cases are individually ran, they work well properly.
**OBS 2:** The **Case mode** does not consider **fixtures**, only the executed statements called by the test function. 
