import utilities
import datetime


def show_sales_report(sales_list):
    """
    Função imprime na tela a lista de vendas.

    :param sales_list: Lista de vendas.
    :return: Imprime a lista de vendas.
    """
     
    utilities.clear()
    print("\t Relatório de vendas:")

    for i in sales_list: #itera sobre a lista vendas
        print (f"\n Nome: {i.get('name')} \n Quantidade vendida: {i.get('amount')} \n Valor da venda: {i.get('price_sale')} \n Categpria do produto: {i.get('category')} \n Data de venda: {i.get('date_sale')}")
    
    return sales_list

def add_sale_in_list(sale_list, atributes):
     """
     Função que coloca uma adição de itens na lista de atualizações

     :param sale_list: Lista de vendas.
     :param atributes: Lista de atributos da atualização.
     :return: Lista de atualização em atualizada.
     """
     new_sale = { 
         "name": atributes[0],
         "category" : atributes[3],
         "amount" : atributes[1], 
         "price_sale" : atributes[2],
         "date_sale" : datetime.datetime.now()
     } 

     sale_list.append(new_sale)

     return sale_list

def get_in_sale_list(sale_list, name):
    result = []

    for sale in sale_list:
        if sale.get("name") == name:
            result.append(f"\n quantidade vendida: {sale.get('amount')} \n valor da venda: {sale.get('price_sale')} \n data da venda: {sale.get('date_sale')} ")

    return result


def add_change_in_changes_list(changes_list, change):
     """
     Função que coloca uma atualização de produto na lista de atualizações.

     :param changes_list: Lista de atualizações.
     :param atributes: Lista de atributos da atualização.
     :return: Lista de atualização em atualizada.
     """
     new_change = { 
         "name": change[0],
         "category" : change[3],
         "amount" : change[1], 
         "old_price" : change[2],
         "new_price" : change[3],
         "change_date" : datetime.datetime.now()
     } 

     changes_list.append(new_change)

     return changes_list

def add_exclusion_in_changes_list(changes_list, attributes):
     """
     Função que coloca uma exclusão de produto na lista de atualizações.

     :param changes_list: Lista de atualizações.
     :param atributes: Lista de atributos da atualização.
     :return: Lista de atualização em atualizada.
     """
     new_exclusion = { 
         "name": attributes[0],
         "category" : attributes[1],
         "amount" : attributes[2], 
         "price" : attributes[3],
         "exclusion_date" : datetime.datetime.now()
     } 

     changes_list.append(new_exclusion)

     return changes_list

def add_addition_in_changes_list(changes_list, atributes):
     """
     Função que coloca uma adição de produto na lista de atualizações.

     :param changes_list: Lista de atualizações.
     :param atributes: Lista de atributos da atualização.
     :return: Lista de atualização em atualizada.
     """
     new_addition = { 
         "name": atributes[0],
         "category" : atributes[3],
         "amount" : atributes[1], 
         "price" : atributes[2],
         "addition_date" : datetime.datetime.now()
     } 

     changes_list.append(new_addition)

     return changes_list

def show_historic (changes_list):
    """
    Função que imprime o historico de atualizações na tela

    :param changes_list: lista de atualizações
    :return: imprime a lista de atualizações
    """

    utilities.clear()
    print("\t Relatório de vendas:")

    for dict in  changes_list:
        if "addition_date" in dict:
            print(f"\nAdição de produto: \n\t Nome: {dict['name']}\n\t Categoria:{dict['category']}\n\t Quantidade:{dict['amount']}\n\t Preço unidade: {dict['price']}\n\t Data de adição: {dict['addition_date']} ")
            continue

        elif "change_date" in dict:
            print(f"\nAlteração de produto: \n\t Nome: {dict['name']}\n\t Categoria:{dict['category']}\n\t Quantidade:{dict['amount']}\n\t Preço anterior: {dict['old_price']}\n\t Preço atual: {dict['new_price']}\n\t Data de alteração: {dict['change_date']}")
            continue
        
        elif "exclusion_date" in dict:
            print(f"\nExclusão de produto: \n\t Nome: {dict['name']}\n\t Categoria: {dict['category']}\n\t Quantidade: {dict['amount']}\n\t Preço produto: {dict['price']}\n\t Data de Exclusão: {dict['exclusion_date']}")
            continue
                  
    return changes_list


