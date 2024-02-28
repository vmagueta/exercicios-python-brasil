#! usr/bin/env python3

"""Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos)."""

tamanho = float(input("Qual o tamanho do arquivo em MB? "))
velocidade = int(input("Qual a velocidade da sua internet em Mbps? "))

tempo = (tamanho * 8) / velocidade
print(f"O seu arquivo de {tamanho} MB será baixado em {tempo:.1f} segundos.")
