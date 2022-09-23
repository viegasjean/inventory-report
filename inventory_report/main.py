import sys
from inventory_report.inventory.inventory import Inventory


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    arquivo, caminho_do_arquivo_input, tipo_de_relatório = sys.argv

    relatorio = Inventory.import_data(
        caminho_do_arquivo_input, tipo_de_relatório
    )
    print(relatorio, end="")


if __name__ == "__main__":
    main()
