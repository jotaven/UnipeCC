crianca = 0
adulto = 0

while True:
    idade = int(input('Digite a idade(Digite um numero negativo para finalizar): '))
    if idade < 0:
        break

    elif 0 < idade <= 15:
        crianca += 1

    elif idade > 15:
        adulto += 1

print(f"{crianca} da primeira  e {adulto} Adultos")

