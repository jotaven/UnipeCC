'''Faça um Programa que peça dois números e imprima o maior deles.'''


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"o numero {numero1} é maior.")

elif numero2 > numero1:
    print(f"O numero {numero2} é maior")

else:
    print("os numeros são iguais")
