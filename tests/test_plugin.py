import os
from utils import run_pytest, extract_pytest_results_coverage_visualizer


def test_without_fixtures():
    py_cov = 37
    cov_vis = int(extract_pytest_results_coverage_visualizer(run_pytest(['--coverage-visualizer',]).split('\n')))
    assert cov_vis == py_cov

def test_with_fixtures():
    py_cov = 79
    cov_vis = int(extract_pytest_results_coverage_visualizer(run_pytest(['--coverage-visualizer',]).split('\n')))
    assert  cov_vis == py_cov
    
def test_coverage_directory_creation():
    directory = os.getcwd() + "\\intro-to-pytest" + "\\.coverage_reports"
    assert os.path.exists(directory)

def test_coverage_report_generation():
    directory = os.getcwd() + "\\output"
    assert os.path.exists(directory + "\\index.html")