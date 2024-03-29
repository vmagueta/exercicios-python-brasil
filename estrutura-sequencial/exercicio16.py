#! usr/bin/env python3

"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
tinta a serem compradas e o preço total."""

area = int(input("Qual o tamanho da área a ser pintada? "))

litros = area / 3
latas = round(litros / 18)
preco = latas * 80
print(f"Para pintar uma área de {area}m² você precisará de {latas} lata(s) de tinta")
print(f"O preço total foi de R$ {preco:.2f}")
