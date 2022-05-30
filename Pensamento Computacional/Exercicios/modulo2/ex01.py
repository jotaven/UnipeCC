tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados = []
tabela = []

while True:
    tabela = []
    
    num = int(input('Digite o valor: '))
    if num <= 0:
        break

    for c in tabuada:
        tabela.append(c*num)
        
    resultados.append(tabela)
    print(tabela)

print(resultados)
    

    