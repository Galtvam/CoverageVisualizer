import sys
import os
import trace
import functools

from .read_reports import get_executed_statements, count_executed_statements, count_statements
from .generate_visual_report import *

APPLICATION_DIRECTORY = os.getcwd()
DEFAULT_REPORTS_DIRECTORY = APPLICATION_DIRECTORY + "\\.coverage_reports"

class CoverageVisualizerPlugin:
    _ignoredirs = [sys.prefix, sys.exec_prefix]
    
    def __init__(self):
        self.__tracers = []
        self.__test_files_statements = {}
        self.__count_executed_statements = {}

    def pytest_pyfunc_call(self, pyfuncitem):
        test_function = pyfuncitem.obj
        
        # Trace each test individually 
        tracer = trace.Trace(trace=0, count=1, countfuncs=0, countcallers=0, ignoredirs=CoverageVisualizerPlugin._ignoredirs)
        self.__tracers.append(tracer)

        @functools.wraps(test_function)
        def tracer_wrapper(*args, **kwargs):
            tracer.runfunc(test_function, *args, **kwargs)

        pyfuncitem.obj = tracer_wrapper
        if not str(pyfuncitem.fspath) in self.__test_files_statements.keys():
            self.__test_files_statements[str(pyfuncitem.fspath)] = count_statements(str(pyfuncitem.fspath))


    def pytest_sessionfinish(self, session, exitstatus):
        total_statements = count_statements(APPLICATION_DIRECTORY)
        total_statements -= sum(self.__test_files_statements.values())
    
        for i, tracer in enumerate(self.__tracers):
            if i == 0:
                results = tracer.results()
            else:
                results.update(tracer.results())
        
        if results:
            results.write_results(coverdir=DEFAULT_REPORTS_DIRECTORY)
            get_executed_statements(DEFAULT_REPORTS_DIRECTORY, self.__count_executed_statements)
            
        total_executed_statements = count_executed_statements(self.__count_executed_statements)
        VisualReportGenerator.generate_visual_report(total_statements, total_executed_statements)


def pytest_configure(config):
    if config.getvalue('use_coverage_visualizer'):
        config.pluginmanager.register(CoverageVisualizerPlugin(), 'coverage_visualizer_plugin')


def pytest_addoption(parser):
    """Add plugin CLI options"""

    parser.addoption(
        '--coverage-visualizer',
        dest='use_coverage_visualizer',
        action='store_true',
        default=False,
        help='Enable Coverage Visualzier plugin.'
    )

