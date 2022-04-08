class VisualReportGenerator:
    def __init__(self):
        pass
    
    @staticmethod
    def generate_visual_report(total_statements, total_executed_statements):
        print(' Total statements: ' + str(total_statements))
        print(' Total executed statements: ' + str(total_executed_statements))
        print(' Total Coverage: ' + str((total_executed_statements/total_statements)*100) + '%')