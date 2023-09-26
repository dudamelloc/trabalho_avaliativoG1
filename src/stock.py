import utilities
import historic

def add_product(stock, changes_list, name = None): 
     """
     Função para que adiciona um produto ao stock. Se o parametro opcional name for passado é pulada a etapa de solicitação do nome.

     :param stock: O stock de itens.
     :param changes_list: A lista de atualizações.
     :param name: Um parametro opcional que se não for None pula a solicitação do atributo nome para o cadastro do produto.
     """
     utilities.clear ()
     product = attributes_product(name)
     
     # extrai as infomações do produto
     name_product = product[0]
     product_amount = product[1]
     unit_price = product[2]
     category = product [3]
     price_historic = []
     price_historic.append (unit_price)

     new_product = { 
         "price_historic" : price_historic,
         "category" : category,
         "amount" : product_amount, 
         "price" : unit_price 
     } 
      #verifica se o produto já existe no estoque.
     if name_product in stock: 
        option = utilities.validated_yes_no ("Produto já cadastrado. Quer somar com a quantidade atual? Y/N")
        
        if option == "Y":
            stock[name_product]["amount"] += product_amount

        
     else: 
         # Adiciona um novo produto 
         stock[name_product] = new_product 
  
     historic.add_addition_in_changes_list(changes_list, product)
     return stock

def attributes_product(name = None): 
     """
     Função que solicita para o usuario os atributos para cadastro do produto. Se o atributo opcional não for None pula uma etapa do cadastro.

     :param name: Atributo opcional que se não for None pula a etapa de solicitação do nome do produto.
     :return: Uma lista com os atriutos do produto.
     """

     attributes = ("Digite o nome do produto: ",
                   "Digite a quantidade do produto:",  
                   "Digite o preço do produto: ",
                   "Digite a categoria do produto: "
                    ) 
  


     product = [] 
  
     for i in range(len(attributes)): 
         #se nome for passado e o for estiver na primeira volta ele adiona +1 no i adiciona mais um na lista e ignora o restante do for
         #adicionando o +1 ele ignora a primeira pergunta para  n ser necessario informar novamente o nome
         if i == 0 and name is not None:
            i += 1
            product.append(name)
            continue
      
         if i == 0: 
            attribute = input(f"{attributes[i]}").capitalize() 

         elif i == 1: 
            attribute = utilities.valided_input_int (f"{attributes[i]}") 
            
         elif i == 2:
            attribute = utilities.valided_input_float (f"{attributes[i]}") 

         elif i == 3: 
            attribute = input(f"{attributes[i]}").capitalize()
                 
         product.append(attribute) 
     return product

def get_product(stock, sales_list, changes_list):
    """
    Função que busca um produto por seu nome e imprime todos seus atributos na tela, incluindo o histórico de vendas do mesmo
    Solicita o nome do profuto a ser buscado, caso não esteja cadastrado gera uma pergunta para o usuario, se ele quer cadastrar o direciona para o cadastro do produto
    
    :param stock: O Stock de itens.
    :param sales_list: A lista de vendas.
    :return: Imprime na tela os dados do produto.
    """

    utilities.clear()
    search = input("Digite o nome do produto que deseja buscar: ").capitalize()
    if search not in stock:
        utilities.clear()
        print(f'O produto {search} não foi encontrado no estoque.')
        
        option = utilities.validated_yes_no("Deseja adicionar no stock? Y/N?").upper()

        if option == "Y":
            add_product(stock, changes_list, search)
        return
    
    sales_historic = historic.get_in_sale_list(sales_list, search)

    product = stock[search]
    print(f'Produto: {search}')
    print(f'Quantidade em estoque: {product["amount"]}')
    print(f'Preço unitário: R${product["price"]}')
    print(f'Histórico de preço: {product["price_historic"]}')
    print(f'Categoria: {product["category"]}')
    print("Histórico de vendas: \n[")
    for x in range(len(sales_historic)):
        print(sales_historic[x])
    print("\n]")
    return stock

def show_all_products(stock): 
     """
     Imprime todos os produtos que estão no estoque.
     
     :param stock: stock de itens.
     :return: imprime todos os produtos que estão no estoque.
     """

     utilities.clear() 
     print ("Lista de produtos total:") 
     for chave, subdicionario in stock.items(): 
         print(f"Produto: {chave}") 
         print(f"\t - Preço unitario: {subdicionario['price']}") 
         print(f"\t - Quantidade em estoque: {subdicionario['amount']}") 
         print(f"\t - Historico de preços: {subdicionario['price_historic']}")
         print(f"\t - Categoria: {subdicionario['category']}")
     return stock 

def price_update(stock, changes_list):
    """
    Função que atualiza o preço
    Solicita o nome do produto que deseja atualizar, caso n seja encontrado informa que o mesmo não foi encontrado, após solicita o novo preço e atualiza o preço do produto
    
    :param stock: stock de itens.
    :param changes_list: lista de atualizações.
    :return: stock atualizado e lista de atualizações atualizada
    """
    
    name =  input("Digite o nome do produto que deseja atualizar: ")
    name = name.capitalize()

    if name not in stock:
        print("Producto {name} não encontrado...")

    new_price = utilities.valided_input_float(f"Digite o atual preço do produto {name}: ")
    product = stock[name]
    
    oldprice = product['price']
    product["price"] = new_price
    product["price_historic"].append(new_price)
    
    atrtibutes = [
                    name, product['category'],
                    product['amount'], oldprice,
                    new_price
                 ]
    
    historic.add_change_in_changes_list(changes_list, atrtibutes)
    return stock

def delete_product(stock, changes_list):
    """
    Função para deletar um produto do stock, solicitando para o usuario o nome e retorna uma mensagem informando que não foi encontrado o produto que o mesmo deseja deletar caso esse produto não for encontrado
    
    :param stock: stock de itens.
    :param changes_list: lista de atualizações.
    :return: stock atualizado.
    """

    name =  input("Digite o nome do produto que deseja deletar: ")
    name = name.capitalize()

    if name not in stock:
        print("Producto {name} não encontrado...")

    delete_product = stock.pop(name)

    attributes = [
                  name, delete_product.get("category"), 
                  delete_product.get("amount"), delete_product.get("price")
                 ]
    historic .add_exclusion_in_changes_list(changes_list, attributes)

    return stock

def search_by_category (stock): 
    """"
    Função que retorna um listagem com todos os produtos de uma determinada categoria que é solicitada pelo usuario
    :param stock: stock itens.
    """
    products_of_category = []

    category = input("Digite uma categoria: ")
    category = category.capitalize ()

    found = False  # Variável para verificar se a categoria foi encontrada

    for product, attributes in stock.items():
        if attributes.get("category").capitalize() == category:
            products_of_category.append(product)
            found = True  # A categoria foi encontrada

    if not found:
        print(f"Categoria '{category}' não encontrada.")
    else:
        print(f"Produtos na categoria '{category}':")
        for product in products_of_category:
            print(product)
    
    return 
