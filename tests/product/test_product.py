from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )

    assert type(product.id) == int

    assert type(product.nome_do_produto) == str

    assert type(product.nome_da_empresa) == str

    assert type(product.data_de_fabricacao) == str

    assert type(product.data_de_validade) == str

    assert type(product.numero_de_serie) == str

    assert type(product.instrucoes_de_armazenamento) == str

    assert (
        str(product)
        == "O produto Nicotine Polacrilex fabricado em 2021-02-18 por" +
        " Target Corporation com validade até 2023-09-17 precisa ser" +
        " armazenado instrucao 1."
    )
