slovar = {}
print("дарова, это пицерия емае чё будешь брать ,брат?")
change = int(input("Пепперони(это пицца с колбасками епт) - 1, 4 сыра(сэра в чтре раза бальше) - 2, барбека(в 2 раза больще мяса) - 3, гавайская(с энанасиками) - 4, маргарита(мэм такой ест) - 5"))
result = 0
i = 0
r = 0
d = 0
while i <= 1000:
    if change == 1:
        size = int(input("Тесто тоньше чем ты до пахода в нашу пицерию - 1, тесто норм - 2, крающек с начинькой - 3"))
        if size == 1:
            price = str(input("плати скорее: 699.99 рублей. Добавить в корзину (да/нет)"))
            money = 699.99
            if price == "да":
                result = result + money
            else:
                result = result
        elif size == 2:
                price = str(input("плати скорее: 399.99 рублей. Добавить в корзину (да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        else:
                price = str(input("плати скорее: 899.99 рублей. Добавить в корзину (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
    elif change == 2:
        size = int(input("Тесто тоньше чем ты до пахода в нашу пицерию - 1, тесто норм - 2, крающек с начинькой - 3"))
        if size == 1:
            price = str(input("плати скорее: 499.99 рублей. Добавить в корзину (да/нет)"))
            money = 499.99
            if price == "да":
                result = result + money
            else:
                result = result
        elif size == 2:
                price = str(input("Стоимость выбранной пиццы составляет: 399.99 рублей. Добавить в корзину думай скорей(да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        else:
                price = str(input("плати скорее: 899.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
    elif change == 3:
        size = int(input("Тесто тоньше чем ты до пахода в нашу пицерию - 1, тесто норм - 2, крающек с начинькой - 3"))
        if size == 1:
            price = str(input("плати скорее: 599.99 рублей. Добавить в корзину думай скорей (да/нет)"))
            money = 599.99
            if price == "да":
                result = result + money
            else:
                result = result
        elif size == 2:
                price = str(input("плати скорее: 399.99 рублей. Добавить в корзину думай скорее (да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        else:
                price = str(input("плати скорее: 899.99 рублей. Добавить в корзину думай скорее (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
    elif change == 4:
        size = int(input("Тесто тоньше чем ты до пахода в нашу пицерию - 1, тесто норм - 2, крающек с начинькой - 3"))
        if size == 1:
            price = str(input("плати скорее: 599.99 рублей. Добавить в корзину думай скорее (да/нет)"))
            money = 599.99
            if price == "да":
                result = result + money
            else:
                result = result
        elif size == 2:
                price = str(input("плати скорее: 399.99 рублей. Добавить в корзину думай скорее(да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        else:
                price = str(input("плати скорее: 899.99 рублей. Добавить в корзину думай скорее (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
    elif change == 5:
        size = int(input("Тесто тоньше чем ты до пахода в нашу пицерию - 1, тесто норм - 2, крающек с начинькой - 3"))
        if size == 1:
            price = str(input("плати скорее: 599.99 рублей. Добавить в корзину думай скорее (да/нет)"))
            money = 599.99
            if price == "да":
                result = result + money
            else:
                result = result
        elif size == 2:
                price = str(input("плати скорее: 399.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        else:
                price = str(input("плати скорее: 899.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
    print("Сейчас в корзине:", result, "руб.")
    continue_steps = str(input("Продолжить выбор пицц? (да\нет)"))
    if continue_steps == "да":
        continue
    elif continue_steps == "нет":
        break
while r <= 1000:
    r = r + 1
    drinks = str(input("Добавить в корзину напитки?(да\нет)Узбекистян закончился"))
    if drinks == "да":
        change_drinks = int(input("Кола - 1, Фанта - 2, Кофе - 3, Сок - 4, Випс - 5"))
        if change_drinks == 1:
            size_of_drink = int(input("ОБЪЁМ: 0.3, 0.5, 0.7, 1"))
            if size_of_drink == 0.3:
                price = str(input("Стоимость напитка составляет: 59.99 рублей. Добавить в корзину думай скорее (да/нет)"))
                money = 59.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size_of_drink == 0.5:
                price = str(input("Стоимость напитка составляет: 79.99 рублей. Добавить в корзину думай скоре (да/нет)"))
                money = 79.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size_of_drink == 0.7:
                price = str(input("Стоимость напитка составляет: 99.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 99.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size_of_drink == 1:
                price = str(input("Стоимость напитка составляет: 149.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 149.99
                if price == "да":
                    result = result + money
                else:
                    result = result
    print("Стоимость всей корзины составляет", result, "руб.")
    continue_steps = str(input("Продолжить выбор напитков? (да\нет)"))
    if continue_steps == "да":
        continue
    elif continue_steps == "нет":
        break
while d <= 1000:
    sweets = (input("Добавить в корзину сладости?(да\нет)"))
    if sweets == "да":
        change_sweets = int(input("Мороженое - 1, Кекс - 2, Торти - 3, Бэзе - 4, шокодадка - 5"))
        if change_sweets == 1:
            size_of_sweets = int(input("Очень маленькая - 1, маленькая - 2, средняя - 3, большая - 4"))
            if size_of_drink == 1:
                price = str(input("Стоимость сладости составляет: 59.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 59.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size_of_sweets == 2:
                price = str(input("Стоимость сладости составляет: 79.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 79.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size_of_sweets == 3:
                price = str(input("Стоимость сладости составляет: 99.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 99.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size_of_sweets == 4:
                price = str(input("Стоимость сладости составляет: 149.99 рублей. Добавить в корзину думай скорей (да/нет)"))
                money = 149.99
                if price == "да":
                    result = result + money
                else:
                    result = result
    print("Стоимость всей корзины составляет", result, "руб.")
    continue_steps = str(input("Продолжить выбор сладостей? (да\нет)"))
    if continue_steps == "да":
        continue
    elif continue_steps == "нет":
        break
change_pay = int(input("Выберите способ оплаты: наличные - 1, карта - 2"))
if change_pay == 1:
    print('Всё ок, приятного аппетита,ждем тебя снова здесь, брат ;)')
elif change_pay == 2:
    money_to_pay = float(input("ВВЕДИТЕ СУММУ ОПЛАТЫ"))
    change = money_to_pay - result
    print("ВЫ ВНЕСЛИ:", money_to_pay, 'ВАША СДАЧА:', change)