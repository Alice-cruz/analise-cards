# Identificador de Tipo de Cartão de Crédito

Este projeto é um script em Python que identifica o tipo de um cartão de crédito com base no número informado. Ele verifica o número do cartão em relação a prefixos e comprimentos pré-definidos para diferentes tipos de cartões, como MasterCard, Visa, American Express, entre outros.

## Como Funciona

1. O script define um dicionário com os tipos de cartões, cada um contendo:
   - **Prefixos**: Os dígitos iniciais do número do cartão.
   - **Comprimentos**: Os comprimentos válidos do número do cartão.

2. A função `get_card_type`:
   - Remove os espaços do número do cartão informado.
   - Verifica se o número corresponde a um prefixo e comprimento válidos para algum tipo de cartão.
   - Retorna o tipo do cartão caso encontre uma correspondência ou "Tipo de Cartão Desconhecido" caso contrário.

3. O usuário insere o número do cartão, e o script exibe o tipo identificado.

## Como Usar

1. Execute o script no terminal:
   ```bash
   python index.py