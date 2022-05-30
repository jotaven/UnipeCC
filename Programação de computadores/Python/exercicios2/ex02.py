
peoples = []
for c in range(3):
    sexo = str(input(f'Qual o sexo da {c+1} pessoa (M/F): ')).upper().strip()
    while sexo not in 'MF':
        print('Sexo inválido!')
        sexo = str(input(f'Qual o sexo da {c+1} pessoa (M/F): ')).upper().strip()
    peoples.append(sexo)

homens = peoples.count('M')
mulheres = peoples.count('F')
print(f'Homens: {homens}\nMulheres: {mulheres}')