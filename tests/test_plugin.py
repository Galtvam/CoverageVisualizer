import os
import shutil

from pytest import fixture
from utils import *

project_dir = os.getcwd() + "\\project_test"

# The data is pre-fetched because multiples sequential executions of pytest.main() does not work properly.
# You can run the coverage for each test case descommenting the py_cov lines and commenting the COVARAGE_RAW_EXECUTION usages.
COVERAGE_RAW_EXECUTION = {
    'test_all_cases': 96,
    'test_with_fixtures': 88,
    'test_with_case_mode': 44,
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
    '''
    Run all the tests and check if the coverages are the same.
    '''
    cov_vis = int(extract_pytest_results_coverage_visualizer(run_pytest(['--coverage-visualizer']).split('\n')))
    py_cov = COVERAGE_RAW_EXECUTION['test_all_cases']
    #py_cov = run_pycov()
    assert cov_vis == py_cov

def test_with_fixtures():
    '''
    Run a specific test case which uses fixtures.
    '''
    test_file ="database_test.py"
    cov_vis = int(extract_pytest_results_coverage_visualizer(run_pytest(['--coverage-visualizer', '.\\tests\\' + test_file]).split('\n')))
    py_cov = COVERAGE_RAW_EXECUTION['test_with_fixtures'] 
    #py_cov = run_pycov_specific_test_case(test_file, "project_test.services")
    assert cov_vis == py_cov
    
def test_with_case_mode():
    '''
    Even with the execution of the same test case, the coverage is not the same because they observe
    the files starting from different moments.
    '''
    test_file ="fail_test.py"
    run_pytest(['--coverage-visualizer', '--case-mode=True', '.\\tests\\' + test_file])
    cov_vis = get_coverage(path=project_dir+'\\coverage.xml', element_name="services")
    py_cov = COVERAGE_RAW_EXECUTION['test_with_case_mode']
    #py_cov = run_pycov_specific_test_case(test_file, "project_test.services")
    assert cov_vis != py_cov
    
def test_coverage_xml_creation():
    '''
    Validates the creation of the coverage.xml file.
    '''
    run_pytest(['--coverage-visualizer'])
    directory = project_dir + "\\coverage.xml"
    assert os.path.exists(directory)
    
def test_coverage_xml_creation_case_mode():
    '''
    Validates the creation of the coverage.xml file.
    '''
    run_pytest(['--coverage-visualizer', '--case-mode=True'])
    directory = project_dir + "\\coverage.xml"
    assert os.path.exists(directory)

def test_coverage_report_generation():
    '''
    Validates the creation of the index.html report file.
    '''
    run_pytest(['--coverage-visualizer'])
    directory = project_dir + "\\output"
    assert os.path.exists(directory + "\\index.html")

def test_coverage_report_generation_case_mode():
    '''
    Validates the creation of the index.html report file.
    '''
    run_pytest(['--coverage-visualizer', '--case-mode=True'])
    directory = project_dir + "\\output"
    assert os.path.exists(directory + "\\index.html")