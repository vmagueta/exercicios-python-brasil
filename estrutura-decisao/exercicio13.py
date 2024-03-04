#! usr/bin/env python3

"""Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer
valor inválido."""

week_days = {
    '1': "Sunday",
    '2': "Monday",
    '3': "Tuesday",
    '4': "Wednesday",
    '5': "Thursday",
    '6': "Friday",
    '7': "Saturday",
}

day = input("Type a number to receive a day of the week: ")

if day not in week_days.keys():
    print("Deu merda")
else:
    print(f"{day} - {week_days[day]}.")
