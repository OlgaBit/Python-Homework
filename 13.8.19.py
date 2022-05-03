ticket = int(input("Введите количество билетов:"))
print("Укажите возраст каждого посетителя:")
pris = 0
for i in range(ticket):
    age = int(input("Возраст: "))
    if age < 18:
        pris += 0
    elif 18 <= age < 25:
        pris += 990
    else:
        pris += 1390
if ticket > 3:
    discount = 0.9
else:
    discount = 1
print("Сумма к оплате -", pris * discount)