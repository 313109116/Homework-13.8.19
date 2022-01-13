tickets = int(input("Сколько билетов вам необходимо? \n"))
price = []
for i in range(1, tickets + 1):
    age = int(input(f"Возраст {i} участника? "))
    if age < 18:
        price.append(0)
    if age > 25:
        price.append(1390)
    elif age >= 18 <= 25:
        price.append(990)

if tickets > 3:
        print("Сумма с учетом скидки составляет ", ((sum(price) * 0.9)), "руб.")
else:
        print("Сумма составляет ", sum(price), "руб.")
