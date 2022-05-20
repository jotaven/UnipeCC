lst = []
for c in range(1, 11):
    valorProduto = float(input(f'Digite o valor do produto {c}: '))
    lst.append(valorProduto)

print(max(lst))