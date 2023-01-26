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

#crud 2
#teste se existe empregado
def existe_empregado(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

#inserir dados
def insere_empregado(dic):

    print("Inserindo Empregado...")
    
    cpf = input("Digite o CPF do empregado:")
    
    if existe_empregado(dic,cpf):
        print("Empregado já está cadastrado!")
        pausa()

    else:
        nome = input("Digite o nome do empregado:").capitalize()
        data_de_nascimento = input("Digite a data de nascimento(00/00/0000):")
        sexo = input("Digite qual o sexo(M/F):").upper()
        endereço = input("Digite o endereço(Rua, n° - bairro):")
        escolaridade = input("Digite qual seu grau de escolaridade do empregado:")

        #lista para emails
        emails = []

        email = input("Digite um e-mail:")
        while (email != ""):
            emails.append(email)
            email = input("Digite um e-mail:")
            
        if (len(emails) == 0 ):
            emails.append("Este empregado não possui e-mail:")

        #lista para telefones
        telefones = []

        tel = input("Digite um telefone:")
        while (tel != ""):
            telefones.append(tel)
            tel = input("Digite um telefone:")
            
        if ( len(telefones) == 0 ):
            telefones.append("Este empregado não possui telefone!")

        dic[cpf] = (nome, data_de_nascimento, sexo, endereço, escolaridade, emails, telefones)

        print("Empregado inserido com sucesso!")
        pausa()
        
#fim da função inserir

#mostra dados
def mostra_empregado(dic,chave):

    print("Mostrando Empregado...")
    
    if existe_empregado(dic,chave):
        dados = dic[chave]

        print(f"Nome: {dados[0]}")
        print(f"Data de Nascimento: {dados[1]}")
        print(f"Sexo: {dados[2]}")
        print(f"Endereço: {dados[3]}")
        print(f"Escolaridade: {dados[4]}")

        print(f"E-mails: {dados[5]}")
        
        fones = " - ".join(dados[6])
        print(f"Telefones: {fones}")

    else:
        print("Este empregado não foi cadastrado!")

#fim da função mostra empregado

#altera dados
def altera_empregado(dic,chave):

    print("Alterando Empregado...")
    
    if existe_empregado(dic,chave):
        
        mostra_empregado(dic,chave)
        
        confirma = input("Tem certeza que deseja alterar algum dado? (S/N):").upper()

        if confirma == 'S':
            nome = input("Digite o nome do empregado:").capitalize()
            data_de_nascimento = input("Digite a data de nascimento(00/00/0000):")
            sexo = input("Digite qual o sexo(M/F):").upper()
            endereço = input("Digite o endereço(Rua, n° - bairro):")
            escolaridade = input("Digite qual seu grau de escolaridade do empregado:")

            #lista para e-mails alterados
            emails = []

            email = input("Digite um e-mail:")
            while (email != ""):
                emails.append(email)
                email = input("Digite um e-mail:")

            if ( len(emails) == 0 ):
                emails.append("Este empregado não possui e-mail")
            
            #lista para telefones alterados
            telefones = []

            tel = input("Digite um telefone:")
            while ( tel != "" ):
                telefones.append(tel)
                tel = input("Digite um telefone:")

            if ( len(telefones) == 0 ):
                telefones.append("Este empregado não possui telefone")

            #dicionario com novas informações
            dic[chave]=(nome, data_de_nascimento, sexo, endereço, escolaridade, emails, telefones)

            print("Dados foram alterados com sucesso!")
            pausa()

        else:
            print("Alteração dos dados foi cancelada!")
            pausa()
            
    else:
         print("Empregado não cadastrado!")
         pausa()

#fim da função altera

#remove empregado
def remove_empregado(dic,chave):

    print("Removendo Empregado...")

    if existe_empregado(dic,chave):
        mostra_empregado(dic,chave)

        confirma = input("Tem certeza que deseja apagar? (S/N): ").upper()
        
        if confirma == 'S':
            del dic[chave]

            print("Dados foram apagados com sucesso!")
            pausa()

        else:
            print("Exclusão canselada!")
            pausa()

    else:
        print("Empregado não cadastrado!")
        pausa()

#fim da funão remove

#mostra todos empregados
def mostra_todos_empregados(dic):

    print("Mostrando Empregados...")
    
    print("Relatório: Todos os empregados\n")
    print("CPF - Nome - Data de Nascimento - Sexo - Endereço - Escolaridade - E-mails - Telefones\n")

    for cpf in dic:
        tupla = dic[cpf]
        em = "/" . join(tupla[5])
        fones = "/".join(tupla[6])
        
        linha = cpf + " - " + tupla[0] + " - " + tupla[1] + " - " + tupla[2] + " - " + tupla[3] + " - " + tupla[4] + " - " + em + " - " + fones

        print(linha)

    print("")
    pausa()
    
#fim da função da mostra todos       

#grava dados no arquivo
def grava_empregado(dic):
    arq = open("empregados.txt", "w")
    
    for cpf in dic:
        tupla = dic[cpf]
        em="/#".join(tupla[5])

        fones = "/#".join(tupla[6])

        linha = cpf + ";" + tupla[0] + ";" + tupla[1] + ";" + tupla[2] + ";" + tupla[3] + ";" + tupla[4] + ";" + em + ";" + fones + ";" + "\n"
        
        arq.write(linha)
        
    arq.close()
    
#fim da função grava

#recupera empregado
def recupera_empregado(dic):
    
    if ( existe_arquivo("empregados.txt") ):
        arq = open("empregados.txt", "r")

        for linha in arq:
            linha = linha[:len(linha)-1]
            lista = linha.split(";")

            cpf = lista[0]
            nome = lista[1]
            data_de_nascimento = lista[2]
            sexo = lista[3]
            endereço = lista[4]
            escolaridade = lista[5]
            emails = lista[6]
            telefones = lista[7]

            lista_tel = telefones.split("#")

            dic[cpf] = (nome, data_de_nascimento, sexo, endereço, escolaridade, emails, lista_tel)

#fim da função recupera empregado

#menu crud 2
def menu_empregados(dic_empregado):
    opc = 0

    print(30*"=")
    print("    MENU DE EMPREGADOS    ")
    print(30*"=")

    while ( opc != 6 ):

        print("\nGerenciamento de empregados:\n")
        print("1 - Insere Empregado")
        print("2 - Altera Empregado")
        print("3 - Remove Empregado")
        print("4 - Mostra um Empregado")
        print("5 - Mostra todos os Empregados")
        print("6 - Sair do menu de Empregados")

        opc = int( input("Digite uma opção: ") )
            
        if opc == 1:
            print("\n")
            insere_empregado(dic_empregado)
                
        elif opc == 2:
            print("\n")
            cpf = input("Digite o CPF do empregado: ")
            altera_empregado(dic_empregado,cpf)
                
        elif opc == 3:
            print("\n")
            cpf = input("Digite o CPF do empregado a ser removido: ")
            remove_empregado(dic_empregado,cpf)
                
        elif opc == 4:
            print("\n")
            cpf = input("Digite o CPF do empregado a ser consultado: ")
            mostra_empregado(dic_empregado,cpf)
            pausa()
                
        elif opc == 5:
            print("\n")
            mostra_todos_empregados(dic_empregado)
                
        elif opc == 6:
            grava_empregado(dic_empregado)

#fim do menu

