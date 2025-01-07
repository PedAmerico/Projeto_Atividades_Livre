# Projeto_Cadastro e RPG

Este repositório contém dois projetos independentes:

1. **Projeto_Cadastro**: Um sistema simples de cadastro de usuários, com funcionalidades de login, criação de contas e armazenamento de dados em formato JSON.
2. **RPG**: Um jogo de RPG em que os jogadores podem criar personagens, lutar contra outros e salvar o progresso.

## Projetos

### 1. Projeto_Cadastro

O **Projeto_Cadastro** é um sistema básico de cadastro de usuários e administração. O projeto permite que o usuário crie uma conta, faça login e interaja com um menu de opções. O sistema armazena as informações dos usuários em um arquivo JSON, e as funcionalidades incluem a verificação de credenciais de login e o gerenciamento de dados de usuários.

#### Funcionalidades:
- **Cadastro de Usuários**: Permite criar um novo usuário com nome, email e senha.
- **Login**: Usuários podem fazer login utilizando suas credenciais (email e senha).
- **Verificação de Credenciais**: O sistema valida os dados de login e permite que os usuários acessem a plataforma.
- **Armazenamento em JSON**: As informações dos usuários são salvas em um arquivo JSON, para fácil persistência e leitura.

### 2. Sistema de RPG com Personagens

O segundo projeto é um jogo de **RPG** onde o jogador pode criar personagens de diferentes classes (Guerreiro, Mago e Arqueiro), lutar contra outros personagens e salvar o progresso em um arquivo JSON.

#### Funcionalidades:
- **Criação de Personagens**: Criação de personagens de três classes (Guerreiro, Mago e Arqueiro).
- **Combate**: O jogador pode iniciar combates entre dois personagens, usando habilidades específicas de cada classe.
- **Salvar Personagens**: O progresso do jogo pode ser salvo e carregado posteriormente.
- **Carregar Personagens**: Permite carregar os personagens salvos para novos combates.

#### Classes:
- **Personagem**: Classe base que define atributos comuns como vida, mana, ataque e defesa.
- **Guerreiro**: Subclasse focada em ataques físicos e alta defesa.
- **Mago**: Subclasse com habilidades mágicas e grande quantidade de mana.
- **Arqueiro**: Subclasse com ataques de longo alcance e boa defesa.

