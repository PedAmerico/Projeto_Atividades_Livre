import json
from pedido import Pedido
from usuario import Usuario
from produto import Produto
from carrinho import Carrinho

class Menu:
    def __init__(self):
        self.usuario_logado = None

    def exibir_menu(self):
        while True:
            print("Escolha uma opção (1-3):")
            print("1. Login")
            print("2. Cadastro")
            print("3. Sair")

            opcao = input("Digite sua opção: ")

            if opcao == "1":
                if self.login():
                    return
            elif opcao == "2":
                self.cadastro()
            elif opcao == "3":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")

    def login(self):
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        usuario = Usuario.login(email, senha)

        if usuario:
            self.usuario_logado = usuario
            print(f"\nLogin bem-sucedido! Bem-vindo, {usuario['nome']}")
            self.exibir_opcoes(usuario)
            return True
        else:
            print("Email ou senha incorretos!")
            return False

    def cadastro(self):
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        tipo_usuario = input("Digite o tipo de usuário (administrador/cliente): ")
        endereco = input("Digite seu endereço (somente para clientes): ")

        Usuario.cadastrar_usuario(nome, email, senha, tipo_usuario, endereco)
        print(f"Usuário {nome} cadastrado com sucesso!")

    def exibir_opcoes(self, usuario):
        if usuario['tipo_usuario'] == 'administrador':
            self.exibir_menu_administrador()
        elif usuario['tipo_usuario'] == 'cliente':
            self.exibir_menu_cliente()

    def exibir_menu_administrador(self):
        while True:
            print("\nMenu do Administrador:")
            print("1. Adicionar Produto")
            print("2. Remover Produto")
            print("3. Visualizar Pedidos")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_produto()
            elif opcao == "2":
                self.remover_produto()
            elif opcao == "3":
                self.visualizar_pedidos()
            elif opcao == "4":
                print("Saindo do menu do administrador...")
                self.exibir_menu()
            else:
                print("Opção inválida!")

    def exibir_menu_cliente(self):
        carrinho = Carrinho(self.usuario_logado)
        while True:
            print("\nMenu do Cliente:")
            print("1. Ver Produtos")
            print("2. Adicionar Produto ao Carrinho")
            print("3. Remover Produto do Carrinho")
            print("4. Finalizar Pedido")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                carrinho.ver_produtos()
            elif opcao == "2":
                carrinho.adicionar_produto()
            elif opcao == "3":
                carrinho.remover_produto()
            elif opcao == "4":
                carrinho.finalizar_pedido()
                break
            elif opcao == "5":
                print("Saindo do menu do cliente...")
                self.exibir_menu()
            else:
                print("Opção inválida!")

    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        produto = Produto(nome, preco)
        produto.adicionar_produto()
        print(f"Produto {nome} adicionado com sucesso!")

    def remover_produto(self):
        nome = input("Digite o nome do produto a ser removido: ")
        Produto.remover_produto(nome)
        print(f"Produto {nome} removido com sucesso!")

    def visualizar_pedidos(self):
        try:
            with open("pedidos.json", "r") as arquivo:
                pedidos = json.load(arquivo)  # Carrega os pedidos do arquivo JSON

            if pedidos:
                for pedido in pedidos:
                    print(f"Cliente: {pedido['cliente']} - Itens: {', '.join(pedido['itens'])}")
            else:
                print("Nenhum pedido encontrado.")
        except FileNotFoundError:
            print("Arquivo de pedidos.json não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de pedidos. Verifique se o JSON está formatado corretamente.")
