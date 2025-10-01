menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}

def all_menu():
    print("\n=== ВСЕ МЕНЮ ===")
    print("Сортировка по названию:")
    print([x for x in sorted(menu)])
    print("\nСортировка по цене:")
    print(sorted(menu.items(), key=lambda x: x[1]))

def mid_price():
    """Рассчитать среднюю цену"""
    prices = list(map(lambda item: item[1], menu.items()))
    average_price = sum(prices) / len(prices)
    print(f"Средняя цена: {average_price:.2f} руб.")

def update_price():
    """Обновить или добавить позицию в меню"""
    user_menu = input("Введите название позиции для обновления: ")
    try:
        user_price=int(input('Введите новую цену:'))
        if user_price<0:
            print("Цена не может быть отрицательной!")
            return
    except ValueError:
        print("Ошибка: введите целое число для цены!")
        return

    if user_menu in menu:
        update_menu=lambda a, b: menu.update([(a, b)])
        update_menu(user_menu, user_price)
    else:
        update_menu=lambda a, b: menu.update([(a, b)])
        update_menu(user_menu, user_price)


def del_menu():
    """Удалить позицию из меню"""
    user_menu = input("Введите название позиции для обновления: ")
    print('Позиция удалена!' if user_menu in menu and menu.pop(user_menu) else 'Позиция не найдена!')

def search_menu():
    """Показать все блюда дешевле определённой цены N"""
    try:
        n=int(input())
        if n<0:
            print("Цена не может быть отрицательной!")
            return
    except ValueError:
        print("Ошибка: введите целое число!")
        return

    cheaper_n=list(filter(lambda x: x[1]<=n, menu.items()))
    print(cheaper_n if cheaper_n else 'Позиция не найдена!')

def min_max_menu():
    """Показать самые дешевые и дорогие позиции"""
    min_menu=min(menu.items(), key=lambda x: x[1])
    max_menu=max(menu.items(), key=lambda x: x[1])
    print(min_menu,max_menu)


def drink_menu():
    """Показывает только напитки из меню."""
    print("\n=== НАПИТКИ ===")
    drinks = sorted(filter(lambda x: x[0] in ['coffee', 'tea', 'juice'], menu.items()))
    print(drinks if drinks else 'Напитки не найдены!')




from functools import reduce
def make_order():
    """Функция для оформления заказа."""
    order_string = input("Введите список блюд через запятую: ")
    dishes = list(map(lambda x: x.strip(), order_string.split(',')))
    available_dishes = list(filter(lambda dish: dish in menu, dishes))
    unavailable_dishes = list(filter(lambda dish: dish not in menu, dishes))
    if unavailable_dishes:
        print(f"Блюда отсутствуют в меню: {', '.join(unavailable_dishes)}")
    
    order = {dish: menu[dish] for dish in available_dishes}
    
    if order:
        total = reduce(lambda x, y: x + menu[y], order, 0)
        print('Ваш заказ:')
        list(map(lambda i_item: print(f'{i_item[0] + 1}. {i_item[1][0]} — {i_item[1][1]} руб.'), enumerate(order.items())))
        print(f'Итого: {total} руб.')
        if total > 500:
            print('Поздравляем, у вас скидка 10%!')
    else:
        print("Вы ничего не выбрали")



while True:
    print("\n" + "="*50)
    print("Меню кафе")
    print("="*50)
    print("1. Всё меню")
    print("2. Рассчитать среднюю цену")
    print("3. Обновить или добавить позицию в меню")
    print("4. Удалить позицию из меню")
    print("5. Показать все блюда дешевле определённой цены ")
    print("6. Показать самые дешевые и дорогие позиции")
    print("7. Показывает только напитки из меню")
    print("8. Оформить заказ")
    print("9. Выход ")
    print("="*50)

    try:
            user = int(input("Выберите действие (1-9): "))
            
            if user == 1:
                all_menu()
            elif user == 2:
                mid_price()
            elif user == 3:
                update_price()
            elif user == 4:
                del_menu()
            elif user == 5:
                search_menu()
            elif user == 6:
                min_max_menu()
            elif user == 7:
                drink_menu()
            elif user == 8:
                make_order()
            elif user == 9:
                print("Выход из программы")
            else:
                print("Неверный выбор. Введите число от 1 до 9.")
    except ValueError:
            print("Ошибка: введите число")
    except Exception as e:
            print(f"Произошла ошибка: {e}")