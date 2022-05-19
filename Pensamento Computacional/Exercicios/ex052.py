"""Faça um programa que leia 5 números e informe o maior número."""

lista = []

for c in range(1, 6):
    numero = int(input(f"Digite o {c} numero: "))
    lista.append(numero)

sortear = lista.sort()
print(sortear)

