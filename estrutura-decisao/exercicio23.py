#! usr/bin/env python3

"""Faça um Programa que peça um número e informe se o número é inteiro ou
decimal. Dica: utilize uma função de arredondamento."""

numero = float(input("Digite um número: "))

if numero == round(numero):
    print(f"O número {numero:.0f} é inteiro.")
elif numero != round(numero):
    print(f"O número {numero} é decimal.")
