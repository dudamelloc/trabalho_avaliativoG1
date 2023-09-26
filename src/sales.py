import utilities
import historic

def sell_product(stock, sales_list): 
    """
    Função que vende um produto e atualiza o estoque.
    Solicita o nome do produto, se o produto não for encontrado exibe uma mensagem avisando que o produto não foi encontrado.

    :param stock: Stock de itens.
    :sales_list: Lista de vendas
    :return: Stocke de itens e Lista de vendas atualizados.
    """
    utilities.clear ()
      
    product_sold = input("Digite o nome de um produto vendido: ")
    product_sold = product_sold.capitalize()
    
    if product_sold not in stock: 
        print(f"{product_sold} não encontrado...")
        return stock, sales_list 


    quantity_sell_product = utilities.valided_input_int("Digite a quantidade do produto vendida:")

        
    if quantity_sell_product > stock[product_sold]["amount"]:
        print(f"Você tem {stock[product_sold]['amount']} unidades de {product_sold}...")
            
        return stock, sales_list
            
    elif quantity_sell_product == stock[product_sold]["amount"]:
       
        option = utilities.validated_yes_no(f"Você tem apenas {stock[product_sold]['amount']} de {product_sold}, deseja zerar o estoque? Y/N").upper()
        
        if option == "N":
            return stock
        
    stock[product_sold]["amount"] -= quantity_sell_product    
   
    product = stock[product_sold] 
    valor_total = quantity_sell_product * product["price"]

    print(f'Produto: {product_sold}') 
    print(f'Quantidade atual em estoque: {product["amount"]}') 
    print(f'Valor unitário: {product["price"]}')
    print(f'Valor total da venda: R${valor_total}') 
    
    sale = [product_sold,
            quantity_sell_product,
            valor_total,
            product['category']
            ] 

    historic.add_sale_in_list(sales_list, sale)

    return stock
    