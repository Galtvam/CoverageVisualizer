import os
import subprocess
from coverage import Coverage
import pytest
from xml.dom import minidom



TEST_DIRECTORY = os.getcwd() + "\\intro-to-pytest"

def run_pytest(optional_args=None, timeout=30):
    optional_args = optional_args or []
    try:
        stdout = subprocess.check_output(['pytest'] + optional_args, 
                               text=True, shell=True, cwd=TEST_DIRECTORY, timeout=timeout)
    except subprocess.CalledProcessError as error:
        stdout = error.stdout
    return stdout


def extract_pytest_results_coverage_visualizer(pytest_output):
    for l in pytest_output[::-1]:
        if "Total Coverage" in l:
            return float(l.split(" ")[-1][:-1]) 

def run_pycov(test_dir):
    cov = Coverage()
    cov.start()
    pytest.main(['-x', (os.getcwd() + "\\intro-to-pytest\\" + test_dir), '-vv', ])
    cov.stop()
    cov.xml_report()
    
    mydoc = minidom.parse('coverage.xml')
    classes = mydoc.getElementsByTagName('class')
    for element in classes:
        if element.getAttribute('name') == "services.py":
            coverage = element
    return int(float(coverage.attributes['line-rate'].value)*100)

def run_pycov_fixtures():
    cov = Coverage()
    cov.start()
    pytest.main(['-x', (os.getcwd() + "\\intro-to-pytest"), '-vv', ])
    cov.stop()
    cov.xml_report()
    
    mydoc = minidom.parse('coverage.xml')
    classes = mydoc.getElementsByTagName('class')
    for element in classes:
        if element.getAttribute('name') == "services.py":
            coverage = element
    return int(float(coverage.attributes['line-rate'].value)*100)
