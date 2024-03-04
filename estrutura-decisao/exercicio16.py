#! usr/bin/env python3

"""Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações:

    - Se o usuário informar o valor de A igual a zero, a equação não é do segundo
    grau e o programa não deve pedir os demais valores, sendo encerrado;
    - Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;
    - Se o delta calculado for igual a zero a equação possui apenas uma raiz
    real; informe-a ao usuário;
    - Se o delta for positivo, a equação possui duas raiz reais;
    informe-as ao usuário;"""

def calcula(a, b, c):
    delta = ((b ** 2) - 4 * a * c) ** 0.5
    if delta < 0:
        print("O delta foi negativo {delta:.0f}, assim a equação não possui raízes reais.")
    elif delta == 0:
        x =  (-b + delta) / 2 * a
        return(f"O delta foi 0, sendo assim, só tem uma raíz {x:.0f}")
    elif delta > 0:
        x1 = (-b + delta) / 2 * a
        x2 = (-b - delta) / 2 * a
        return(f"O delta foi {delta:.0f}, sendo assim as raízes são {x1:.0f} e {x2:.0f}")


variables = {
    "a": None,
    "b": None,
    "c": None
}

for variable in variables:
    variables[variable] = int(input("Digite um número: "))
    if variables["a"] == 0:
        print("This is not a Second Degree Equation")
        break

print(calcula(variables["a"], variables["b"], variables["c"]))
