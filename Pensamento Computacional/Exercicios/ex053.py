"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

lista = []

for c in range(1,6):
    numero = int(input(f"Digite o {c} numero: "))
    lista.append(numero)

soma = sum(lista)
media = soma/len(lista)

print(f"A soma é {soma} e a média é de {media}")