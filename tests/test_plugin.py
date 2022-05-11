import os
import shutil

from pytest import fixture
from utils import run_pytest, run_pycov, run_pycov_fixtures, extract_pytest_results_coverage_visualizer, is_there_path

project_dir = os.getcwd() + "\\project_test"

COVERAGE_RAW_EXECUTION = {
    'test_all_cases': 96,
    'test_with_fixtures': 88,
}

@fixture(autouse=True)
def delete_coverage_file():
    yield 
    
    files = [project_dir + "\\coverage.xml", 
             project_dir + "\\.coverage", 
             "coverage.xml", 
             ".coverage"]
    
    folders = [project_dir + "\\output\\", 
               "output"]
    
    for file in files:
        if is_there_path(file):
            os.remove(file)
    
    for folder in folders:
        if is_there_path(folder):
            try:
                shutil.rmtree(folder)
            except:
                shutil.rmtree(folder)

def test_all_cases():
    cov_vis = int(extract_pytest_results_coverage_visualizer(run_pytest(['--coverage-visualizer']).split('\n')))
    py_cov = COVERAGE_RAW_EXECUTION['test_all_cases'] #run_pycov()
    assert cov_vis == py_cov

def test_with_fixtures():
    test_file ="database_test.py"
    cov_vis = int(extract_pytest_results_coverage_visualizer(run_pytest(['--coverage-visualizer', '.\\tests\\' + test_file]).split('\n')))
    py_cov = COVERAGE_RAW_EXECUTION['test_with_fixtures'] #run_pycov_fixtures(test_file)
    assert cov_vis == py_cov
    
def test_coverage_xml_creation():
    run_pytest(['--coverage-visualizer'])
    directory = project_dir + "\\coverage.xml"
    assert os.path.exists(directory)

def test_coverage_report_generation():
    run_pytest(['--coverage-visualizer'])
    directory = project_dir + "\\output"
    assert os.path.exists(directory + "\\index.html")