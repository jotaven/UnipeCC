lst = []
while True:
    num = int(input('Digite um numero: '))
    lst.append(num)
    if num == 0:
        break

print(f'O maior numero informado é: {max(lst)}')