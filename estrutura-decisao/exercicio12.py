#! usr/bin/env python3

"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde
ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor
da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
    Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00
"""

def salary_print():
    print(f"""
    Gross salary: ({hours:.0f} * {value:.0f}) : $ {gross_salary:.2f}
    (-) IR ({ir}%)             : $ {ir_value:.2f}
    (-) INSS (10%)           : $ {inss:.2f}
    (-) Syndicate (3%)       : $ {syndicate:.2f}
    FGTS (11%)               : $ {fgts:.2f}
    Total of Discounts       : $ {discounts:.2f}
    Net Salary               : $ {salary:.2f}
    """)


hours = float(input("How many hours do you work? "))
value = float(input("How much money do you receive for hour?"))

gross_salary = hours * value
inss = gross_salary * (10/100)
syndicate = gross_salary * (3/100)
fgts = gross_salary * (11/100)

if gross_salary <= 900:
    ir = 0
    ir_value = 0
    discounts = ir + inss + syndicate
    salary = gross_salary - ir - inss - syndicate
    salary_print()
elif gross_salary <= 1500:
    ir = 5
    ir_value = gross_salary * 5/100
    discounts = ir + inss + syndicate
    salary = gross_salary - ir - inss - syndicate
    salary_print()
elif gross_salary <= 2500:
    ir = 10
    ir_value = gross_salary * 10/100
    discounts = ir + inss + syndicate
    salary = gross_salary - ir - inss - syndicate
    salary_print()
elif gross_salary > 2500:
    ir = 20
    ir_value = gross_salary * 20/100
    discounts = ir + inss + syndicate
    salary = gross_salary - ir - inss - syndicate
    salary_print()
