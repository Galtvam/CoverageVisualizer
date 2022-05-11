import os
import subprocess
from coverage import Coverage
import pytest
from xml.dom import minidom



TEST_DIRECTORY = os.getcwd() + "\\project_test"

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

def run_pycov():
    cov = Coverage()
    cov.start()
    pytest.main([(os.getcwd() + "\\project_test\\"), ])
    cov.stop()
    cov.xml_report()
    return get_coverage('project_test.services')

def run_pycov_specific_test_case(test_name, element_name,):
    cov = Coverage()
    cov.start()
    pytest.main([(os.getcwd() + "\\project_test\\tests\\" + test_name )])
    cov.stop()
    cov.xml_report()
    return get_coverage(element_name= element_name)

def get_coverage(element_name, path='coverage.xml', ):
    mydoc = minidom.parse(path)
    classes = mydoc.getElementsByTagName('package')
    for element in classes:
        if element.getAttribute('name') == element_name:
            coverage = element
            return int(float(coverage.attributes['line-rate'].value)*100)
    return False

def is_there_path(path):
    return os.path.exists(path)