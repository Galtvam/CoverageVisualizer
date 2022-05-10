__author__ = ['Galtvam', 'vgss', 'fekete1']

__license__ = 'MIT'
__version__ = '0.0.0'

import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='coverage-visualizer',
    version=__version__,
    author=__author__,
    description='Pytest plugin to visualize the coverage of your tests',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Galtvam/CoverageVisualizer',
    packages=['coverage_visualizer'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Pytest'
    ],
    entry_points={
        'pytest11': ['coverage_visualizer = coverage_visualizer.plugin']
    },
    install_requires=['pytest', 'Coverage', 'jinja2'],
    python_requires='>=3.7',
)