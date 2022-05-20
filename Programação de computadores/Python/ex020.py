opt1, opt2, opt3 = 0, 0, 0
for c in range(1, 16):
    print('\n#### Opnião do filme ####')
    opniao = int(input(f'''
    3. Ótimo
    2. Bom
    1. Regular
    Digite a opnião do espectador {c}: '''))
    if opniao == 1:
        opt1 += 1

    elif opniao == 2:
        opt2 +=1

    elif opniao == 3:
        opt3 +=1


print(f"{opt3} acharam o filme Ótimo")
print(f"{opt2} acharam o filme Bom")
print(f"{opt1} acharam o filme Regular")