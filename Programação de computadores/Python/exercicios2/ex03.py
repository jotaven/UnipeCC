'''Cada espectador de um cinema respondeu a um questionário no qual constava sua opinião em relação ao filme: ótimo – 3, bom – 2, regular – 1. Faça um programa que receba a opinião de 5 espectadores em uma lista, calcule e mostre a quantidade de pessoas que responderam ótimo, bom e regular.'''

lista = []
print('Qual a sua opinião em relação ao filme: ótimo – 3, bom – 2, regular – 1')
for c in range(1, 6):
    opniao = int(input(f'Opnião do {c}o especator: '))
    lista.append(opniao)

print(f'{lista.count(1)} classificaram o filme como Regular.')
print(f'{lista.count(2)} classificaram o filme como Bom.')
print(f'{lista.count(3)} classificaram o filme como Ótimo.')
