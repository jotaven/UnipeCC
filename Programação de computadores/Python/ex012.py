from ast import NodeVisitor


preco = float(input('Digite o preço do prouduto: '))

if preco <= 50:
    novoPreco = preco*1.05

elif 50 < preco < 100:
    novoPreco = preco*1.1

else:
    novoPreco = preco*1.15

print(f'O novo preço é de {novoPreco:.2f}')

if novoPreco <= 80:
    print('Barato')

elif 80 < novoPreco <= 120:
    print('Normal')

elif 120 < novoPreco <= 200:
    print('Caro')

else:
    print('Muito Caro!')

