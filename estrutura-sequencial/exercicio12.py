#! usr/bin/env python3

"""Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58  """

altura = input("Digite sua altura em metros para descobrir seu peso ideal: \n")

peso_ideal = (72.7 * float(altura)) - 58
print(f"Para sua altura de {altura}m, seu peso ideal é {peso_ideal:.1f} kg.")
