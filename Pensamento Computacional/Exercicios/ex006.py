'''
Exercicio 006
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''

from math import pi

raio = float(input('Digite o valor do raio em m: '))

areaDoCirculo = 2*pi*(raio**2)

print(f'A area do círculo é igual a {areaDoCirculo:.2f}m²')