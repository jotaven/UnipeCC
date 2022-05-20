qSim = 0
qNao = 0
for c in range(15):
    beterraba = int(input("Você gosta de beterraba?\n1. Sim\n2. Não\n "))
    if beterraba == 1:
        qSim += 1
    elif beterraba == 2:
        qNao += 1 
print(f'{qSim} Gostam de Beterraba, enquanto {qNao} não gostam.')