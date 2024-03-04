#! usr/bin/env python3

"""Faça um Programa que peça um número correspondente a um determinado ano
e em seguida informe se este ano é ou não bissexto."""

year = int(input("Enter a year: "))
years = list(range(0,2101, 100))

if year in years:
    print(year)
    if year % 400 != 0:
        print(f"O ano de {year} não é um ano bissexto")
    elif year % 400 == 0:
        print(f"O ano de {year} é um ano bissexto")
elif year not in years:
    if year % 4 == 0:
        print(f"O ano de {year} é um ano bissexto")
    elif year % 4 != 0:
        print(f"O ano de {year} não é um ano bissexto")
