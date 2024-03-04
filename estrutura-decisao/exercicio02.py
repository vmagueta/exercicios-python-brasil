#! usr/bin/env python3

""" Faça um Programa que peça um valor e mostre na tela se
o valor é positivo ou negativo."""

number = float(input("Digite um número: "))

if number > 0:
    print(f"O número {number} é positivo.")
elif number < 0:
    print(f"O número {number} é negativo.")
