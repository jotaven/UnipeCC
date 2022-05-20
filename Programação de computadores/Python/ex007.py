idade = int(input("digite sua idade: "))
if 5 <= idade <= 10:
    print("infantil")
elif 11 <= idade <= 15:
    print("juvenil")
elif 16 <= idade <= 20:
    print("Júnior")
elif 21 <= idade <= 25:
    print("Profissional")
else:
    print("deu ruim...")