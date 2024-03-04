#! usr/bin/env python3

"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
5% sobre o total da compra.

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário
e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade
de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar."""

carne = input("Qual o tipo de carne que será comprada? ").strip().lower()
quilos = int(input("Quantos quilos estão sendo comprados? "))
forma_pagamento = input("Será pago com o Cartão Tabajara? ").strip().lower()

if carne == "file":
    if quilos <= 5:
        preco = 4.90
        valor = quilos * preco
        print(valor)
    elif quilos > 5:
        preco = 5.80
        valor = quilos * preco
        print(valor)
elif carne == "alcatra":
    if quilos <= 5:
        preco = 5.90
        valor = quilos * preco
        print(valor)
        print("5.90 A")
    elif quilos > 5:
        preco = 6.80
        valor = quilos * preco
        print(valor)
        print("6.80 A")
elif carne == "picanha":
    if quilos <= 5:
        preco = 6.90
        valor = quilos * preco
        print(valor)
        print("6.90 P")
    elif quilos > 5:
        preco = 7.80
        valor = quilos * preco
        print(valor)
        print("7.80 P")

if forma_pagamento == "sim":
    desconto = valor * 0.05
    valor_total = valor - desconto
    print(f"""
    ~~~~~~~~~~ CUPOM FISCAL ~~~~~~~~~~
    {carne.capitalize()} R$ {preco:.2f} x {quilos} kg = R$ {valor:.2f}

    Tipo de pagamento = Cartão Tabajara

    Valor = R$ {valor:.2f}
    Desconto = R$ {desconto:.2f}
    Valor Total a ser pago = R$ {valor_total:.2f}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
elif forma_pagamento == "não" or forma_pagamento == "nao":
    print(f"""
    ~~~~~~~~~~ CUPOM FISCAL ~~~~~~~~~~
    {carne.capitalize()} R$ {preco:.2f} x {quilos} kg = R$ {valor:.2f}

    Tipo de pagamento = Convencional

    Valor = R$ {valor:.2f}
    Desconto = R$ 0,00
    Valor Total a ser pago = R$ {valor:.2f}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
