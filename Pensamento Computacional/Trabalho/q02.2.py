'''02 – Faça um programa que leia um número
indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um
valor igual a -1 (que não deve ser armazenado).
• Após esta entrada de dados, faça: 
- Mostre a quantidade de valores que foram lidos; len()
- Exiba todos os valores na ordem em que foram informados, um ao lado do outro; append()
- Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; reverse
- Calcule e mostre a soma dos valores; sum()
- Calcule e mostre a média dos valores; sum()/len()
- Calcule e mostre a quantidade de valores acima da média calculada;
- Calcule e mostre a quantidade de valores abaixo de sete;
- Encerre o programa com uma mensagem;'''
notas = []
nMedia = 0
menorSete = 0

while True:
    valor = int(input('Digite o valor: '))
    while valor < -1:
        valor = int(input('Digite o valor!: '))
    if valor == -1:
        break
    notas.append(valor)

reverse = notas[::-1]

media = sum(notas)/len(notas)

for c in notas:
    if c > media:
        nMedia += 1

    if menorSete < 7:
        menorSete += 1

print(f'Quantidade de valores que foram lidos: {len(notas)}')
print(f'Valores na ordem em que foram informados: {notas}')
print(f'A soma dos valores: {sum(notas)}')
for item in reverse:
    print(item)
print(f'A média dos valores: {media}')
print(f'A quantidade de valores acima da média calculada: {nMedia}')
print(f'Quantidade de valores abaixo de sete: {menorSete}')