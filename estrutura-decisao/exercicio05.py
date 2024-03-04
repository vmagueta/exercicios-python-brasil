#! usr/bin/env python3

"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

grades = []

for i in range(1,3):
    grade = float(input("Type your grade: "))
    grades.append(grade)

average = (grades[0] + grades[1]) / 2

if average == 10:
    print(f"You've been approved with distinction.")
elif average >= 7:
    print(f"You've been approved.")
elif average < 7:
    print(f"You've been reproved.")
