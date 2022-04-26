import os
import subprocess


TEST_DIRECTORY = os.getcwd() + "\\intro-to-pytest"

def run_pytest(optional_args=None, timeout=15):
    optional_args = optional_args or [] 
    stdout = subprocess.check_output(['pytest'] + optional_args + [ '.'], 
                               text=True, shell=True, cwd=TEST_DIRECTORY, timeout=timeout)
    return stdout


def extract_pytest_results_coverage_visualizer(pytest_output):
    for l in pytest_output[::-1]:
        if "Total Coverage" in l:
            return float(l.split(" ")[-1][:-1])

