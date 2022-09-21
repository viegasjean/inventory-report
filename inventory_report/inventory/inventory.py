from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def read_file(cls, path):
        _, extensao = path.split(".")
        if extensao == "csv":
            return CsvImporter.import_data(path)
        if extensao == "json":
            return JsonImporter.import_data(path)
        if extensao == "xml":
            return XmlImporter.import_data(path)
        raise ValueError("Unknown extension")

    @classmethod
    def import_data(cls, path: str, tipo: str):
        produtos = cls.read_file(path)
        if tipo == "simples":
            return SimpleReport.generate(produtos)
        if tipo == "completo":
            return CompleteReport.generate(produtos)
