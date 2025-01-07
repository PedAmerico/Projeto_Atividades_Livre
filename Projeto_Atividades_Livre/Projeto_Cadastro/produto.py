import json

class Produto:
    def __init__(self, nome_produto, preco_produto):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto

    @staticmethod
    def salvar_produtos(produtos):
        with open('produtos.json', 'w') as file:
            json.dump([produto.__dict__ for produto in produtos], file, indent=4)

    @staticmethod
    def carregar_produtos():
        try:
            with open('produtos.json', 'r') as file:
                produtos_data = json.load(file)
                return [Produto(produto["nome_produto"], produto["preco_produto"]) for produto in produtos_data]
        except FileNotFoundError:
            return []

    def adicionar_produto(self):
        produtos = Produto.carregar_produtos()
        produtos.append(self)
        Produto.salvar_produtos(produtos)

    @staticmethod
    def remover_produto(nome):
        produtos = Produto.carregar_produtos()
        produtos = [p for p in produtos if p.nome_produto != nome]
        Produto.salvar_produtos(produtos)