#! usr/bin/env python3

"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar
Dica: utilize o operador módulo (resto da divisão)."""

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
