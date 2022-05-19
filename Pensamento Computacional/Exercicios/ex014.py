'''
Exercicio 014
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.

Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

pesoPeixe = float(input("Digite o peso do peixe: "))

if pesoPeixe >= 50:
    excesso = pesoPeixe - 50
    multa = 4 * excesso
    print(f"O peso total é de {pesoPeixe}, teve um excesso de {excesso}Kg e com isso, teve uma multa de {multa:.2f} reais.")

else:
    print(f"Não haverá multa.")