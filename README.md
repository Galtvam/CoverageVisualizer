# CoverageVisualizer
![license](https://img.shields.io/github/license/Galtvam/CoverageVisualizer) ![pyversion](https://img.shields.io/pypi/pyversions/pytest)

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
