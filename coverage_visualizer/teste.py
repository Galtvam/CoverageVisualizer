from generate_visual_report import VisualReportGenerator


dicionario = {"teste_que_deu_quase.py":{"executed_statements":10, "total_statements":20, "coverage":0.5},
            "teste_que_deu_bom.py":{"executed_statements":23, "total_statements":23, "coverage":1}
}

VisualReportGenerator().generate_visual_report(total_statements =100, 
                                            total_executed_statements=1000, 
                                            dicionario = dicionario)


