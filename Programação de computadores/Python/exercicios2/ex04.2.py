'''Faça um programa que lê 4 números reais em uma lista, calcula e exibe a quantidade de números negativos e a soma dos números positivos dessa mesma lista;'''
import numpy as np

numeros = []
for c in range(4):
    num = float(input('Digite um valor: '))
    numeros.append(num)

numeros = np.array(numeros)
quantNegativos = len(numeros[numeros<0])
somaPositivos = sum(numeros[numeros>0])

print(f'Quantidade de numeros negativos: {quantNegativos}\nSoma dos numeros positivos: {somaPositivos}')