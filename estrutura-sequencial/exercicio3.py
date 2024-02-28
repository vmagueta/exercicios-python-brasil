#! usr/bin/env python3

"""Faça um Programa que peça dois números e imprima a soma."""

numbers = []
for num in range(1,3):
    num = int(input("Digite o número: "))
    numbers.append(num)

soma = numbers[0] + numbers[1]
print(f"A soma dos números é {soma}")
