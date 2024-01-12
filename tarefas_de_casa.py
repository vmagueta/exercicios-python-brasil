#! usr/bin/env python
""" Esse programa tem como objetivo escolher a pessoa responsável
por determinada tarefa doméstica através de um sorteio.
"""
__version__ = "0.1.0"

import random

participantes = ["Kamila", "Victor"]
tarefas = {
    "Varre a Casa", 
    "Passar aspirador", 
    "Lavar Banheiros", 
    "Limpar a Cozinha", 
    "Lavar Roupas",
    "Limpar Áreas Comuns",
}

for tarefa in tarefas:
    print(f"O escolhido para a tarefa {tarefa} foi:")
    input("Aperte enter para sortear...\n")
    print(f"{random.choice(participantes)}\n")
