#! usr/bin/env python3

"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

numbers = []

for i in range(1,4):
    i = int(input("Type a number: "))
    numbers.append(i)

numbers_ordered = sorted(numbers)
print(list(reversed(numbers_ordered)))
