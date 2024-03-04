#! usr/bin/env python3

"""Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. I
mprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
conforme o caso."""

shifts = {
    "m": "Morning",
    "a": "Afternoon",
    "n": "Night"
}

shift = input("Which shift do you study? M/A/N\n").strip().lower()

if shift == "m":
    print(f"Good Morning! You study in the {shifts[shift]} shift.")
elif shift == "a":
    print(f"Goor Afternoon! You study in the {shifts[shift]} shift.")
elif shift == "n":
    print(f"Good Night! You study in the {shifts[shift]} shift.")
else:
    print(f"You typed '{shift}', that's a invalid value. Try m/a/n")
