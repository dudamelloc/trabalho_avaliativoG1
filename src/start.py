import utilities
import menu
import stock
import sales
import historic

def data(): 
     """
     Função que inicia os dados do programa
     """
     sales_list = []
     changes_list = []
     stock ={ 


         "Lampada" : {"price": 12.40, "amount": 7, "price_historic": [7, 7.50], "category": "Material De Construcao"}, 
         "Mesa" : {"name": "Mesa", "price": 299.99, "amount": 5, "price_historic": [305.50, 299.00], "category": "Mobilia"}, 
         "Cadeira" : {"name": "Cadeira", "price": 5.99, "amount": 16, "price_historic": [435.08, 5.99], "category": "Mobilia"} 
     } 
  
     return stock, sales_list, changes_list 

def direct(option, stock_items, sales_list, changes_list): 
     """
     Função que direciona a escolha do usuario para função que faz o que foi solicitado.

     :param option: A opção que o usuario digitou no menu.
     :param stock_items: O stocke de itens.
     :param sales_list: A lista de vendas.
     :param changes_list: A lista de atualizações.
     """

     if option == 1: 
         stock.add_product(stock_items, changes_list) 
         
     elif option == 2: 
         stock.get_product(stock_items, sales_list, changes_list) 
  
     elif option == 3: 
         stock.show_all_products (stock_items) 

     elif option == 4:
         sales.sell_product(stock_items, sales_list) 
        
     elif option == 5:
         historic.show_sales_report(sales_list)

     elif option == 6:
        stock.price_update (stock_items, changes_list)

     elif option == 7:
         stock.delete_product (stock_items, changes_list)
        
     elif option == 8:
        historic.show_historic(changes_list)
        
     elif option == 9:
         stock.search_by_category(stock_items)

    
def start_program():
     """
     Função que da o inicia o programa
     """
     stock, sales_list, changes_list = data()

     while True:
         input("Precisone enter para continuar...") 
         utilities.clear() 
      
         option = menu.menu() 
         
         if option == 0: 
             print ("Programa encerrado!")
             break
         
         direct(option, stock, sales_list, changes_list) 



