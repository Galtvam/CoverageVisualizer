import os
from utils import run_pytest, run_pycov, run_pycov_fixtures, extract_pytest_results_coverage_visualizer
#import shutil


def test_without_fixtures():
    cov_vis = int(extract_pytest_results_coverage_visualizer(run_pytest(['--coverage-visualizer', 'tests\\20_no_fixture_test.py']).split('\n')))
    py_cov = run_pycov('tests\\20_no_fixture_test.py')
        
    assert cov_vis == py_cov

def test_with_fixtures():
    py_cov = int(extract_pytest_results_coverage_visualizer(run_pytest(['--coverage-visualizer', '.']).split('\n')))
    cov_vis = run_pycov_fixtures()
    
    assert cov_vis == py_cov
    
def test_coverage_directory_creation():
    directory = os.getcwd() + "\\intro-to-pytest" + "\\.coverage_reports"
    assert os.path.exists(directory)

def test_coverage_report_generation():
    directory = os.getcwd() + "\\intro-to-pytest" + "\\output"
    assert os.path.exists(directory + "\\index.html")