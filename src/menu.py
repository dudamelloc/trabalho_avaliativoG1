import utilities

def menu():
    """
    Imprime na tela um menu e solicita para o usuario a sua opção de escolha

    :return: A escolha do usuario.
    """
    while True:
        utilities.clear()
        utilities.time_sleep(0.5)
        print("""
        ------------------------------------------
        |   OPÇÕES                               |
        |   1- Adicionar um produto.             |
        |   2- Buscar um produto.                |
        |   3- Visualizar todos os produtos.     |
        |   4- Vender um produto.                |
        |   5- Visualizar Relatório de Vendas.   |
        |   6- Alterar o valor do produto.       |
        |   7- Excluir o produto.                |             
        |   8- Histórico de alterações.          |
        |   9- Buscar por Categoria.             |
        |   0- Para sair.                        |
        ------------------------------------------
        """)
        option = utilities.valided_input_int("Digite sua opção: ")

        return option