

#João Lucas e Leticia Moura
#Crud3

from crud1 import*
from crud2 import*


def existe_contrato(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

  
def insere_contrato(dicL, dicE, dicC):    
    
    nome_Loja = input("Digite o nome da loja:")
    
    if existe_loja(dicL,nome_Loja):       
        
        CPF = input("Digite o CPF:")
        
        if existe_empregado(dicE, CPF):

            chave = (nome_Loja, CPF)
            print(chave)
            
            if ( existe_contrato(dicC, chave) ):
                
                print("Este contrato já existe!")
                pausa()

            else:

                data=  input("Digite a data:")
                salario = int( input("Digite o salário:") )
                dicO=[]
                
                observacoes = input("Digite as observações:")
                while (observacoes !=""):
                    dicO.append(observacoes)
                    observacoes = input("Digite as observações:")

                    if (len(observacoes)==0):
                        print("sem observações")
                        pausa()
                
                dicC[ chave ] = (salario, dicO,data)
                print(dicC)

                print("Dados inseridos com sucesso!")
                pausa()

        else:

            print("Este CPF não existe!")
            pausa()

    else:

        print("Esta loja não existe!")
        pausa()


def mostra_contrato(dicL, dicE, dicC, nome_Loja, CPF):

    chave = (nome_Loja, CPF) 
    
    if existe_contrato(dicC,chave):
        obs=[]
        dados = dicC[chave]
        print(dados)

        print("Dados do contrato:")
        print("-----------------\n")
        
        print("Loja:")
        print("-------")
        mostra_loja(dicL, nome_Loja)
        print()
       
        print("Empregado:")
        print("-------------")
        mostra_empregado(dicE, CPF)
        print()

        obs = " - ".join(dados[1])
        
        print(f"Salário: {dados[0]}")
        print(f"Observações: {dados[1]}")
        
    else:

        
        print("O contrato informado não existe!")


def altera_contrato(dicL, dicE, dicC, nome_Loja, CPF):
    
    chave = (nome_Loja, CPF)
    
    if existe_contrato(dicC, chave):
       
        mostra_contrato(dicL, dicE, dicC, nome_Loja, CPF)

        confirma = input("Tem certeza que deseja alterá-la? (S/N): ").upper()
        
        if confirma == 'S':
            data=  input("Digite a data")
            salario = int( input("Digite o salário:") )
            observacoes = input("Digite as observações:")
            dicO=[]
            while (observacoes !=""):
                dicO.append(observacoes)
                observacoes = input("Digite as observações:")
                    

            if (len(observacoes)==0):
                dicO.append("Sem obseravações")      
       
            dicC[ chave ] = (salario, dicO, data)
            
            print("Dados alterados com sucesso!")
            pausa()
            
        else:

            
            print("Alteração cancelada!")
            pausa()

    else:

        
        print("Este contrato não está cadastrado!")
        pausa()


def remove_contrato(dicL, dicE, dicC, nome_Loja, CPF):

   
    chave = (nome_Loja, CPF)    
    
    
    
    if existe_contrato(dicC,chave):

        
        mostra_contrato(dicL, dicE, dicC, nome_Loja, CPF)

        
        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper()
        
        if confirma == 'S':

            
            del dicC[chave]
       
            print("Dados apagados com sucesso!")
            pausa()
            
        else:

          
            print("Exclusão cancelada!")
            pausa()

    else:

        
        print("Este contrato não está cadastrado!")
        pausa()



def mostra_todos_contratos(dicL, dicE, dicC):

   
    print(" Mostra todos os contratos")
    print("----------------------------\n")
    
   

    for chave in dicC:

        
        nome_Loja = chave[0]
        CPF = chave[1]

        
        mostra_contrato(dicL, dicE, dicC, nome_Loja, CPF)

        print("----------------------------\n")

    

    print("")
    pausa()


def grava_contrato(dic):

    
    arq = open("contrato.txt", "w")

    
    
    for chave in dic:

        
        nome_Loja = chave[0]
        CPF = chave[1]

        
        tupla = dic[chave]

        
        salario = str( tupla[0] )
        
        obs = "#".join(tupla[1])

        datinha=tupla[2]

        
        linha = nome_Loja+";"+CPF+";"+salario+";"+obs+";"+datinha+"\n"

        
        arq.write(linha)
    
    arq.close()

 
def recupera_contrato(dic):
    
    if (existe_arquivo("contrato.txt")):
        arq = open("contrato.txt","r")
        
        for linha in arq:
            linha = linha[:len(linha)-1]
            lista = linha.split(";")

            nome_Loja= lista[0]
            CPF = lista[1]
            
            salario = lista[2]
            observacoes = lista[3]
            data = lista[4]
            obs= observacoes.split("#")

            chave = (nome_Loja, CPF)

            dic[chave] = (salario,obs,data)       


def relatorio(dicL, dicE, dicC, X, Y):

    
    print("Relatório: Contratos com ano entre", X, " e ", Y)
    print("---------------------------------------------\n")
    
    

    for chave in dicC:
        valor = dicC[chave]                        
        
        anoingr = valor[2]                               
        
        if ( int(anoingr) >= X and int(anoingr) <= Y ):
            
            nome_Loja = chave[0]
            CPF = chave[1]
           
            mostra_contrato(dicL, dicE, dicC, nome_Loja, CPF)

            print("----------------------------\n")
       
    print("")
    pausa()


def menu_contrato(dicL, dicE, dicC):
    
    opc = 0
    print(25*"=")
    print("    MENU CONTRATO   ")
    print(25*"=")
    
    while ( opc != 6 ):

        # Exibe o menu:
        
        print("1 - Insere Contrato")
        print("2 - Altera Contrato")
        print("3 - Remove Contrato")
        print("4 - Mostra um Contrato")
        print("5 - Mostra todos os Contrato")
        print("6 - Sair do menu de Contratos")

        
        opc = int( input("Digite uma opção: ") )
        
        if opc == 1:
            
            insere_contrato(dicL, dicE, dicC)
            
        elif opc == 2:
            print("Alterar Contrato:")
            nome_Loja = input("Digite o nome da loja: ")
            CPF = input("Digite o CPF:")
           
            altera_contrato(dicL, dicE, dicC, nome_Loja, CPF)
            
        elif opc == 3:
            print("Remover contrato :")
            nome_Loja = input("Digite o nome da loja: ")
            CPF = input("Digite o CPF:")
            remove_contrato(dicL, dicE, dicC, nome_Loja, CPF)
            
        elif opc == 4:
            print("Consultar Contrato:")
            nome_Loja = input("Digite o nome da loja: ")
            CPF = input("Digite o CPF:")
            mostra_contrato(dicL, dicE, dicC, nome_Loja, CPF)
            pausa()
            
        elif opc == 5:
            mostra_todos_contratos(dicL, dicE, dicC)
            
        elif opc == 6:
        
            grava_contrato(dicC)

