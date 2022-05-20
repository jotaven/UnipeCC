adolecentes = 0
while True:
    idade = int(input("Digite a idade: "))
    if idade <= 0:
        break
    elif 12 < idade < 17:
        adolecentes += 1
    
print(f"Tem {adolecentes} adolecentes...")