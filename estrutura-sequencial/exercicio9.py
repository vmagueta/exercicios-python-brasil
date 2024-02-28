#! usr/bin/env python3

"""Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

temp_celsius = 5 * ((temp_fahrenheit - 32) / 9)
print(f"A temperatura {temp_fahrenheit}°F em celsius é {temp_celsius:.1f}°C.")
