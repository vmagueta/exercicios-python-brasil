#! usr/bin/env python3

"""Faça um Programa que peça 2 números inteiros e um número real. C
Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.
"""
num_int1 = int(input("Digite um número inteiro: "))
num_int2 = int(input("Digite outro número inteiro: "))
num_flt = float(input("Digite um número real /  ponto flutuante: "))

op1 = (2 * num_int1) + (num_int2 / 2)
op2 = (3 * num_int1) + num_flt
op3 = num_flt ** 3

print(f"""
- O produto do dobro do primeiro com metade do segundo é {op1}.
- A soma do triplo do primeiro com o terceiro é {op2}.
- O terceiro elevado ao cubo é {op3}.
"""
)
