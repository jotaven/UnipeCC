'''Faça um programa que lê 4 números reais em uma lista, calcula e exibe a quantidade de números negativos e a soma dos números positivos dessa mesma lista;'''
positivo = []
negativo = []

for c in range(4):
    num = float(input('Digite um valor: '))
    if num > 0:
        positivo.append(num)

    elif num < 0:
        negativo.append(num)

print(f'Quantidade de numeros negativos: {len(negativo)}\nSoma dos numeros positivos: {sum(positivo)}')
