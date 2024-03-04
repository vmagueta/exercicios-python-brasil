#! usr/bin/env python3

"""Faça um Programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida.  """

import sys

date = input("Enter a date in format [dd]: ").strip()
if int(date) < 0 or int(date) > 31:
    print("Você digitou uma data inválida. Apenas datas de 1 a 31.")
    sys.exit(1)
elif int(date) < 10:
    date = "0" + date
month = input("Enter a month in format [mm]: ").strip()
if int(month) < 0 or int(month) > 12:
    print("Você digitou um mês inválido. Apenas meses de 1 a 12")
    sys.exit(1)
elif int(month) < 10:
    month = "0" + month
year = input("Enter a year in format [aaaa]: ").strip()
if int(year) < 0:
    print("Você digitou um ano inválido. Apenas anos de 0 acima.")
    sys.exit(1)
elif int(year) < 10:
    year = "000" + year
elif int(year) < 100:
    year = "00" + year
elif int(year) < 1000:
    year = "0" + year

print(f"{date}/{month}/{year} é uma data válida!")
