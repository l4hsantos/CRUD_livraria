livros = [] #entidade principal (título, id, autor, ano, preço, estoque)
clientes = [] #entidade principal(nome, cpf, email, telefone)
compras = [] #entidade negócio (liga livros e clientes)
    #as listas ("[]") guardam TODOS os itens



def boas_vindas():
    print("—" * 60) #estilização de título
    print("     BEM-VINDO À LIVRARIA DAS CARTAS PERDIDAS".center(60))
    print("—" * 60)
    print(" Um lugar onde cada livro possui uma história esperando para ser reencontrada.\nA sua próxima grande aventura está a uma página de distância.")
    print()


def cadastrar_livro():
    print("\n Cadastre o livro seguindo os dados abaixo")
    print("Alerta: O 'id' só deve possuir números")
    IDF = input("Digite o 'id'(identificador) do livro: " ) 
    #em banco de dados seria not null e chave primária
    titulo = input("Digite o título do livro: ").upper()
    autor = input("Digite o nome do autor: ").upper()
    ano = input("Digite o ano que o livro foi públicado: ")
    preco = input("Digite o preço do livro: ")
    preco = preco.replace("," , ".")
    preco = float(preco) 
    estoque = input("Digite quantos livros têm no estoque: ")
    estoque = int(estoque)

    livros.append((IDF, titulo, autor, ano, preco, estoque))
    print(f"\nO cadastro do livro '{titulo}' foi realizado.")

def lista_livro(): 
    if not livros:
        print("\nNenhum livro foi cadastrado\n")
    else:
        print("\nLivros cadastrados:\n ")
        for livro in livros:
            print(f"ID: {livro[0]}")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Ano de publicação: {livro[3]}")
            print(f"Preço: {livro[4]}")
            print(f"Estoque: {livro[5]} unidades disponíveis")
            print("—" * 40)

def alterar_livro():
    while True:
        livro_alterar = input("Digite o 'id'(indicador) do livro que você deseja alterar: ")
        for livro in livros:
            IDF, titulo, autor, ano, preco, estoque = livro
            if IDF == livro_alterar:
                print(f"Título: {titulo}, Autor: {autor}, Ano de publicação: {ano}, Preço: {preco}, Estoque: {estoque}")

                novo_titulo = input("Qual o novo título? ").upper()
                novo_autor = input("Qual o novo autor? ").upper()
                novo_ano = input("Qual o novo ano de publicação? ")
                novo_preco = input("Qual o novo preço? ")
                novo_preco = novo_preco.replace(",",".")
                novo_preco = float(novo_preco)
                novo_estoque = input("Qual o novo estoque? ")
                novo_estoque = int(novo_estoque)

                confirma = input("Para confirmar digite (1), para cancelar digite (0): ")
                confirma = int(confirma)
                if confirma == 1:
                    livros[livros.index(livro)] = (IDF, novo_titulo, novo_autor, novo_ano, novo_preco, novo_estoque)
                    print(f"\nO livro foi alterado com sucesso!\nTítulo: {novo_titulo}, Autor: {novo_autor}, Ano: {novo_ano}, Preço: R${novo_preco}, Estoque: {novo_estoque}, ID: {ID}")
                else:
                    print("A alteração foi cancelada.")
                return  

        print(f"O livro com o 'id'(identificador) {livro_alterar} não foi encontrado. Tente novamente!")
        

def excluir_livro():
    excluir_id = input("Digite o 'id'(identificador) do livro que você deseja excluir: ")

    for i in range(len(livros)): #len = quantidade de livros cadastrados
        if livros[i][0] == excluir_id:
            del livros[i] 
            print("O livro foi excluído. Se quiser adicioná-lo novamente precisa cadastrar(2)\n")
            return
        print("O 'id'(identificador) digitado não foi encontrado. Tente novamente")

#A linha do for i in range está percorrendo toda a lista "livros"
#A var "i" gera um índice que começa no 0 até a quantidade de livros -1, permitindo acessá-los individualmente 
#livros[i][0] acessa o PRIMEIRO valor da tupla, que é o id, e se somente se, for igual ao digitado pelo usuário, o livro será excluído
#del livros[i] exclui o livro de acordo com o livro encontrado

