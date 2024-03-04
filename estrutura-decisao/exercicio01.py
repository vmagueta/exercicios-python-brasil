#! usr/bin/env python3

""" Faça um Programa que peça dois números e imprima o maior deles."""

numbers = []

for i in range(1,3):
    number = int(input("Digite um número: "))
    numbers.append(number)

if numbers[0] > numbers[1]:
    print(f" O maior número é o {numbers[0]}")
elif numbers[0] < numbers[1]:
    print(f"O maior número é o {numbers[1]}")
