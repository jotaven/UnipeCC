'''
Exercicio 013
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7h) - 58
    Para mulheres: (62.1h) - 44.7
'''

altura = float(input('Informe a sua altura: '))
genero = str(input('Informe o seu gênero(M/F): ')).upper().strip()
pesoIdeal = 0


if genero == 'M':
    pesoIdeal = 72.7 * altura - 58
elif genero == 'F':
    pesoIdeal = 62.1 * altura - 44.7

print(f'O seu peso ideal é de {pesoIdeal:.2f}')
