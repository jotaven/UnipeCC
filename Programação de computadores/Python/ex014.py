opcao = ''

while opcao != 'NAO':
    distancia = float(input("Digite a distancia percorrida(m): "))
    tempo = int(input("Digite o tempo que levou para percorrer a distancia total(s): "))
    velocidadeMedia = distancia/tempo
    print(f'A velocidade média foi de {velocidadeMedia}m/s')
    opcao = str(input("Deseja continuar? [SIM/NAO]")).upper().strip()