from jinja2 import FileSystemLoader, Environment
import os
import webbrowser

class VisualReportGenerator:
    def __init__(self):
        pass
    
    @staticmethod
    def generate_visual_report(final_report):
        print('\n\n')
        print('Total statements: ' + str(final_report['Final Coverage']['total_statements']))
        print('Total executed statements: ' + str(final_report['Final Coverage']['executed_statements']))
        print('Total Coverage: ' + str((final_report['Final Coverage']['coverage'])*100) + '%')
        
        loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
        env = Environment(loader=loader)
        template = env.get_template("template_project.html")

        os.makedirs("output", exist_ok=True)
        file = open("output/index.html", "w")

        render = template.render(total_statements=final_report['Final Coverage']['total_statements'], executed_statements= final_report['Final Coverage']['executed_statements'],
                        total_coverage= str(round(final_report['Final Coverage']['coverage']*100, 2)) + '%', dicionario=final_report)

        file.write(render)
        file.close()

    @staticmethod
    def generate_visual_report_per_testfile(final_report):
        '''
        Generate a report divided by test file, with the coverage of each file per test case.
        '''
        
        loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
        env = Environment(loader=loader)
        template = env.get_template("template_case.html")

        os.makedirs("output", exist_ok=True)
        file = open("output/index.html", "w")

        render = template.render(dicionario=final_report)

        file.write(render)
        file.close()

