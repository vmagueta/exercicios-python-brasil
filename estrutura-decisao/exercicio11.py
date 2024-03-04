#! usr/bin/env python3

"""As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa
que calculará os reajustes.

- Faça um programa que recebe o salário de um colaborador e o reajuste segundo
o seguinte critério, baseado no salário atual:
- Salários até R$ 280,00 (incluindo) : aumento de 20%
- Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- Salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
- O salário antes do reajuste;
- O percentual de aumento aplicado;
- O valor do aumento;
- O novo salário, após o aumento.  """

salary = float(input("How much is the salary of the employee? "))

if salary < 280:
    print(f"The current salary is $ {salary:.2f}, it will be adjusted in 20%")
    new_salary = salary + (salary * (20/100))
    print(f"The raise in the salary is $ {(new_salary - salary):.2f}")
    print(f"The new salary is $ {new_salary:.2f}")
elif salary == 280 or salary < 700:
    print(f"The current salary is $ {salary:.2f}, it will be adjusted in 15%")
    new_salary = salary + (salary * (15/100))
    print(f"The raise in the salary is $ {(new_salary - salary):.2f}")
    print(f"The new salary is $ {new_salary:.2f}")
elif salary == 700 or salary < 1500:
    print(f"The current salary is $ {salary:.2f}, it will be adjusted in 10%")
    new_salary = salary + (salary * (10/100))
    print(f"The raise in the salary is $ {(new_salary - salary):.2f}")
    print(f"TThe new salary is $ {new_salary:.2f}")
elif salary >= 1500:
    print(f"The current salary is $ {salary:.2f}, it will be adjusted in 5%")
    new_salary = salary + (salary * (5/100))
    print(f"The raise in the salary is $ {(new_salary - salary):.2f}")
    print(f"The new salary is $ {new_salary:.2f}")