def cadastrar_cliente():
    print("\nCadastre o cliente de acordo com os dados abaixo")
    print("Alerta: o CPF deve conter 11 dígitos!")
    while True:
        cpf = input("Digite o CPF do cliente: ")
        if len(cpf) == 11 and cpf.isdigit():
            formato_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            print(f"O CPF foi formatado: {formato_cpf}")
            break
        else:
            print("CPF inválido. Confira a quantidade de números.")
    
    nome = input("Digite o nome completo do cliente: ").upper()
    email = input("Digite o email do cliente: ").upper()

    while True:
        print("Alerta: o telefone deve conter o DDD do estado")
        telefone = input("Digite o telefone do cliente: ")
        if len(telefone) == 11 and telefone.isdigit():
            formato_telefone = f"({telefone[:2]}) {telefone[2:3]}{telefone[3:7]}-{telefone[7:]}"
            print(f"Telefone foi formatado: {formato_telefone}")
            break
        else:
            print("Telefone inválido. Confira a quantidade de números.")
    
    cliente = (formato_cpf, nome, email, formato_telefone)
    clientes.append(cliente)
    print(f"\nO(a) cliente {nome} foi cadastrado(a)!\n") 

def lista_cliente():
    if not clientes:
        print("\nNenhum cliente foi cadastrado\n")
    else:
         print("\nLista de clientes cadastrados:\n ")
         for cliente in clientes:
            print(f"Nome: {cliente[0]}")
            print(f"CPF: {cliente[1]}")
            print(f"Email: {cliente[2]}")
            print(f"Telefone: {cliente[3]}")
            print("—" * 40)

def alterar_cliente():
    while True:
        cpf = input("Digite o CPF (Cadastro de Pessoa Física) do cliente que deseja alterar: ")
        if len(cpf) != 11:
            print("CPF inválido. Confira a quantidade de números.")
            continue  # volta para o início do laço

        formato_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        
        for CLIENTE in clientes:
            if CLIENTE[0] == formato_cpf:
                print(f"CPF: {CLIENTE[0]}, Nome: {CLIENTE[1]}, Email: {CLIENTE[2]}, Telefone: {CLIENTE[3]}")
                
                novo_nome = input("Qual o novo nome completo? ").upper()
                novo_email = input("Qual o novo email? ").upper()
                print("Alerta: o telefone deve ser inserido junto com o DDD")
                telefone = input("Qual o novo telefone? ")

                if len(telefone) != 11:
                    print("Telefone inválido. Confira a quantidade de dígitos.")
                    return

                formato_telefone = f"({telefone[:2]}) {telefone[2:3]}{telefone[3:7]}-{telefone[7:]}"
                confirma = input("Para confirmar digite (1), para cancelar digite (0): ")

                if confirma == "1":
                    clientes[clientes.index(CLIENTE)] = (formato_cpf, novo_nome, novo_email, formato_telefone)
                    print(f"\nO cliente foi alterado com sucesso!\nCPF: {formato_cpf}, Nome: {novo_nome}, Email: {novo_email}, Telefone: {formato_telefone}")
                else:
                    print("A alteração foi cancelada.")
                return
        
        print(f"O cliente com CPF {cpf} não foi encontrado. Tente novamente.")

def excluir_cliente():
    excluir_cpf = input("Digite o CPF do cliente que você deseja excluir: ")
    
    cpf_normal = excluir_cpf.replace(".", "").replace("-", "")
     
    if len(cpf_normal) == 11:
        
        formato_cpf = f"{cpf_normal[:3]}.{cpf_normal[3:6]}.{cpf_normal[6:9]}-{cpf_normal[9:]}"
        
#Antes de adicionar o cpf_normal, o usuário era obrigado a digitar o cpf com 14 dígitos,
#Agora, o próprio código formata novamente para apagar, corrigindo possíveis complicações

        for c in range(len(clientes)):
            if clientes[c][0] == formato_cpf:
                del clientes[c]
                print("O cadastro do cliente foi apagado. Se quiser adicioná-lo novamente, realize o cadastro (opção 2).\n")
                return
        
        print("O CPF (Cadastro de Pessoa Física) digitado não foi encontrado. Tente novamente.")
    else:
        print("CPF inválido. Ele deve conter 11 dígitos numéricos.")

import datetime

