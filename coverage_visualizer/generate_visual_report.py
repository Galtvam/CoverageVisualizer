from jinja2 import FileSystemLoader, Environment
import os
import webbrowser

class VisualReportGenerator:
    def __init__(self):
        pass
    
    @staticmethod
    def generate_visual_report(final_report):
        print('Total statements: ' + str(final_report['final_coverage']['total_stataments']))
        print('Total executed statements: ' + str(final_report['final_coverage']['executed_statements']))
        print('Total Coverage: ' + str(final_report['final_coverage']['coverage']*100) + '%')
        
        loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
        env = Environment(loader=loader)
        template = env.get_template("template.html")

        os.makedirs("output", exist_ok=True)
        file = open("output/index.html", "w")

        render = template.render(total_statements= final_report['final_coverage']['total_stataments'], executed_statements= final_report['final_coverage']['executed_statements'],
                        total_coverage= str(final_report['final_coverage']['coverage']*100) + '%', dicionario=final_report)

        file.write(render)
        file.close()

        path= os.path.abspath("output/index.html")
        webbrowser.open("file://"+path)

