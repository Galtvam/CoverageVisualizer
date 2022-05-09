import os
from xml.dom import minidom

XML_FILE = 'coverage.xml'

def count_collection_statements(tracers):
    all_tracers = {}
    
    for file in tracers.keys():
        for tracer in tracers[file].keys():
            tracers[file][tracer].xml_report()
            if file not in all_tracers.keys():
                all_tracers[file] = {}
            all_tracers[file][tracer] = count_statements(compute_final=False)
    
    return all_tracers

def count_statements(compute_final=True):
    files_coverage = {}
    total_statements = 0
    total_executed_statements = 0
    
    mydoc = minidom.parse(XML_FILE)
    classes = mydoc.getElementsByTagName('class')
    
    for element in classes:
        element_name = element.getAttribute('name')
        file_name = element.attributes['filename'].value
        # 'plugin.py' in element_name or 
        if not ('test' in element_name) and ('CoverageVisualizer' not in file_name):
            files_coverage[file_name] = count_lines(element)
            
            if compute_final:
                total_executed_statements += files_coverage[file_name]['executed_statements']
                total_statements += files_coverage[file_name]['total_statements']
    
    if compute_final:
        if total_statements > 0:
            total_coverage = total_executed_statements/total_statements
        else:
            total_coverage = 0
        
        # Add the coverage of the project
        files_coverage['final_coverage'] = {'total_statements': total_statements, 'executed_statements': total_executed_statements, 'coverage': total_coverage}
    
    return files_coverage

def count_lines(element):
    lines = element.getElementsByTagName('line')
    
    statement_number = len(lines)
    executed_statements = 0
    
    for line in lines:
        if(int(line.attributes['hits'].value) != 0):
            executed_statements += 1
    
    if statement_number > 0:
        coverage = executed_statements/statement_number
    else:
        coverage = 1
    
    return {'total_statements': statement_number, 'executed_statements': executed_statements, 'coverage': coverage}