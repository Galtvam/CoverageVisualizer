import os
import re

from pylint import epylint as lint

def get_cover_file_names(directory, count):
    fileExt = r".cover"
    files = [_ for _ in os.listdir(directory) if _.endswith(fileExt)]
    
    for file_name in files:
        if not file_name in count.keys():
            count[file_name] = {}
        read_cover_file(str(directory), file_name, count)
    return count

def read_cover_file(file_dir, file_name, dictionary):
    with open(file_dir + '/' + file_name) as f:
        lines = f.readlines()
        find_executed_lines(lines, file_name, dictionary)
    
def find_executed_lines(lines, file_name, dictionary):
    for (i, l) in enumerate(lines):
        match = re.search(r"\d: ", l)
        if (type(match) == re.Match) or (' import ' in l):
            dictionary[file_name][i+1] = True

def count_statements(file):
    (pylint_stdout, pylint_stderr) = lint.py_run((file + ' -s n -r y --disable=all'), return_std=True)
    a = pylint_stdout.readlines()[4:5]
    #Get the number of statements in the application
    return [int(s) for s in a[0].split() if s.isdigit()][0]

def count_executed_statements(dictionary):
    total = 0
    for a in dictionary.keys():
        if not 'test' in a:
            total += len(dictionary[a])
    return total


if __name__ == '__main__':
    fileDir = os.getcwd()
    get_cover_file_names(fileDir)