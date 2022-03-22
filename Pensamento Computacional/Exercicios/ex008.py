'''
Exercicio 008
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

dinheiroPorHora =  float(input('Quantos reais você ganha por hora? '))
tempoDeTrabalho = int(input('Quantas horas você trabalha por mês? '))

salarioMensal = dinheiroPorHora * tempoDeTrabalho

print(f'O seu salário mensal é de {salarioMensal}')