'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

number1 = int(input("Digite o primeiro numero: ")) + 1
number2 = int(input("Digite o segundo numero: "))

print(list(range(number1, number2)))