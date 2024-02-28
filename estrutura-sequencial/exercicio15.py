#! usr/bin/env python3

"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

hora = float(input("Quantas horas você trabalha por mês? "))
valor = float(input("Quanto você ganha por hora? "))

salario_bruto = hora * valor
inss = salario_bruto * (8/100)
ir = salario_bruto * (11/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - inss - ir - sindicato

print(f"""Seu salário bruto é de R$ {salario_bruto:.2f};
Seu IR foi R$ {ir:.2f};
Seu INSS foi R$ {inss:.2f};
O Sindicato foi R$ {sindicato:.2f};
Portanto, seu salário líquido foi de R$ {salario_liquido:.2f}""")
