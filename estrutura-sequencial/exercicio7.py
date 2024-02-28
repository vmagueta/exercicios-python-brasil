#! usr/bin/env python3

""" Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário."""

lados = {
    "lado 1": None,
    "lado 2": None,
}

for lado in lados:
    lados[lado] = int(input(f"Digite o {lado}: "))

area = lados["lado 1"] * lados["lado 2"]
print(f"O dobro da área é {area * 2}.")
