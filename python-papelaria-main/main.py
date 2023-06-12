import os
import json
import zipfile
from Service.UsuarioService import UsuarioService
from Service.ProdutosService import ProdutosService
from Service.VendaService import VendaService
from Service.SobreService import SobreService
from Service.APIViaCepService import APIViaCepService

usuarioService = UsuarioService()
produtoService = ProdutosService()
vendaService = VendaService()
sobreService = SobreService()
apiViaCepService = APIViaCepService(14010030)

#-------------------Clear-------------------------------
def clearConsole():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)
#------------------------------------------------------

#-------------------APIViaCepService-------------------------------
def apiViaCep():
    lojaLocation = apiViaCepService.getLojaLocation()
    print(lojaLocation)
    input("Pressione Enter para continuar...")
#------------------------------------------------------

#-------------------Zip-------------------------------

def exportarDados():
    # Consultar e obter os dados das tabelas do banco de dados
    dados_usuarios = usuarioService.getAll()  # Supondo que você tenha uma função para obter todos os usuários
    dados_produtos = produtoService.getAll()  # Supondo que você tenha uma função para obter todos os livros
    dados_vendas = vendaService.getAll()  # Supondo que você tenha uma função para obter todas as vendas

    dados_usuarios_json = [usuario.to_dict() for usuario in dados_usuarios]
    dados_produto_json = [produto.to_dict() for produto in dados_produtos]
    dados_vendas_json = [venda.to_dict() for venda in dados_vendas]

    # Salvar os dados JSON em arquivos temporários
    with open('usuarios.json', 'w') as arquivo_usuarios:
        json.dump(dados_usuarios_json, arquivo_usuarios, indent=4)

    with open('produto.json', 'w') as arquivo_produto:
        json.dump(dados_produto_json, arquivo_produto, indent=4)

    with open('vendas.json', 'w') as arquivo_vendas:
        json.dump(dados_vendas_json, arquivo_vendas, indent=4)

    # Compactar os arquivos JSON em um arquivo ZIP
    with zipfile.ZipFile('dados.zip', 'w') as zip_file:
        zip_file.write('usuarios.json')
        zip_file.write('produto.json')
        zip_file.write('vendas.json')

    # Remover os arquivos JSON temporários
    os.remove('usuarios.json')
    os.remove('produto.json')
    os.remove('vendas.json')
#------------------------------------------------------

#-------------------Login-------------------------------

def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    usuarios = usuarioService.getAll()
    for usuario in usuarios:
        if usuario.email == email and usuario.senha == senha:
            print("Login bem-sucedido!")
            input("Pressione Enter para continuar...")
            return True
    print("Email ou senha incorretos!")
    input("Pressione Enter para continuar...")
    return False

def registro():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    usuarioService.criarUsuario(nome, email, senha)
    print("Usuário registrado com sucesso!")
#--------------------------------------------------

#-------------------Função de Usuarios------------------
def criarUsuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")
    usuarioService.criarUsuario(nome, email, senha)
    print(f"Usuario criado com sucesso!!!")
    input("Pressione Enter para continuar...")

def deletarUsuario():
    id_usuario = int(input("Digite o Id do usuario para deletar: "))
    usuarioService.deleteUsuario(id_usuario)
    print(f"Produto deletado com sucesso!!!")
    input("Pressione Enter para continuar...")

def getAllUsuarios():
    usuarios = usuarioService.getAll()
    for usuario in usuarios:
         print(f"Nome: {usuario.nome}")
         print(f"Email do Usuario: {usuario.email}")
         print(f"Senha do Usuario: {usuario.senha}")
         print(f"|----------------------------------------|")
    input("Pressione Enter para continuar...")

def getByIdUsuario():
    id_usuario = int(input("Digite o Id do usuario para buscar o usuario: "))
    usuario = usuarioService.getById(id_usuario)
    print(f"Nome: {usuario.nome}")
    print(f"Email do usuario: {usuario.email}")
    print(f"Senha do Usuario: {usuario.senha}")
    input("Pressione Enter para continuar...")

def atualizarUsuario():
    id_usuario = input("Digite o Id do usuario para atualizar: ")
    nome = input("Digite o novo nome do usuario: ")
    email = input("Digite o novo email do usuario: ")
    senha = input("Digite o novo senha do senha: ")
    usuarioService.updateUsuario(id_usuario, nome, email, senha)

