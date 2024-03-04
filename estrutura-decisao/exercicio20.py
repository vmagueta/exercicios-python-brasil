#! usr/bin/env python3

"""Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:

- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva
média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva
média alcançada;
- A mensagem "Aprovado com Distinção", se a média for igual a 10."""

notas = []

for i in range(1,4):
    notas.append(float(input("Digite sua nota: ")))

media = (sum(notas)) / len(notas)

if media >= 7 and media < 10:
    print(f"Você foi aprovado com uma média de {media:.1f}")
elif media < 7 and media > 0:
    print(f"Você foi reprovado com uma média de {media:.1f}")
elif media == 10:
    print(f"Você passou com distinção com uma média {media:.1f}")
