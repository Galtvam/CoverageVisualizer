from jinja2 import FileSystemLoader, Environment
import os
import webbrowser

class VisualReportGenerator:
    def __init__(self):
        pass
    
    @staticmethod
    def generate_visual_report(total_statements, total_executed_statements):
        
        loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
        env = Environment(loader=loader)
        template = env.get_template("template.html")

        os.makedirs("output", exist_ok=True)
        file = open("output/index.html", "w")

        render = template.render(total_statements= total_statements, executed_statements= total_executed_statements,
                        total_coverage= str((total_executed_statements/total_statements)*100) + '%')

        file.write(render)
        file.close()

        path= os.path.abspath("output/index.html")
        webbrowser.open("file://"+path)