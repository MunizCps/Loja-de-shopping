from crud1 import *
from crud2 import *
from crud3 import *

dic_Loja={}
dic_Empregado={}
dic_Contrato= {}

recupera_loja(dic_Loja)
recupera_empregado(dic_Empregado)

recupera_contrato(dic_Contrato)

opc = 0

while (opc !=5):
    
    print(50*"=")
    print("Trabalho 4º Bimestre - João Lucas e Letícia Moura")
    print(50*"=" + "\n")
    
    print("1 - Gerenciar Loja")
    print("2 - Gerenciar Empregado")
    print("3 - Gerenciar Contrato")
    print("4 - Relatório")
    print("5 - Finalizar Programa")
    
    opc = int( input("Digite uma opção: ") )

    if opc == 1:
        menu_loja(dic_Loja)
        print("\n\n\n\n")
            
    elif opc == 2:
        menu_empregados(dic_Empregado)
        print("\n\n\n\n")
            
    elif opc == 3:
        menu_contrato(dic_Loja, dic_Empregado, dic_Contrato)
        print("\n\n\n\n")

    elif opc == 4:
        X =  int(input("Digite o ano inicial:"))
        Y =  int(input("Digite o ano final:"))
        relatorio(dic_Loja, dic_Empregado, dic_Contrato, X, Y)
        print("\n\n\n\n")

print("\n\n*** FIM DO PROGRAMA ***\n\n")
