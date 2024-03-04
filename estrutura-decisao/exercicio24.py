#! usr/bin/env python3

"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar. O resultado da operação deve ser acompanhado de
uma frase que diga se o número é:

    - par ou ímpar;
    - positivo ou negativo;
    - inteiro ou decimal."""

def operacoes(operacao, numeros):
    n1, n2 = numeros
    if operacao == "sum":
        return(sum(numeros))
    elif operacao == "sub":
        return(n1 - n2)
    elif operacao == "mul":
        return(n1 * n2)
    elif operacao == "div":
        return(n1 / n2)

def par_impar(resultado):
    if resultado % 2 == 0:
        return("par")
    elif resultado % 2 != 0:
        return("impar")

def positivo_negativo(resultado):
    if resultado < 0:
        return("negativo")
    elif resultado > 0:
        return("positivo")

def inteiro_decimal(resultado):
    if resultado == round(resultado):
        return("inteiro")
    elif resultado != round(resultado):
        return("decimal")


numeros = []
operacoes_disponiveis = ["sum", "sub", "mul", "div"]

for i in range(1,3):
    numeros.append(float(input("Digite um número: ")))

operacao = input("Digite a operação que deseja realizar: [sum/sub/mul/div] ").strip().lower()
if operacao not in operacoes_disponiveis:
    print("Você digitou uma operação inválida.")

resultado = operacoes(operacao, numeros)
pa_im = par_impar(resultado)
po_ne = positivo_negativo(resultado)
in_de = inteiro_decimal(resultado)

print(f"O número {resultado} é {pa_im}, é {po_ne} e também é {in_de}.")
