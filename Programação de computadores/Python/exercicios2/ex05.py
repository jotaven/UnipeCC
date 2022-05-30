'''Faça um programa que receba o preço de cinco produtos em uma lista, calcula e exiba:

A quantidade de produtos com preço inferior a R$ 50,00;
A quantidade de produtos com preço entre R$ 50,00 e 80,00;
A quantidade de produtos com preço acima de R$ 80,00
A média de preço dos produtos;'''

valores = []
q1 = 0
q2 = 0
q3 = 0

for c in range(5):
    preco = float(input('Digite o preço do produto: '))
    valores.append(preco)

for c in valores:
    if c < 50:
        q1 += 1
    elif 50 <= c < 80:
        q2 += 1
    else:
        q3 += 1


media = sum(valores)/len(valores)

print(f'''A quantidade de produtos com preço inferior a R$ 50,00: {q1};
A quantidade de produtos com preço entre R$ 50,00 e 80,00: {q2};
A quantidade de produtos com preço acima de R$ 80,00: {q3}
A média de preço dos produtos: {media}''')
