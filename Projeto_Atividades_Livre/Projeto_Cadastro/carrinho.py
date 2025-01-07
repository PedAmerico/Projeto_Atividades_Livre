import json
from produto import Produto

class Carrinho:
    def __init__(self, usuario):
        self.usuario = usuario
        self.itens = []

    def ver_produtos(self):
        produtos = Produto.carregar_produtos()
        if produtos:
            for produto in produtos:
                print(f"Produto: {produto.nome_produto}, Preço: {produto.preco_produto}")
        else:
            print("Nenhum produto disponível.")

    def adicionar_produto(self):
        nome = input("Digite o nome do produto que deseja adicionar: ")
        produtos = Produto.carregar_produtos()

        for produto in produtos:
            if produto.nome_produto == nome:
                self.itens.append(produto)
                print(f"{produto.nome_produto} adicionado ao carrinho.")
                return
        print("Produto não encontrado.")

    def remover_produto(self):
        nome = input("Digite o nome do produto que deseja remover: ")
        for produto in self.itens:
            if produto.nome_produto == nome:
                self.itens.remove(produto)
                print(f"{produto.nome_produto} removido do carrinho.")
                return
        print("Produto não encontrado no carrinho.")

    def finalizar_pedido(self):
        if not self.itens:
            print("Carrinho vazio! Adicione produtos antes de finalizar o pedido.")
            return

        pedido = {
            "cliente": self.usuario['nome'],
            "itens": [{"produto": p.nome_produto, "preco": p.preco_produto} for p in self.itens],
        }

        try:
            with open("pedidos.json", "r") as file:
                pedidos = json.load(file)
        except FileNotFoundError:
            pedidos = []

        pedidos.append(pedido)

        with open("pedidos.json", "w") as file:
            json.dump(pedidos, file, indent=4)

        print("Pedido finalizado com sucesso!")
        self.itens.clear()