'''01 – Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em
comissões. O vendedor recebe $200 por semana mais 9 por
cento de suas vendas brutas daquela semana.
• Por exemplo, um vendedor que teve vendas brutas de
$3000 em uma semana recebe $200 mais 9 por cento de
$3000, ou seja, um total de $470.

• Escreva um programa (usando um array de contadores)
que determine quantos vendedores receberam salários nos
seguintes intervalos de valores:
$200 - $299 
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante 


Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário,sem fazer vários ifs aninhados.'''
import numpy as np
lista = []

while True:
    comissao = 0.09 * float(input('Digite o valor bruto de vendas da semana: '))
    salario = comissao + 200
    print(f'A comissao foi de {comissao}')
    lista.append(comissao)
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break

np_lista = np.array(lista)

print(np_lista[np.logical_and(np_lista > 200, np_lista < 300)])

'''print(sum(300 <= i < 400 for i in comissao))
print(sum(200.00 <= i < 300.00 for i in comissao))
print(sum(400 <= i < 500 for i in comissao))
print(sum(500 <= i < 600 for i in comissao))
print(sum(600 <= i < 700 for i in comissao))
print(sum(700 <= i < 800 for i in comissao))
print(sum(800 <= i < 900 for i in comissao))
print(sum(900 <= i < 1000 for i in comissao))
print(sum(1000 <= i for i in comissao))'''
