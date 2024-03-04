#! usr/bin/env python3

"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letter = input("Type a letter: ")

vowels = ("aeiouáéíóúãẽõâêô")

if letter in vowels:
    print(f"The letter {letter} is a vowel.")
else:
    print(f"The letter {letter} is a consonant.")
