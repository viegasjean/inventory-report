from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, produtos):
        simple_report = super().generate(produtos)
        simple_report += "\nProdutos estocados por empresa:\n"
        empresas = Counter(
            [produto["nome_da_empresa"] for produto in produtos]
        )

        for k, v in empresas.items():
            simple_report += f"- {k}: {v}\n"

        return simple_report
