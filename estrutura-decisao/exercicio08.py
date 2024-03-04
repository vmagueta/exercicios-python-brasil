#! usr/bin/env python3

"""Faça um programa que pergunte o preço de três produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

prices = {
    "price 1": None,
    "price 2": None,
    "price 3": None,
}

for price in prices:
    prices[price] = float(input("Type the price of the product: "))

print(f"Você pode comprar o produto de valor {min(prices.values())}")
