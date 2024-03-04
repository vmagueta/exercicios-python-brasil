#! usr/bin/env python3

"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. """

sexo = input("Digite F se é feminino ou M se é masculino: ").strip().lower()

if sexo == "f":
    print(f"Você digitou {sexo.upper()} - Feminino.")
elif sexo == "m":
    print(f"Você digitou {sexo.upper()} - Masculino.")
else:
    print(f"Você digitou {sexo.upper()}, isto é inválido. Digite M ou F")
