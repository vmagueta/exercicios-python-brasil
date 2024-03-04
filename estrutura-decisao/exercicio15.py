#! usr/bin/env python3

"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um
triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;"""

triangulo = False
lados = []
for i in range(1,4):
    lados.append(int(input("Digite o valor do lado do triangulo: ")))


lado1, lado2, lado3 = lados
if lados[0] + lados[1] > lados[2]:
    print(f"{lado1}, {lado2}, {lado3} formam um triângulo.")
    triangulo = True
elif lados[0] + lados[2] > lados[1]:
    print(f"{lado1}, {lado2}, {lado3} formam um triângulo.")
    triangulo = True
elif lados[1] + lados[2] > lados[0]:
    print(f"{lado1}, {lado2}, {lado3} formam um triângulo.")
    triangulo = True
else:
    print(f"{lado1}, {lado2}, {lado3} não formam um triângulo.")

if triangulo:
    lado1, lado2, lado3 = lados
    if lado1 == lado2 and lado1 == lado3:
        print("Inclusive, este é um triângulo equilátero")
    elif lado1 == lado2 and lado1 != lado3:
        print("Inclusive, este é um triângulo isóceles")
    elif lado1 == lado3 and lado1 != lado2:
        print("Inclusive, este é um triângulo isóceles")
    elif lado2 == lado3 and lado2 != lado1:
        print("Inclusive, este é um triângulo isóceles")
    else:
        print("Inclusive, este é um triângulo escaleno")
