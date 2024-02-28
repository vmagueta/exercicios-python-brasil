#! usr/bin/env python3

"""Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.
F = 9 / 5 * (C + 32)
"""

temp_cel = float(input("Digite a temperatura em Celsius: "))

temp_fah = ((9 / 5) * temp_cel) + 32
print(f"A temperatura {temp_cel}°C em Fahrenheit é {temp_fah}°F.")
