# Sistema de Gestão de Produtos e Pedidos

Este projeto é um sistema simples de gerenciamento de produtos e pedidos, com funcionalidades para clientes e administradores. O sistema permite o login, cadastro, visualização de pedidos, adição e remoção de produtos, e gerenciamento de carrinhos de compras.

## Funcionalidades

- **Login e Cadastro**: Usuários podem se cadastrar como "administrador" ou "cliente" e realizar login no sistema.
- **Menu de Administrador**:
  - Adicionar e remover produtos.
  - Visualizar pedidos feitos pelos clientes.
- **Menu de Cliente**:
  - Visualizar produtos disponíveis.
  - Adicionar e remover produtos do carrinho.
  - Finalizar pedidos.
  
## Estrutura do Projeto

O projeto é composto pelos seguintes componentes principais:

1. **Menu**: Responsável pela navegação entre os menus de administrador e cliente.
2. **Usuário**: Responsável pela autenticação, login e cadastro de usuários.
3. **Produto**: Gerencia os produtos disponíveis no sistema.
4. **Carrinho**: Gerencia o carrinho de compras do cliente.
5. **Pedido**: Gerencia os pedidos feitos pelos clientes.
6. **Banco de Dados (Arquivo JSON)**: Utiliza arquivos JSON para armazenar os dados de usuários, produtos e pedidos.

## Pré-requisitos

- Python 3
- Dependências:
  - `json` (biblioteca padrão do Python)

## Como Rodar o Projeto

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/SEU-USUARIO/PROJETO.git