#--------------------------------------------------

#-------------------Função de Produtos------------------
def criarProduto():
    nome = input("Digite o nome do produto: ")
    preco_venda = input("Digite o preço da venda do produto: ")
    preco_compra = input("Digite o preço da compra do produto: ")
    grupo = input("Digite o grupo do produto: ")
    quantidade_em_estoque = input("Quantidade em estoque: ")
    produtoService.criarProduto(nome, preco_venda, preco_compra, grupo, quantidade_em_estoque)
    print(f"Produto criado com sucesso!!!")
    input("Pressione Enter para continuar...")

def deletarProduto():
    id_produto = int(input("Digite o Id do produto para deletar: "))
    produtoService.deleteProduto(id_produto)
    print(f"Produto deletado com sucesso!!!")
    input("Pressione Enter para continuar...")

def getAllProdutos():
    produtos = produtoService.getAll()
    for produto in produtos:
         print(f"Nome: {produto.nome}")
         print(f"Preço de venda: {produto.preco_venda}")
         print(f"Preço de compra: {produto.preco_compra}")
         print(f"Grupo: {produto.grupo}")
         print(f"Quantidade em estoque: {produto.quantidade_em_estoque}")
         print(f"|----------------------------------------|")
    input("Pressione Enter para continuar...")
    produtos = []

def getByIdProdutos():
    id_produto = int(input("Digite o Id do produto para buscar o produto: "))
    produto = produtoService.getById(id_produto)
    print(f"Nome: {produto.nome}")
    print(f"Preço de venda: {produto.preco_venda}")
    print(f"Preço de compra: {produto.preco_compra}")
    print(f"Grupo: {produto.grupo}")
    print(f"Quantidade em estoque: {produto.quantidade_em_estoque}")
    input("Pressione Enter para continuar...")

def atualizarProduto():
    id_produto = input("Digite o Id do produto para atualizar: ")
    nome = input("Digite o novo nome do produto: ")
    preco_venda = input("Digite o novo preço de venda do produto: ")
    preco_compra = input("Digite o novo preço de compra do produto: ")
    grupo = input("Digite o novo grupo do produto: ")
    quantidade_em_estoque = input("Digite a nova quantidade em estoque: ")
    produtoService.updateProduto(id_produto, nome, preco_venda, preco_compra, grupo, quantidade_em_estoque)
#--------------------------------------------------

#-------------------Função de Venda---------------
def criarVenda():
    id_usuario = int(input("Digite o Id do Usuario: "))
    id_produto = int(input("Digite o Id do produto: "))
    quantidade_comprada = int(input("Digite a quantidade comprada "))
    data_compra = input("Digite a data da compra: ")
    valor_total = int(input("Digite o valor total: "))
    vendaService.criarVenda(id_usuario, id_produto, quantidade_comprada, data_compra, valor_total)
    print(f"Venda criada com sucesso!!!")
    input("Pressione Enter para continuar...")

def deletarVenda():
    id_venda = int(input("Digite o Id da venda para deletar: "))
    vendaService.deleteVenda(id_venda)
    print(f"Venda deletada com sucesso!!!")
    input("Pressione Enter para continuar...")

def getAllVenda():
    vendas = vendaService.getAll()
    for venda in vendas:
         print(f"Id de Usuario: {venda.id_usuario}")
         print(f"Id de Produto: {venda.id_produto}")
         print(f"Quantidade Comprada: {venda.quantidade_comprada}")
         print(f"Data de Compra: {venda.data_compra}")
         print(f"Valor Total: {venda.valor_total}")
         print(f"|----------------------------------------|")
    input("Pressione Enter para continuar...")
    clearConsole()

def getByIdVenda():
    id_venda = int(input("Digite o Id da venda para buscar a venda: "))
    venda = vendaService.getById(id_venda)
    print(f"Id de Usuario: {venda.id_usuario}")
    print(f"Id de Produto: {venda.id_produto}")
    print(f"Quantidade Comprada: {venda.quantidade_comprada}")
    print(f"Data de Compra: {venda.data_compra}")
    print(f"Valor Total: {venda.valor_total}")
    input("Pressione Enter para continuar...")

