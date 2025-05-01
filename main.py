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
    id = input("Digite o 'id'(identificador) do livro: " ) 
    #em banco de dados seria not null e chave primária
    titulo = input("Digite o título do livro: ").upper()
    autor = input("Digite o nome do autor: ").upper()
    ano = input("Digite o ano que o livro foi públicado: ")
    preco = input("Digite o preço do livro: ")
    preco = preco.replace("," , ".")
    preco = float(preco) 
    estoque = input("Digite quantos livros têm no estoque: ")
    estoque = int(estoque)

    livros.append((id, titulo, autor, ano, preco, estoque))
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


def cadastrar_compra():

def lista_compra():
    



#O menu vem depois das listas para não gerar um erro, já que as variáveis ainda vão ser declaradas

def menu():
    while True: #assim o código continua rodando até o usuário sair
        print("—" * 60)
        print(" MENU - LIVRARIA DAS CARTAS PERDIDAS".center(60))
        print("—" * 60)
        print('''
1. Cadastrar um novo livro
2. Lista de livros disponíveis
3. Excluir livro cadastrado
4. Cadastrar novo cliente
5. Lista de clientes cadastrados
6. Excluir cliente cadastrado
7. Registrar uma nova compra
8. Lista de compras 
9. Sair
       ''' )

        numero_menu = input("O que você deseja? ")


        if numero_menu == "1":
            cadastrar_livro()
        elif numero_menu == "2":
            lista_livro()
        elif numero_menu == "3":
            excluir_livro()
        elif numero_menu == "4":
            cadastrar_cliente()
        elif numero_menu == "5":
            lista_cliente()
        elif numero_menu == "6":
            excluir_cliente()
        elif numero_menu == "7":
            cadastrar_compra()
        elif numero_menu == "8":
            lista_compra()
        elif numero_menu == "9":
            print("Obrigada pela prefrência. Volte sempre!")
            break
        else:
            print("Essa opção não existe. Tente novamente, por favor.")

       

boas_vindas()
menu()