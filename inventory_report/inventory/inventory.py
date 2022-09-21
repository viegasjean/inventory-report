

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    @classmethod
    def import_data(cls, path: str, tipo: str):
        arquivo, extensao = path.split('.')
        match extensao:
            case "csv":
                produtos = CsvImporter.import_data(path)
            case "json":
                produtos = JsonImporter.import_data(path)
            case "xml":
                produtos = XmlImporter.import_data(path)
            case _:
                raise ValueError(f"o arquivo {arquivo}.{extensao} é invalido")
        if tipo == 'simples':
            return SimpleReport.generate(produtos)
        if tipo == 'completo':
            return CompleteReport.generate(produtos)
