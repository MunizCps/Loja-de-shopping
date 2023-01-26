#João Lucas e Leticia Moura
#funções auxiliares
def pausa():
    input("Tecle <ENTER> para continuar...\n")

def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

#crud1
#teste se loja existe
def existe_loja(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

#inserir loja
def insere_loja(dic):
    
    print("Inserindo Loja...")
    
    nome_loja = input("Digite aqui o nome da loja:")

    if existe_loja(dic,nome_loja):
        print(" A loja já foi cadastrada!!! ")
        pausa()
        
    else:
        localização = input(" Digite aqui a localização: ")
        ramoAtuação = input(" Digite o ramo de atuação: ")
        
        valorAluguel = int(input(" Digite o valor de aluguel: "))
        
        telContato = int( input("Digite o telefone de contato: "))

        dic[nome_loja]=(localização,ramoAtuação,valorAluguel,telContato)
        print(" Dados inseridos com sucesso!")
        pausa()

#Mostrar loja
def mostra_loja(dic,chave):
    
    print("Mostrando Loja...")
    
    if existe_loja(dic,chave):
        dados = dic[chave]

        print("Localização, Ramo de atuação, Valor do aluguel, Telefone de contato")
        print(dados[0], dados[1], dados[2], dados[3])

    else:
        print(" Loja não cadastrada! ")

#alterar loja

def altera_loja(dic,chave):

    print("Alterando Loja...")
    
    if existe_loja(dic,chave):
        
        mostra_loja(dic,chave)

        confirma = input("Tem certeza que deseja alterar (S/N): ").upper()

        if confirma == 'S':
            localização = input(" Digite aqui a localização: ")
            ramoAtuação = input(" Digite o ramo de atuação: ")
            valorAluguel = int(input(" Digite o valor de aluguel: "))
            telContato = int( input("Digite o telefone de contato: "))

            dic[chave]=(localização, ramoAtuação, valorAluguel, telContato)

            pausa()
        else:
            print("Alteração cancelada!!!")
            pausa()
    else:
        print("Loja não cadastrada! ")
        pausa()

#remover loja

def remove_loja(dic,chave):

    print("Removendo Loja...")

    if existe_loja(dic,chave):
        
        mostra_loja(dic,chave)

        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper()

        if confirma == 'S':

            del dic[chave]

            print("Dados apagados com sucesso! ")
            pausa()
        else:
            print("Exclusão Cancelada!!!")
            pausa()

    else:
        print("Loja não cadastrada!")
        pausa()

def mostra_todas_loja(dic):

    print("Mostrando Lojas...")

    print("Relatório: Todas as lojas\n")
    print("Nome da loja - Localização - Ramo de atuação - Valor de aluguel - Telefone de contato\n")

    for nome_loja in dic:
        tupla = dic[nome_loja]
        
        linha = nome_loja + " - " + tupla[0] + " - " + tupla[1] + " - " + \
                tupla[2] + " - " + str(tupla[3])

        print(linha)
    print("")
    pausa()

#gravar dados no arquivo

def grava_loja(dic):
    arq = open("loja.txt","w")

    for nome_loja in dic:
        tupla = dic[nome_loja]
        linha = nome_loja+";"+tupla[0]+";"+tupla[1]+";"+tupla[2]+";"+str(tupla[3])+"\n"
        arq.write(linha)
        
    arq.close()

def recupera_loja(dic):
    if existe_arquivo("loja.txt"):
         arq = open("loja.txt", "r")
         for linha in arq:
             linha = linha[:len(linha)-1]
             lista = linha.split(";")
             nome_loja = lista[0]
             localização = lista[1]
             ramoAtuação = lista[2]
             valorAluguel = lista[3]
             telContato = float( lista[4] )

             dic[nome_loja] = (localização,ramoAtuação, valorAluguel, telContato)

#Menu das lojas
def menu_loja(dic_loja):
    opc = 0

    print(20*"=")
    print("    MENU DE LOJA    ")
    print(20*"=")
    
    while( opc!=6):
        print("\nGerenciamento de lojas:\n")
        print("1 - Insere Loja")
        print("2 - Altera Loja")
        print("3 - Remove Loja")
        print("4 - Mostra uma Loja")
        print("5 - Mostra todas as Lojas")
        print("6 - Sair do menu de Lojas")

        opc = int( input("Digite uma opção: ") )

        if opc == 1:
            print("\n")
            insere_loja(dic_loja)
            
        elif opc == 2:
            print("\n")
            nome_loja = input("Nome da loja a ser alterado: ")
            altera_loja(dic_loja, nome_loja)
            
        elif opc == 3:
            print("\n")
            nome_loja=input("Nome da loja a ser removido: ")
            remove_loja(dic_loja, nome_loja)
            
        elif opc == 4:
            print("\n")
            nome_loja=input("Nome da loja a ser consultado: ")
            mostra_loja(dic_loja, nome_loja)
            pausa()
            
        elif opc == 5:
            print("\n")
            mostra_todas_loja(dic_loja)
            
        elif opc == 6:
            # Se escolheu sair, grava os dados no arquivo.
            grava_loja(dic_loja)

#################################################################################


            
         
        
        