def cadastrar_compra():

    print("\nREGISTRAR COMPRA - LIVRARIA DAS CARTAS PERDIDAS\n")
 
    print("ALERTA: O CPF deve conter 11 números")
    cpf = input("Digite o CPF (Cadastro de Pessoa Física) do cliente: ")
    if len(cpf) != 11:
        print("CPF inválido. Digite novamente.")
        return

    formato_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    achar_cliente = None
    for CLIENTE in clientes:
        if CLIENTE[0] == formato_cpf: #índice do cpf
            achar_cliente = CLIENTE
            break

    if not achar_cliente:
        print("O cliente não foi encontrado. Tente novamente.")
        return

    IDF = input("Digite o 'id'(identificador) do livro que deseja comprar: ")
    achar_livro = None
    for LIVRO in livros: #índice do ID
        if LIVRO[0] == IDF:
            achar_livro = LIVRO
            break

    if not achar_livro:
        print("O livro não foi encontrado. Tente novamente.")
        return

    qnt = input("Digite a quantidade de livros que deseja comprar: ")
    qnt = int(qnt)

    if qnt > achar_livro[5]:  # [5] é o índice do estoque
        print("Desculpe, estoque insuficiente.")
        return

    preco = achar_livro[4]  # [4] é o índice do preço
    total = preco * qnt
    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M") #data exata com mês, dia, ano e hora

    novo_estoque = achar_livro[5] - qnt #diminuir a quantidade do estoque na lista livros
    livros[livros.index(achar_livro)] = (*achar_livro[:5], novo_estoque) #o * desempacota para alterar um valor
    #se não usar o * você cria uma tupla dentro de outra tupla

    compras.append((formato_cpf, IDF, qnt, preco, total, data))
   
    print("—" * 50)
    print("\nNOTA FISCAL - LIVRARIA DAS CARTAS PERDIDAS")
    print("—" * 50)
    print(f"Data: {data}")
    print(f"Cliente: {achar_cliente[1]}")
    print(f"CPF: {formato_cpf}")
    print(f"Livro: {achar_livro[1]} - {achar_livro[2]}")
    print(f"Quantidade: {qnt}")
    print(f"Preço: R${preco}")
    print("—" * 50)
    print(f"Total: R${total}")
    print("—" * 50)
    print("Obrigada pela compra. Volte sempre!\nOnde sua próxima aventura está a uma página de distância!")

def lista_compra():
    print("—"*60)
    print("\nREGISTRO DE COMPRAS - LIVRARIA DAS CARTAS PERDIDAS")
    print("—"*60)

    if not compras:
        print("Nenhuma compra foi registrada.")
        return
    for COMPRA in compras:
        formato_cpf, IDF, qnt, preco, total, data = COMPRA

        for CLIENTE in clientes:
            if CLIENTE[0] == formato_cpf:
                nome = CLIENTE[1].upper()
                break
        
        IDF = COMPRA[1]

        for LIVRO in livros:
            if LIVRO[0] == IDF:
                titulo = LIVRO[1]
                autor = LIVRO[2]
                break
        
        print(f"Data: {data}")
        print(f"Cliente: {nome}")
        print(f"Livro: {titulo}")
        print(f"Quantidade: {qnt}")
        print(f"Preço: {preco}")
        print(f"Total: R${total}")
        print("—"*60)

def alterar_compra():
    print("—"*60)
    print("\nALTERAR COMPRA - LIVRARIA DAS CARTAS PERDIDAS")
    print("—"*60)
    
    cpf = input("Digite o CPF do cliente para alterar a compra: ")
    formato_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
  

    achar_compra = None
    for compra in compras: 
        if compra[0] == formato_cpf:
            achar_compra = compra
            break
    
    if not achar_compra:
        print("A compra não encontrada por esse CPF.")
        return

    print("\nA compra foi achada!")
    print(f"Cliente: {achar_compra[0]}")
    print(f"Livro: {achar_compra[1]}")
    print(f"Quantidade: {achar_compra[2]}")
    print(f"Preço: {achar_compra[3]}")
    print(f"Total: {achar_compra[4]}")


    alterar = input("\nO que você deseja alterar? 1- quantidade 2- preço): ").upper()

    listar_compra = list(achar_compra)

    if alterar == "1":
        nova_qnt = input("Digite a nova quantidade: ")
        nova_qnt = int(nova_qnt)
        listar_compra[2] = nova_qnt
        listar_compra[4] = listar_compra[3] * nova_qnt  #atualiza o total
        print("A quantidade foi alterada com sucesso!")

    elif alterar == "2":
        novo_preco = input("Digite o novo preço: ")
        novo_preco = float(novo_preco)
        listar_compra[3] = novo_preco
        listar_compra[4] = novo_preco * listar_compra[2]  #atualiza o total
        print("O preço foi alterado com sucesso!")

    else:
        print("Opção inválida. Tente novamente.")

    compras[compras.index(achar_compra)] = tuple(listar_compra)

    print("—"*60)
    print(f"Compra atualizada: {listar_compra}")

