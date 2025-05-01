livros = [] #entidade principal (título, id, autor, ano, preço, estoque)
clientes = [] #entidade principal(nome, cpf, email, telefone)
compras = [] #entidade negócio (liga livros e clientes)
    #as listas ("[]") guardam TODOS os itens



def boas_vindas():
    print("—" * 60) #estilização de título
    print("     BEM-VINDO À LIVRARIA DAS CARTAS PERDIDAS".center(60))
    print("—" * 60)
    print(" Um lugar onde cada livro possui uma história esperando para ser reencontrada,\n a sua próxima grande aventura está a uma página de distância.")
    print()


def cadastrar_livro():
    print("\n Cadastre o livro seguindo os dados abaixo")
    print("Alerta: O ID só deve possuir números")
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
    nome = input("Digite o nome completo do cliente: ").upper()
    print("Alerta: o CPF deve ser conter os pontos e traços, totalizando 14 caracteres")
    #em BD essa seria a chave primária da entidade cliente e not null (14)
    cpf = input("Digite o CPF do cliente: ")
    email = input("Digite o email do cliente: ").upper()
    print("Alerta: o telefone deve conter o DDD do estado")
    telefone = input("Digite o telefone do cliente: ")

    if len(telefone) == 11:
        formato_telefone = f"({telefone[:2]}) {telefone[2:3]}{telefone[3:7]}-{telefone[7:]}"
#[:2] separa o DDD, [2:3] o "9" da frente, [3:7] os 4 números antes do tracinho, [7:] os 4 últimos números 
#O : é o slicing(fatiamento) de string, que é usado coom base nas posições do caracteres
      
        print(f"Telefone fomratado: {formato_telefone}")
    else:
        print("Telefone inválido. Confira a quantidade de números")

    clientes.append((nome, cpf, email, formato_telefone))
    print(f"\nO(a) cliente {nome} foi cadastrado(a)!\n")



def lista_cliente():

def excluir_cliente():

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