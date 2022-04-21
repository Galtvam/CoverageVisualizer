class VisualReportGenerator:
    def __init__(self):
        pass
    
    @staticmethod
    def generate_visual_report(final_report):
        print(' Total statements: ' + str(final_report['final_coverage']['total_stataments']))
        print(' Total executed statements: ' + str(final_report['final_coverage']['executed_statements']))
        print(' Total Coverage: ' + str(final_report['final_coverage']['coverage']*100) + '%')