#! usr/bin/env python3

"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média, o conceito
    correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
    ou “REPROVADO” se o conceito for D ou E."""

def final_decision():
    grade1, grade2 = grades
    print(f"""
    Grades:             {grade1}   |   {grade2}
    Average grade:      {grade_average}
    Concept:            {concept}
    Final Decision:     {final_grade}
    """)


grades = []
for i in range(1,3):
    grade = float(input("Enter with your grade: "))
    grades.append(grade)

grade_average = sum(grades) / len(grades)

if grade_average >= 0 and grade_average < 4:
    final_grade = "REPROVED!"
    concept = "E"
    final_decision()
elif grade_average >= 4 and grade_average < 6:
    final_grade = "REPROVED!"
    concept = "D"
    final_decision()
elif grade_average >= 6 and grade_average < 7.5:
    final_grade = "APPROVED."
    concept = "C"
    final_decision()
elif grade_average >= 7.5 and grade_average < 9:
    final_grade = "VERY WELL APPROVED!!!"
    concept = "B"
    final_decision()
elif grade_average >= 9 and grade_average <= 10:
    final_grade = "APPROVED WITH DISTINCTION!"
    concept = "A"
    final_decision()
else:
    print("You've done something wrong...")
