import json
from datetime import datetime

class Pedido:
    def __init__(self, usuario, itens):
        self.usuario = usuario
        self.itens = itens
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.numero_pedido = self.gerar_numero_pedido()
        self.status = "Em processamento"

    def gerar_numero_pedido(self):
        # Gerar um número único para o pedido (poderia ser um contador simples ou UUID)
        return f"PEDIDO_{self.usuario['email']}_{self.data.replace('-', '').replace(' ', '_').replace(':', '')}"

    def salvar_pedido(self):
        # Salva o pedido no arquivo de pedidos
        pedidos = Pedido.carregar_pedidos()
        pedidos[self.numero_pedido] = {
            "usuario": self.usuario['nome'],
            "itens": self.itens,
            "data": self.data,
            "status": self.status
        }
        with open("pedidos.json", "w") as file:
            json.dump(pedidos, file, indent=4)
        print(f"Pedido {self.numero_pedido} foi salvo com sucesso!")

    @staticmethod
    def carregar_pedidos():
        try:
            with open("pedidos.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def finalizar_pedido(usuario, itens):
        pedido = Pedido(usuario, itens)
        pedido.salvar_pedido()
        print(f"Pedido {pedido.numero_pedido} finalizado para {usuario['nome']}!")

    def ver_pedido(self):
        print(f"Detalhes do pedido {self.numero_pedido}:")
        print(f"Cliente: {self.usuario['nome']}")
        print(f"Data do Pedido: {self.data}")
        print("Itens do Pedido:")
        for item in self.itens:
            print(f"- {item['nome_produto']} - Preço: {item['preco_produto']}")
        print(f"Status: {self.status}")