def atualizarVenda():
    id_venda = input("Digite o Id da venda para atualizar: ")
    id_produto = input("Digite o novo Id do produto: ")
    id_usuario = input("Digite o novo Id do usuario: ")
    quantidade_comprada = input("Digite a nova quantidade de compra: ")
    data_compra = input("Digite a nova data de compra: ")
    valor_total = input("Digite o novo valor total: ")
    vendaService.updateVenda(id_venda, id_produto, id_usuario, quantidade_comprada, data_compra, valor_total)
#--------------------------------------------------

#-------------------Função do Sobre---------------
def getAllSobre():
    sobre = sobreService.getAll()
    for sobre in sobre:
         print(f"Sobre o Aplicativo: {sobre.sobre}")
    input("Pressione Enter para continuar...")
#--------------------------------------------------

while True:
    clearConsole()
    print("\n1. Login")
    print("2. Registrar")
    print("3. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        if login():
            while True:
                clearConsole()
                print("\n1. Gerenciar Usuários")
                print("2. Gerenciar Produtos")
                print("3. Gerenciar Vendas")
                print("4. Sobre Projeto")
                print("5. Código Postal")
                print("6. Exportar todos os dados JSON")
                print("7. Sair")
    
                opcao = input("\nEscolha uma opção: ")
    
                if opcao == '1':
                    while True:
                        clearConsole()
                        print("\n1. Ver todos os usuários")
                        print("2. Ver um usuário")
                        print("3. Criar um usuário")
                        print("4. Atualizar um usuário")
                        print("5. Remover um usuário")
                        print("6. Voltar ao menu principal")

                        opcao_usuario = input("\nEscolha uma opção: ")

                        if opcao_usuario == '1':
                            clearConsole()
                            getAllUsuarios()
                            pass
                        elif opcao_usuario == '2':
                            clearConsole()
                            getByIdUsuario()
                            pass
                        elif opcao_usuario == '3':
                            clearConsole()
                            criarUsuario()
                            pass
                        elif opcao_usuario == '4':
                            clearConsole()
                            atualizarUsuario()
                            pass
                        elif opcao_usuario == '5':
                            clearConsole()
                            deletarUsuario()
                            pass
                        elif opcao_usuario == '6':
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    pass
                elif opcao == '2':
                    while True:
                        clearConsole()
                        print("\n1. Ver todos os produto")
                        print("2. Ver um produto")
                        print("3. Criar um produto")
                        print("4. Atualizar um produto")
                        print("5. Remover um produto")
                        print("6. Voltar ao menu principal")

                        opcao_usuario = input("\nEscolha uma opção: ")

                        if opcao_usuario == '1':
                            clearConsole()
                            getAllProdutos()
                            pass
                        elif opcao_usuario == '2':
                            clearConsole()
                            getByIdProdutos()
                            pass
                        elif opcao_usuario == '3':
                            clearConsole()
                            criarProduto()
                            pass
                        elif opcao_usuario == '4':
                            clearConsole()
                            atualizarProduto()
                            pass
                        elif opcao_usuario == '5':
                            clearConsole()
                            deletarProduto()
                            pass
                        elif opcao_usuario == '6':
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    pass
                elif opcao == '3':
                    while True:
                        clearConsole()
                        print("\n1. Ver todas as vendas")
                        print("2. Ver uma venda")
                        print("3. Criar venda")
                        print("4. Atualizar uma venda")
                        print("5. Remover uma venda")
                        print("6. Voltar ao menu principal")

                        opcao_usuario = input("\nEscolha uma opção: ")

                        if opcao_usuario == '1':
                            clearConsole()
                            getAllVenda()
                            pass
                        elif opcao_usuario == '2':
                            clearConsole()
                            getByIdVenda()
                            pass
                        elif opcao_usuario == '3':
                            clearConsole()
                            criarVenda()
                            pass
                        elif opcao_usuario == '4':
                            clearConsole()
                            atualizarVenda()
                            pass
                        elif opcao_usuario == '5':
                            clearConsole()
                            deletarVenda()
                            pass
                        elif opcao_usuario == '6':
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    pass
                elif opcao == '4':
                    clearConsole()
                    getAllSobre()
                    pass
                elif opcao == '5':
                    clearConsole()
                    apiViaCep()
                    pass
                elif opcao == '6':
                    clearConsole()
                    exportarDados()
                    pass
                elif opcao == '7':
                    print("Saindo do programa.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            continue
    elif opcao == '2':
        registro()
    elif opcao == '3':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")