import os
import functools
from coverage import Coverage
from enum import Enum, auto

from .read_reports import count_statements, count_collection_statements
from .generate_visual_report import *

APPLICATION_DIRECTORY = os.getcwd()
DEFAULT_REPORTS_DIRECTORY = APPLICATION_DIRECTORY + "\\.coverage_reports"

class USAGE_MODE(Enum):
    PROJECT = auto()
    CASE = auto()

class CoverageVisualizerPlugin:
    
    def __init__(self, mode=USAGE_MODE.PROJECT):
        self.__mode = mode
        
        self.__coverage = None
        self.__test_tracers = {}

    def pytest_sessionstart(self, session):
        if self.__mode == USAGE_MODE.PROJECT:
            self.__coverage = Coverage()
            self.__coverage.start()        
    
    def pytest_pyfunc_call(self, pyfuncitem):
        if self.__mode == USAGE_MODE.CASE:
            test_function = pyfuncitem.obj
            
            # Trace each test individually 
            local_test_tracer = Coverage()
            
            file_name = str(pyfuncitem.fspath)
            test_name = test_function.__name__ + "()"
            
            if not file_name in self.__test_tracers.keys():
                self.__test_tracers[str(pyfuncitem.fspath)] = {}
            self.__test_tracers[str(pyfuncitem.fspath)][test_name] = local_test_tracer
            
            
            @functools.wraps(test_function)
            def tracer_wrapper(*args, **kwargs):
                local_test_tracer.start()
                test_function(*args, **kwargs)
                local_test_tracer.stop()
                
            pyfuncitem.obj = tracer_wrapper
        

    def pytest_sessionfinish(self, session, exitstatus):
        if self.__mode == USAGE_MODE.PROJECT:
            self.__coverage.stop()
            self.__coverage.xml_report()
            
            coverage_data = count_statements()
            VisualReportGenerator.generate_visual_report(coverage_data)
        else:
            coverage_collection_data = count_collection_statements(self.__test_tracers)
            VisualReportGenerator.generate_visual_report_per_testfile(coverage_collection_data)
        

def pytest_configure(config):
    if config.getvalue('use_coverage_visualizer'):
        if (config.getvalue('case_mode')):
            plugin = CoverageVisualizerPlugin(USAGE_MODE.CASE)
        else:
            plugin = CoverageVisualizerPlugin(USAGE_MODE.PROJECT)
            
        config.pluginmanager.register(plugin, 'coverage_visualizer_plugin')


def pytest_addoption(parser):
    """Add plugin CLI options"""

    parser.addoption(
        '--coverage-visualizer',
        dest='use_coverage_visualizer',
        action='store_true',
        default=False,
        help='Enable Coverage Visualizer plugin.'
    )
    
    parser.addoption(
        '--case-mode',
        dest='case_mode',
        default=False,
        help='Enable Coverage Visualizer per test case and file.'
    )

