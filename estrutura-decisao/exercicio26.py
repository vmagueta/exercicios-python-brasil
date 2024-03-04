#! usr/bin/env python3

"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:

- Álcool:
    Até 20 litros, desconto de 3% por litro;
    Acima de 20 litros, desconto de 5% por litro;
- Gasolina:
    Até 20 litros, desconto de 4% por litro;
    Acima de 20 litros, desconto de 6% por litro;

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor
a ser pago pelo cliente sabendo-se que o preço do  litro da gasolina é R$ 2,50
o preço do litro do álcool é R$ 1,90.  """

combustivel = input("Digite o combustível que foi abastecido: A-Álcool / G - Gasolina\n").lower()
litros = float(input(f"Quantos litros foram abastecidos? "))

if combustivel == "g":
    if litros <= 20:
        preco = litros * 2.50
        desconto = preco * 4/100
        preco = preco - desconto
        print(preco)
    elif litros > 20:
        preco = litros * 2.50
        desconto = preco * 6/100
        preco = preco - desconto
        print(preco)
elif combustivel == "a":
    if litros <= 20:
        preco = litros * 1.90
        desconto = preco * 3/100
        preco = preco - desconto
        print(preco)
    elif litros > 20:
        preco = litros * 1.90
        desconto = preco * 5/100
        preco = preco - desconto
        print(preco)
