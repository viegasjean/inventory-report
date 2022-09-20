from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(produtos):
        produtos_na_validade = [
            produto
            for produto in produtos
            if datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            > datetime.today()
        ]

        fabricacao_mais_antiga = min(
            produtos, key=lambda x: x["data_de_fabricacao"]
        )["data_de_fabricacao"]

        validade_mais_proxima = min(
            produtos_na_validade, key=lambda x: x["data_de_validade"]
        )["data_de_validade"]

        empresas = Counter(
            [produto["nome_da_empresa"] for produto in produtos]
        )

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresas.most_common(1)[0][0]}"
        )
