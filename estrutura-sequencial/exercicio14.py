#! usr/bin/env python3

"""João Papo-de-Pescador, homem de bem, comprou um microcomputador
para controlar o rendimento diário de seu trabalho. Toda vez que ele traz
um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado
de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além
do limite e na variável multa o valor da multa que João deverá pagar.

Imprima os dados do programa com as mensagens adequadas."""

peso_peixe = float(input("Digite o peso do peixe: "))

if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa = excesso * 4
    print(f"Você teve um excesso de {excesso:.1f}kg, por isso pagará R$ {multa:.2f} de multa.")
elif peso_peixe <= 50:
    print(f"O peso do peixe foi de {peso_peixe}kg, e está dentro das normas.")
else:
    print("Você digitou algo errado.")
