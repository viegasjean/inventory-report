import csv

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    @classmethod
    def import_data(cls, path: str, tipo: str):
        with open(path, encoding="utf-8") as file:
            produtos = list(csv.DictReader(file))
            if tipo == 'simples':
                return SimpleReport.generate(produtos)
            if tipo == 'completo':
                return CompleteReport.generate(produtos)
