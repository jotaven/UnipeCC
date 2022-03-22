'''
Exercicio 009
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
'''

temperaturaFarenheit = int(input('Digite a temperatura em Farenheit: '))
temperaturaCelcius = (5 * temperaturaFarenheit - 160) / 9

print(f'temperatura Celsius: {temperaturaCelcius:.2f}°')