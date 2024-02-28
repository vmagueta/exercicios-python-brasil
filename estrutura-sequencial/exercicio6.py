#! usr/bin/env python3

""" Faça um Programa que peça o raio de um círculo,
calcule e mostre sua área. """

import math

raio = float(input("Digite o tamanho do raio do círculo: "))

area = math.pi * (raio ** 2)
print(f"A área do círculo é {area:.2f}")
