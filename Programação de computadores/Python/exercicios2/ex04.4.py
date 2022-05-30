numeros = [[],[]]

for c in range(4):
    numero = float(input('Digite um valor: '))
    if numero > 0:
        numeros[1].append(numero)
    elif numero < 0:
        numeros[0].append(numero)

print(
    f'Quantidade de numeros negativos: {len(numeros[0])}\nSoma dos numeros positivos: {sum(numeros[1])}')
