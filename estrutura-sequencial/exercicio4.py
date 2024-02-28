#! usr/bin/env python3
""" Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

notas = {
    "nota 1": None,
    "nota 2": None,
    "nota 3": None,
    "nota 4": None,
}

for nota in notas:
    notas[nota] = int(input("Digite a nota: "))

media = (notas[nota] + notas[nota] + notas[nota] + notas[nota]) / 4
print(media)
