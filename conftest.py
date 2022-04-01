import sys
import os
import trace
import functools

from read_reports import get_cover_file_names, count_executed_statements, count_statements


tracers = []

test_suite_statements = []
test_statements = {}


def pytest_pyfunc_call(pyfuncitem):
    test_function = pyfuncitem.obj

    # Trace each test individually 
    tracer = trace.Trace(trace=0, count=1, countfuncs=0, ignoredirs=[sys.prefix, sys.exec_prefix, 'C:\\Users\\galtv\\AppData\\Local\\Packages'])
    tracers.append(tracer)

    @functools.wraps(test_function)
    def tracer_wrapper(*args, **kwargs):
        tracer.runfunc(test_function, *args, **kwargs)
    
    pyfuncitem.obj = tracer_wrapper
    if not str(pyfuncitem.fspath) in test_statements.keys():
        test_statements[str(pyfuncitem.fspath)] = count_statements(str(pyfuncitem.fspath))
    #test_suite_statements.append(count_statements(str(pyfuncitem.fspath)))


def pytest_sessionfinish(session, exitstatus):
    count = {}
    directory = os.getcwd()

    total_statements = count_statements(directory)
    # Assume que todos os valores são iguais, ou seja, o mesmo arquivo de teste foi executado
    #total_statements -= test_suite_statements[-1]
    total_statements -= sum(test_statements.values())
    total_statements -= count_statements(directory + '\\conftest.py') #remove os statements desse aquivo
    total_statements -= count_statements(directory + '\\read_reports.py') #remove os statements do read_reports
    print('Total: ' + str(total_statements))

    for i, tracer in enumerate(tracers):
        results = tracer.results()
        results.write_results()
        get_cover_file_names(directory, count)
    
    total_executed_statements = count_executed_statements(count)
    print('Total executed statements: ' + str(total_executed_statements))
    print('Total Coverage: ' + str((total_executed_statements/total_statements)*100) + '%')


    