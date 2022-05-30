numPositivos = []
for c in range(6):
    num = int(input(f'Digite o {c+1} numero: '))
    if num > 0:
        numPositivos.append(num)
print(f'Numeros positivos: {numPositivos}')