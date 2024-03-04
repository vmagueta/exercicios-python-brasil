#! usr/bin/env python3

"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente"."""

respostas = {
    "Telefonou para a vítima?": None,
    "Esteve no local do crime?": None,
    "Mora perto da vítima?": None,
    "Devia para a vítima?": None,
    "Já trabalhou com a vítima?": None,
}

for resposta in respostas.keys():
    print(resposta)
    respostas[resposta] = input("Sua resposta: ").strip().lower().replace('ã', 'a')
    if respostas[resposta] == "sim":
        respostas[resposta] = True
    elif respostas[resposta] == "nao":
        respostas[resposta] = False

quantidade_true = []
for resposta in respostas.values():
    if resposta == True:
        quantidade_true.append(resposta)
    else:
        continue

if len(quantidade_true) == 0 or len(quantidade_true) == 1:
    print("Você foi definido como 'Inocente', obrigado pelos esclarecimentos.")
elif len(quantidade_true) == 3 or len(quantidade_true) == 4:
    print("Você foi definido como 'Cúmplice' e está preso!")
elif len(quantidade_true) == 2:
    print("Você foi definido como 'Suspeito', ficaremos de olho...")
elif len(quantidade_true) == 5:
    print("Você foi descoberto como 'Assassino' e está preso!!")
