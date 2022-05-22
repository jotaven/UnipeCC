
while True:
    codigo = int(input("Digite o codigo do produto(0 para finalizar o programa): "))

    unidade = False

    if codigo == 0:
        break

    if codigo == 1:
        print('Caderno - R$ 12.00')
        unidade = 12

    elif codigo == 2:
        print('Régua - R$ 2.50')
        unidade = 2.5

    elif codigo == 3:
        print('Borracha - R$ 0.25')
        unidade = 0.25

    elif codigo == 4:
        print('Mochila - R$ 50.00')
        unidade = 50

    else: 
        print("Codigo inválido")


    if unidade != False:
        quantidade = int(input("Digite a quantidade adquirida: "))
        print(f"Valor total a ser pago: {unidade*quantidade:.2f}")
