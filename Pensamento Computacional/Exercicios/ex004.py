'''
Exercicio 004
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terceiro bimestre: '))
n4 = float(input('Digite a nota do quarto bimestre: '))

media = (n1 + n2 + n3 + n4 ) / 4

print(f'A média das notas é igual a {media:.2f}')