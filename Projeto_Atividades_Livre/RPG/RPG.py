import json

# Classes do RPG (modelo de Personagem, Guerreiro, Mago, Arqueiro)
class Personagem:
    def __init__(self, nome: str, vida: int, mana: int, ataque: int, defesa: int):
        self.__nome = nome
        self.__vida = vida
        self.__mana = mana
        self.__ataque = ataque
        self.__defesa = defesa
        self.__vivo = True

    @property
    def nome(self):
        return self.__nome

    @property
    def vivo(self):
        return self.__vivo

    def atacar(self, outro):
        pass

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
            self.__vivo = False

    def reviver(self):
        self.__vida = 100
        self.__mana = 50
        self.__vivo = True

    def __str__(self):
        return f"{self.__nome} (Vida: {self.__vida}, Mana: {self.__mana}, Ataque: {self.__ataque}, Defesa: {self.__defesa}, Vivo: {'Sim' if self.__vivo else 'Não'})"

class Guerreiro(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, vida=150, mana=30, ataque=50, defesa=40)

    def atacar(self, outro):
        dano = max(0, self._Personagem__ataque - outro._Personagem__defesa)
        outro.receber_dano(dano)
        return f"{self.nome} atacou {outro.nome} causando {dano} de dano."

class Mago(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, vida=100, mana=100, ataque=40, defesa=30)

    def atacar(self, outro):
        dano = max(0, self._Personagem__ataque + self._Personagem__mana // 10 - outro._Personagem__defesa)
        outro.receber_dano(dano)
        return f"{self.nome} atacou {outro.nome} causando {dano} de dano com magia."

class Arqueiro(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, vida=120, mana=50, ataque=45, defesa=35)

    def atacar(self, outro):
        dano = max(0, self._Personagem__ataque - outro._Personagem__defesa)
        outro.receber_dano(dano)
        return f"{self.nome} atacou {outro.nome} causando {dano} de dano com arco."

# Funções principais do jogo
def criar_personagem():
    nome = input("Digite o nome do personagem: ")
    print("Escolha a classe:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Arqueiro")
    classe = input("Digite o número da classe: ")

    if classe == "1":
        return Guerreiro(nome)
    elif classe == "2":
        return Mago(nome)
    elif classe == "3":
        return Arqueiro(nome)
    else:
        print("Classe inválida. Tente novamente.")
        return criar_personagem()

def combate(personagem1, personagem2):
    print(f"Iniciando combate entre {personagem1.nome} e {personagem2.nome}!")
    while personagem1.vivo and personagem2.vivo:
        print(personagem1.atacar(personagem2))
        if not personagem2.vivo:
            print(f"{personagem1.nome} venceu o combate!")
            break
        print(personagem2.atacar(personagem1))
        if not personagem1.vivo:
            print(f"{personagem2.nome} venceu o combate!")
            break

def salvar_personagens(personagens, arquivo="personagens.json"):
    data = [{"nome": p.nome, "classe": p.__class__.__name__} for p in personagens]
    with open(arquivo, "w") as f:
        json.dump(data, f)

def carregar_personagens(arquivo="personagens.json"):
    try:
        with open(arquivo, "r") as f:
            data = json.load(f)
            personagens = []
            for p in data:
                if p["classe"] == "Guerreiro":
                    personagens.append(Guerreiro(p["nome"]))
                elif p["classe"] == "Mago":
                    personagens.append(Mago(p["nome"]))
                elif p["classe"] == "Arqueiro":
                    personagens.append(Arqueiro(p["nome"]))
            return personagens
    except FileNotFoundError:
        return []

def menu():
    personagens = carregar_personagens()
    while True:
        print("\nMenu do RPG:")
        print("1. Criar Personagem")
        print("2. Listar Personagens")
        print("3. Iniciar Combate")
        print("4. Salvar e Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            personagens.append(criar_personagem())
        elif opcao == "2":
            if not personagens:
                print("Nenhum personagem criado.")
            for p in personagens:
                print(p)
        elif opcao == "3":
            if len(personagens) < 2:
                print("Crie pelo menos dois personagens para iniciar o combate.")
                continue
            print("Selecione os personagens para o combate:")
            for i, p in enumerate(personagens):
                print(f"{i + 1}. {p}")
            try:
                escolha1 = int(input("Digite o número do primeiro personagem: ")) - 1
                escolha2 = int(input("Digite o número do segundo personagem: ")) - 1
                combate(personagens[escolha1], personagens[escolha2])
            except (ValueError, IndexError):
                print("Seleção inválida. Tente novamente.")
        elif opcao == "4":
            salvar_personagens(personagens)
            print("Personagens salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()