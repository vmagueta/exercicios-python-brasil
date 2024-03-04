#! usr/bin/env python3

"""Faça um Programa que leia um número inteiro menor que 1000 e imprima
a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11,
1, 7 e 16"""

import sys

numero = int(input("Digite um número de 0 até 999: "))

if numero < 0 or numero > 1000:
    print(f"Você digitou {numero}, este número é inválido")
    sys.exit(1)

else:
    centena = numero // 100
    dezena = (numero - centena * 100) // 10
    decimal = ((numero - centena * 100) - dezena * 10)

    # centena
    if centena >= 2:
        centena_ = "centenas"
    elif centena == 1:
        centena_ = "centena"
    else:
        centena_ = 0

    # dezena
    if dezena >= 2:
        dezena_ = "dezenas"
    elif dezena == 1:
        dezena_ = "dezena"
    else:
        dezena_ = 0

    #decimal
    if decimal >= 2:
        decimal_ = "unidades"
    elif decimal == 1:
        decimal_ = "unidade"
    else:
        decimal_ = 0

    if centena and dezena and decimal:
        print(f"{centena} {centena_}, {dezena} {dezena_} e {decimal} {decimal_}")
    elif centena and dezena:
        print(f"{centena} {centena_} e {dezena} {dezena_}")
    elif centena and decimal:
        print(f"{centena} {centena_} e {decimal} {decimal_}")
    elif dezena and decimal:
        print(f"{dezena} {dezena_} e {decimal} {decimal_}")
    elif centena:
        print(f"{centena} {centena_}")
    elif dezena:
        print(f"{dezena} {dezena_}")
    elif decimal:
        print(f"{decimal} {decimal_}")
    else:
        print("Você digitou 0")
