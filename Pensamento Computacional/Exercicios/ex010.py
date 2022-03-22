'''
Exercicio 010
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''

temperaturaCelsius = float(input('Digite a temperatura em Celsius: '))
temperaturaFareinheit = temperaturaCelsius * 1.8 + 32

print(f'Temperatura em Fareinheit: {temperaturaFareinheit:.1f}°')
