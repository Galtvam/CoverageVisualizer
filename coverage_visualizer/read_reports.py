import os
import re

from pylint import epylint as lint

EXECUTED_LINES_REGEX = r'\d: '
PYLINT_ARGUMENTS = ' -s n -r y --disable=all'

def count_statements(file):
    (pylint_stdout, pylint_stderr) = lint.py_run((file + PYLINT_ARGUMENTS), return_std=True)
    report_line = pylint_stdout.readlines()[4:5]
    #Get the number of statements in the application
    return [int(s) for s in report_line[0].split() if s.isdigit()][0]

def count_executed_statements(dictionary):
    total = 0
    for a in dictionary.keys():
        if not 'test' in a:
            total += len(dictionary[a])
    return total

def get_executed_statements(directory, count):
    fileExt = r".cover"
    files = [_ for _ in os.listdir(directory) if _.endswith(fileExt)]
    
    for file_name in files:
        if not file_name in count.keys():
            count[file_name] = {}
            
        if not 'test' in file_name:
            read_cover_file(str(directory), file_name, count)
    return count

def read_cover_file(file_dir, file_name, dictionary):
    with open(file_dir + '/' + file_name) as f:
        lines = f.readlines()
        find_executed_lines(lines, file_name, dictionary)
    
def find_executed_lines(lines, file_name, dictionary):
    temp_def_index = 0
    temp_def_executed = False
    for (i, l) in enumerate(lines):
        if ' import ' in l:
            dictionary[file_name][i+1] = True
        elif ' def' in l:
            #Stores the index of the function definition
            temp_def_index = i + 1
            temp_def_executed = True
        else:
            match = re.search(EXECUTED_LINES_REGEX, l)
            if (type(match) == re.Match):
                #Check if the def statement was executed
                if temp_def_executed:
                    dictionary[file_name][temp_def_index] = True
                    temp_def_executed = False
                dictionary[file_name][i+1] = True