def exluir_compra():
    
    print("—"*60)
    print("\nEXCLUIR COMPRA - LIVRARIA DAS CARTAS PERDIDAS")
    print("—"*60)
    
    cpf = input("Digite o CPF(Cadastro de Pessoa Física) do cliente para excluir a compra: ")
    formato_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
  
    achar_compra = None
    for compra in compras: #usa a lista
        if compra[0] == formato_cpf:
            achar_compra = compra
            break
    
    if not achar_compra:
        print("A compra não foi encontrada por esse CPF.")
        return

    print("\nA compra foi achada!")
    print(f"Cliente: {achar_compra[0]}")
    print(f"Livro: {achar_compra[1]}")
    print(f"Quantidade: {achar_compra[2]}")
    print(f"Preço: {achar_compra[3]}")
    print(f"Total: {achar_compra[4]}")

    confirmar = input("\Para cancelar digite(1) e se não quiser cancelar digite(2): ").upper()

    if confirmar == '1':
        del compras[0]
        print("A compra foi excluída com sucesso!")
    else:
        print("A exclusão foi cancelada.")

    print("—"*60)


#O menu vem depois das listas para não gerar um erro, já que as variáveis ainda vão ser declaradas

def menu():
    while True: #assim o código continua rodando até o usuário sair
        print("—" * 60)
        print(" MENU - LIVRARIA DAS CARTAS PERDIDAS".center(60))
        print("—" * 60)
        print('''

1. Cadastrar um novo livro
2. Lista de livros disponiveis
3. Alterar dados de livros
4. Excluir livro cadastrado
5. Cadastrar novo cliente
6. Lista de clientes cadastrados
7. Alterar dados de clientes
8. Excluir cliente cadastrado
9. Registrar uma nova compra
10. Lista de compras
11. Alterar compras
12. Excluir compras
0. Sair

       ''' )

        numero_menu = input("O que você deseja? ")


        if numero_menu == "1":
            cadastrar_livro()
        elif numero_menu == "2":
            lista_livro()
        elif numero_menu == "3":
            alterar_livro()
        elif numero_menu == "4":
            exluir_livro()
        elif numero_menu == "5":
            cadastrar_cliente()
        elif numero_menu == "6":
            lista_cliente()
        elif numero_menu == "7":
            alterar_cliente()
        elif numero_menu == "8":
            excluir_cliente()
        elif numero_menu == "9":
            cadastrar_compra()
        elif numero_menu == "10":
            lista_compra()
        elif numero_menu == "11":
            alterar_compra()
        elif numero_menu == "12":
            exluir_compra()
        elif numero_menu == "0":
            print("—" * 60)
            print("—" * 60)
            print("╔══════════════════════════════════╗")
            print("║  ⌨️ 𝓞𝓫𝓻𝓲𝓰𝓪𝓭𝓪 𝓹𝓮𝓵𝓪 𝓹𝓻𝓮𝓯𝓮𝓻𝓮𝓷𝓬𝓲𝓪   ║")
            print(" Nossas páginas estarão sempre abertas para você.")
            print("║                                  ║")
            print("║  VOLTE QUANDO O SEU CORAÇÃO PEDIR POR NOVAS HISTÓRIAS!  ║")
            print("║   ✍️ ONDE A SUA PRÓXIMA GRANDE AVENTURA ESTÁ A UMA PÁGINA DE DISTÂNCIA║")
            print("║                                  ║")
            print("╚══════════════════════════════════╝")
           
            print("────────────⌨️ LIVRARIA DAS CARTAS PERDIDAS")
            print("—" * 60)
            break
        else:
            print("Essa opção não existe. Tente novamente, por favor.")

       

boas_vindas()
menu()