import time
import os

def valided_input_float (message):
    """
    Entrada de numero flutuante validada, aceita apenas numeros fltuantes/inteiros
    Se a entrada não for um numero flutuante/inteiro solicita que digite novamente
    retorna um numero flutuante

    :param message: Nota para o usuario.
    :return: Numero flutuante
    """
    while True:        
             value = input(message) 
             try: 
                value = float(value) 
             except ValueError: 
                print("Opção inválida, tente novamente...") 
                time_sleep(3) 
                continue 
             break
    return float(value)

def valided_input_int(message):
    """
    Entrada de numero inteiro validada, aceita apenas numeros inteiro
    Se a entrada não for um numero inteiro solicita que digite novamente
    retorna um numreo inteiro

    :param message: Nota para o usuario.
    :return: Numero inteiro.
    """

    while True:        
             value = input(message) 
             try: 
                value = int(value) 
             except ValueError: 
                clear()
                print("Opção inválida, tente novamente...") 
                time_sleep(3) 
                continue 
             break
    return int(value)

def validated_yes_no (message):
      """
      Função que valida se a resposta do usuario foi Y ou N.
      Se não for Y ou N solicita que o usuario digite novamente a resposta.

      :param message: Nota para o usuario.
      :return: Y/N
      """

      while True: 
             opition = input(message).upper() 
             if opition == "Y": 
                 
                 return opition 
  
             elif opition == "N": 
                 return opition
            
             else:  
                 clear () 
                 print ("Resposta invalida tente novamente.") 
                 time_sleep(5)


def clear():
      """
      Função para limpar o terminal
      """
      os.system("cls")


def time_sleep(value):
     """
     Função que conta um tempo de espera
     :param value: 
     """
     time.sleep(value)