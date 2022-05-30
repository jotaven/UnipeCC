import numpy as np

tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
np_tabuada = np.array(tabuada)
resultados = []

while True:
    num = int(input('Digite o valor: '))
    if num <= 0:
        break
    resultados.append(np_tabuada*num)
    print(np_tabuada*num)

print(resultados)