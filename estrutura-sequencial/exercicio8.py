#! usr/bin/env python3

"""Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.  """

valor = float(input("Quanto você ganha por hora? "))
hora = float(input("Quantas horas você trabalhou no mês? "))

salario = valor * hora
print(f"Você teve um salário de R$ {salario:.2f} este mês.")
