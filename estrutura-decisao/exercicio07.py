#! usr/bin/env python3

"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

numbers = {
    "n1": None,
    "n2": None,
    "n3": None,
}

for number in numbers:
    numbers[number] = int(input("Type a number: "))

print(f"O maior número entre eles é o {min(numbers.values())}.")
