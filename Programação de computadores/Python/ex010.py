num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

codigo = int(input('''Escolha o que você quer fazer:
1. Média entre os números digitados
2. Diferença do maior pelo menor
3. Produto entre os números digitados
4. Divisão pelo primeiro pelo segundo\n'''))

if codigo == 1:
    print((num1 + num2)/2)
elif codigo == 2:
    if num1 > num2:
        print(num1-num2)
    elif num2 > num1:
        print(num2-num1)
    else:
        print(0)
elif codigo == 3:
    print(num1 * num2)
elif codigo == 4:
    print(num1/num2)
else:
    print('Código inválido')
