class VisualReportGenerator:
    def __init__(self):
        pass
    
    @staticmethod
    def generate_visual_report(final_report):
        total_statements = final_report['final_coverage']['total_stataments']
        total_executed_statements = final_report['final_coverage']['executed_statements']
        print(' Total statements: ' + str(total_statements))
        print(' Total executed statements: ' + str(total_executed_statements))
        print(' Total Coverage: ' + str((total_executed_statements/total_statements)*100) + '%')