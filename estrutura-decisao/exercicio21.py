#! usr/bin/env python3

"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário a valor do saque e depois informar quantas notas de cada valor serão
fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar
com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de
100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de
100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

notas_disponiveis = [1, 5, 10, 50, 100]
valores_disponiveis = list(range(10, 601))

saque = int(input("Qual o valor do saque a ser feito? "))

if saque in valores_disponiveis:
    notas_100 = saque // 100
    if notas_100 <= 1:
        n100 = "nota"
    elif notas_100 >= 2:
        n100 = "notas"
    notas_50 = (saque - notas_100 * 100) // 50
    notas_10 = ((saque - notas_100 * 100) - (notas_50 * 50)) // 10
    if notas_10 <= 1:
        n10 = "nota"
    elif notas_10 >=2 and notas_10 < 5:
        n10 = "notas"
    notas_5 = ((saque - notas_100 * 100) - (notas_50 * 50) - (notas_10 * 10)) // 5
    notas_1 = ((saque - notas_100 * 100) - (notas_50 * 50) - (notas_10 * 10)) - (notas_5 * 5)
    if notas_1 <= 1:
        n1 = "nota"
    elif notas_1 >= 2:
        n1 = "notas"

    if notas_100:
        saida_100 = f"{notas_100} {n100} de 100,"
    else:
        saida_100 = ""
    if notas_50:
        saida_50 = "1 nota de 50,"
    else:
        saida_50 = ""
    if notas_10:
        saida10 = f"{notas_10} {n10} de 10,"
    else:
        saida10 = ""
    if notas_5:
        saida_5 = "1 nota de 5,"
    else:
        saida_5 = ""
    if notas_1:
        saida_1 = f"{notas_1} {n1} de 1."
    else:
        saida_1 = ""

    print(saida_100,saida_50,saida10,saida_5,saida_1)

else:
    print("O valor não está disponível para saque")
