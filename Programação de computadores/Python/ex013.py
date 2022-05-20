crianca = 0
adulto = 0
idade = 0

while idade >= 0:

    idade = int(input('Digite a idade(Digite um numero negativo para finalizar): '))
    if idade <= 15:
        crianca += 1
    else:
        adulto += 1

print(f'Quantidade da Primeira faixa etária: {crianca}, e da segunda faixa etária: {adulto}')