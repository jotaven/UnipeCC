quantidadeSim = 0
quantidadeNao = 0
erros = 0
for c in range(0, 15):
    resposta = str(input("Você gosta de beterraba?(1 para sim e 2 para não) ")).strip()
    if resposta == "1":
        quantidadeSim += 1
    elif resposta == "2":
        quantidadeNao += 1
    else:
        erros += 1

print(f"A quantidade de Sim foi de {quantidadeSim}, a quantidade de Não foi de {quantidadeNao} e {erros} não responderam corretamente")
