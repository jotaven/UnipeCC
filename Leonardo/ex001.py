import datetime

nascimento = int(input('Qual foi o ano em que você nasceu? '))
anoAtual = datetime.datetime.today().year

idade = anoAtual - nascimento
futuro = idade + (2025 - anoAtual)

print(f'Você tem {idade} anos e em 2025 terá {futuro} anos!')