#! usr/bin/env python3

""" Faça um Programa para uma loja de tintas. O programa deverá pedir o
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- Comprar apenas latas de 18 litros;
- Comprar apenas galões de 3,6 litros;
- Misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias."""

area = int(input("Qual o tamanho da área a ser pintada? "))
area = area + (area * 10/100)
litros_tinta = area / 6
latas = litros_tinta // 18
galoes = litros_tinta // 3.6
print(f"Você precisará de {litros_tinta:.1f} litros de tinta para pintar uma área de {area:.1f} m², contando com os 10% de folga.")

if litros_tinta % 18 != 0:
    latas += 1
    preco = latas * 80
    print(f"Se comprar apenas latas, você precisará de {latas:.0f} latas e custará R$ {preco:.2f}.")

if litros_tinta % 3.6 != 0:
    galoes += 1
    preco = galoes * 25
    print(f"Se comprar apenas Galões, você precisará de {galoes:.0f} galões e custará R$ {preco:.2f}")

latas = None
galoes = None

# misturando os dois
if litros_tinta < 18:
    galoes = litros_tinta / 3.6
    print(galoes)
    print("yes")
if litros_tinta >= 18:
    latas = litros_tinta // 18
    resto = litros_tinta % 18
    galoes = resto // 3.6
    if resto % 3.6 != 0:
        galoes += 1

    preco = (latas * 80) + (galoes * 25)

print(f"""Para você ter o menor desperdiço de tinta possível, você pode levar da seguinte forma:
- {latas:.0f} lata(s);
- {galoes:.0f} galão(ões);

Isso dará um total de R$ {preco:.2f}.
""")
