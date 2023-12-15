def choose_pizza():
    print("дарова, это пицерия емае чё будешь брать ,брат?")
    change = int(input(
        "Пепперони(это пицца с колбасками епт) - 1, 4 сыра(сэра в четыре раза больше) - 2, барбека(в 2 раза больше мяса) - 3, гавайская(с энанасиками) - 4, маргарита(мэм такой ест) - 5"))
    return change


def choose_size():
    size = int(input("Тесто тоньше чем ты до похода в нашу пицерию - 1, тесто норм - 2, крающек с начинькой - 3"))
    return size


def calculate_price(size, pizza_type):
    if size == 1:
        price = 699.99
    elif size == 2:
        price = 399.99
    else:
        price = 899.99

    print(f"Плати скорее: {price} рублей.")
    add_to_cart = input("Добавить в корзину (да/нет)")

    if add_to_cart.lower() == "да":
        return price
    else:
        return 0


def order_pizza():
    result = 0

    while True:
        pizza_type = choose_pizza()
        size = choose_size()
        price = calculate_price(size, pizza_type)
        result += price

        continue_steps = input("Продолжить выбор пицц? (да/нет)")
        if continue_steps.lower() != "да":
            break

    return result


def order_drinks(result):
    r = 0
    while r <= 1000:
        drinks = input("Добавить в корзину напитки? (да/нет) Узбекистян закончился")

        if drinks.lower() == "да":
            # Add logic to choose and calculate the price of drinks
            pass

        continue_steps = input("Продолжить выбор напитков? (да/нет)")
        if continue_steps.lower() != "да":
            break


def order_sweets(result):
    d = 0
    while d <= 1000:
        sweets = input("Добавить в корзину сладости? (да/нет)")

        if sweets.lower() == "да":
            # Add logic to choose and calculate the price of sweets
            pass

        continue_steps = input("Продолжить выбор сладостей? (да/нет)")
        if continue_steps.lower() != "да":
            break


def payment(result):
    change_pay = int(input("Выберите способ оплаты: наличные - 1, карта - 2"))

    if change_pay == 1:
        print('Всё ок, приятного аппетита, ждем тебя снова здесь, брат ;)')
    elif change_pay == 2:
        money_to_pay = float(input("ВВЕДИТЕ СУММУ ОПЛАТЫ"))
        change = money_to_pay - result
        print(f"ВЫ ВНЕСЛИ: {money_to_pay}, ВАША СДАЧА: {change}")


# Main program
result = order_pizza()
order_drinks(result)
order_sweets(result)
payment(result)
