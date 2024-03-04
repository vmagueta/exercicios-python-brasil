#! usr/bin/env python3

"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.  """

morangos = int(input("Quantos quilos foram comprados de morangos? "))
macas = int(input("Quantos quilos foram comprados de maçãs? "))

frutas = macas + morangos

if morangos <= 5:
    preco_morangos = 2.5
elif morangos > 5:
    preco_morangos = 2.20

if macas <= 5:
    preco_macas = 1.80
elif macas > 5:
    preco_macas = 1.50

valor = (macas * preco_macas) + (morangos * preco_morangos)

if valor > 25 or frutas > 8:
    valor_final = valor - (valor * 0.1)
    print(f"O valor a ser pago era de R$ {valor}, porém, com o desconto de 10%, tornou-se R$ {valor_final:.2f}")
else:
    print(f"O valor a ser pago é de R$ {valor:.2f}")
