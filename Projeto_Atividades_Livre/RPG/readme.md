# Sistema de RPG com Personagens

Este projeto é um jogo de RPG simples onde você pode criar personagens de diferentes classes, lutar contra outros personagens e salvar os dados dos personagens em um arquivo JSON. O sistema oferece a possibilidade de criar personagens, listar personagens salvos, realizar combates entre eles e salvar o progresso no final.

## Funcionalidades

- **Criação de Personagens**: O jogador pode criar um personagem e escolher entre três classes: Guerreiro, Mago ou Arqueiro.
- **Combate**: Dois personagens podem lutar entre si, utilizando suas habilidades e atributos.
- **Salvar Personagens**: O progresso do jogo pode ser salvo em um arquivo JSON, permitindo que você continue a jogar depois.
- **Carregar Personagens**: Os personagens salvos podem ser carregados e utilizados novamente para novas batalhas.

## Classes

O sistema possui as seguintes classes de personagens:

- **Personagem**: Classe base com atributos comuns como nome, vida, mana, ataque, defesa e status de vida.
- **Guerreiro**: Subclasse de `Personagem`, com alto ataque e defesa, mas baixa mana.
- **Mago**: Subclasse de `Personagem`, com grande quantidade de mana e habilidades mágicas.
- **Arqueiro**: Subclasse de `Personagem`, com boa combinação de ataque e defesa, focado em ataques de longo alcance.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

1. **`personagem.py`**: Contém as classes `Personagem`, `Guerreiro`, `Mago`, e `Arqueiro`, com seus métodos de ataque, defesa e reviver, e executa o arquivo.
2. **`personagens.json`**: Arquivo JSON onde os personagens criados são salvos para persistência de dados.

