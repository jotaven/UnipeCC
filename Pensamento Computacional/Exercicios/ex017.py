'''
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas 
de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima,
    isto é, considere latas cheias.
'''
from math import ceil

areaPintada = float(input("Digite a area a ser pintada(m²): "))
litros = areaPintada/6
latas = int(litros // 18)
galoes = ceil((litros % 18) / 3.6)
precoTotal = latas*80 + galoes*25
print(f"Será necessario comprar {latas} Latas e {galoes} Galões, custando um total de R${precoTotal:.2f}")

