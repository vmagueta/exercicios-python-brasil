#! usr/bin/env python3

"""Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:

- Para homens: (72.7*h) - 58
- Para mulheres: (62.1*h) - 44.7
"""

h = input("Qual sua altura? \n")
genero = input("Você é homem ou mulher? h/m \n").strip().lower()

if genero == "h":
    peso_ideal_h = (72.7 * float(h)) - 58
    print(f"Seu peso ideal é {peso_ideal_h}")
elif genero == "m":
    peso_ideal_m = (68.1 * float(h) - 44.7)
    print(f"Seu peso ideal é {peso_ideal_m}")
else:
    print("Você digitou uma informação inválida.")
