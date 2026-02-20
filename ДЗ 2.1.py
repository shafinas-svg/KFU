
class ManeyError(Exception):
    pass


def validate_name(name):
    if not name.strip():
        raise ValueError("Имя не может быть пустым")
    if len(name) < 2:
            raise ValueError('Имя слишком короткое')
    return name
    
    
# должен быть числом
# ≥ 12
# raise ValueError("Возраст должен быть числом")

def validate_age(age):
    if not age.isdigit():
        raise ValueError("Возраст должен быть числом без пробелов")
    age=int(age)
    if age<12:
        raise ValueError('Вы слишком маленькие')
    return age
# 3. Количество билетов
# должно быть числом
# > 0
# ≤ 5
# raise ValueError("Некорректное количество билетов")
    
def validate_tickets(count):
    if not count.isdigit():
        raise ValueError("Колиичество должно быть числом без пробелов")
    count=int(count)
    if count<0 or count>5:
        raise ValueError("Некорректное количество билетов")
    return count
    
# 4. Бюджет
# число
# ≥ 0
# raise ValueError("Некорректный бюджет")

def validate_budget(budget):
    if not budget.isdigit():
        raise ValueError('Бюджет должен быть числом')
    budget=int(budget)
    if budget<0:
        raise ValueError("Некорректный бюджет")
    return budget


ticket_ptice= 500
def calculate_total(count):
    return count*ticket_ptice


while True:
    try:
        name=validate_name(input('Введите свое имя:'))
        age=validate_age(input('Введите свой возраст:'))
        count=validate_tickets(input('Введите колличество билетов:'))
        budget=validate_budget(input('Введите свой бюджет:'))

        total=calculate_total(count)

        if budget-total < 0:
            raise ManeyError('Недостаточно средств')
        
        summa = budget - total


        print("Начоло бронирования!")
        print(f"Имя: {name}")
        print(f"Билетов: {count}")
        print(f"К оплате: {total}")
        print(f"Сдача: {summa}" )
        print('Бронирование прошло успешно!. До новых встреч!1')
        
        break

    except ValueError as e:
        print("Ошибка:", e)

    except ManeyError as e:
        print("Ошибка оплаты:", e)
        print("Попробуйте снова\n")

    except Exception as e:
        print("Неизвестная ошибка:", e)
        print("Попробуйте снова\n")
