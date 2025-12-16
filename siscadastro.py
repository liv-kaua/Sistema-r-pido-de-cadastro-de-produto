import time
lista_produtos = []

def cadastrar_produto():
    nome = input("Insira o nome do produto: ")
    codigo = input("Insira o código do produto: ")
    preço_str = input("Insira o preço do produto: R$")
    preço_formatado = preço_str.replace(".", ",") 
    try:
        preço = float(preço_formatado.replace(",", "."))
    except ValueError:
        print("\nErro! Formato de preço inválido. Use apenas números (com vírgula ou ponto!)\n")
        return
    marca = input("Insira a marca do produto: ")
    em_estoque = input("Há em estoque? (Digite S para sim e N para não!): ").lower()

    novo_produto = {
        "nome": nome,
        "codigo": codigo,
        "preço": preço,
        "marca": marca, 
        "em estoque": em_estoque,
    }
    lista_produtos.append(novo_produto)

def listar_produtos():
    if not lista_produtos: 
       print("A lista está vazia! Cadastre um produto primeiro.")
    else:
        print("Lista de produtos cadastrados:\n")
        for produto in lista_produtos:
            print(
                f"Nome: {produto['nome']} ID: {produto['codigo']} "
                f"Preço: R${produto['preço']} Marca: {produto['marca']} "
                f"Em estoque: {produto['em estoque']}" 
                  )
def menu():
    print("--- Menu Principal --- \n")
    print("1. Cadastrar produto\n2. Listar produtos (Ver estoque)\n3. Editar produto\n4. Sair do programa\n"
          )
    escolha = int(input("Escolha uma das funções desejadas (Digite apenas 1, 2, 3 ou 4!): "))
    return escolha

while True:
    escolha = menu()
    if escolha == 1:
        cadastrar_produto()
    elif escolha == 2:
        listar_produtos()
        time.sleep(5)
    elif escolha == 3:
        print("Ainda não foi adicionado esta opção!")
        time.sleep(5)
        pass
    elif escolha == 4:
        print("Programa encerrado!")
        break
    else:
        print("Entrada inválida! Digite apenas 1, 2, 3 ou 4. ")