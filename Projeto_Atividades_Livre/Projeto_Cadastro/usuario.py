import json

import os
import json

class Usuario:
    @staticmethod
    def cadastrar_usuario(nome, email, senha, tipo_usuario, endereco):
        # Verifica se o arquivo 'usuarios.json' existe
        if not os.path.exists('usuarios.json'):
            # Cria o arquivo se não existir
            with open('usuarios.json', 'w') as file:
                json.dump([], file)
        
        # Abre o arquivo 'usuarios.json' para leitura
        with open('usuarios.json', 'r') as file:
            usuarios = json.load(file)

        # Adiciona o novo usuário à lista
        novo_usuario = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "tipo_usuario": tipo_usuario,
            "endereco": endereco
        }
        usuarios.append(novo_usuario)

        # Salva a lista de usuários novamente no arquivo
        with open('usuarios.json', 'w') as file:
            json.dump(usuarios, file)


    @staticmethod
    def login(email, senha):
        # Verifica se o arquivo de usuários existe
        if not os.path.exists('usuarios.json'):
            return None
        
        with open('usuarios.json', 'r') as file:
            usuarios = json.load(file)
        
        # Verifica se o email e senha estão corretos
        for usuario in usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                return usuario
        return None
