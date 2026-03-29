import re
import time
from datetime import datetime, timedelta
from functools import wraps


# 2. РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
pattern = r"^\[(.*?)\]\s+(\w+):\s+(\w+)$"
allowed_actions = {"login", "logout", "view_page"}


# 3. ДЕКОРАТОР
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Функция {func.__name__} выполнена за {end - start:.6f} секунд")
        return result

    return wrapper


# 1. РАБОТА С DATETIME
def parse_line(line):
    line = line.strip()

    match = re.match(pattern, line)
    if not match:
        raise ValueError("Неверный формат строки")

    date_str = match.group(1)
    user_id = match.group(2)
    action = match.group(3)

    try:
        log_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError("Неверный формат даты")

    return log_time, user_id, action


# 4. ОСНОВНАЯ ОБРАБОТКА ФАЙЛА
@timer_decorator
def read_log_file(filename):
    users = {}
    errors = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            line_number = 0

            for line in file:
                line_number += 1

                if not line.strip():
                    continue

                try:
                    log_time, user_id, action = parse_line(line)
                except ValueError as error:
                    errors.append(f"Строка {line_number}: {error}")
                    continue

                if action not in allowed_actions:
                    errors.append(
                        f"Строка {line_number}: неизвестное действие '{action}'"
                    )
                    continue

                if user_id not in users:
                    users[user_id] = {
                        "all_time": timedelta(0),
                        "actions": 0,
                        "login_time": None
                    }

                users[user_id]["actions"] += 1

                if action == "login":
                    if users[user_id]["login_time"] is not None:
                        errors.append(
                            f"Строка {line_number}: у пользователя {user_id} повторный login без logout"
                        )
                    else:
                        users[user_id]["login_time"] = log_time

                elif action == "logout":
                    if users[user_id]["login_time"] is None:
                        errors.append(
                            f"Строка {line_number}: у пользователя {user_id} logout без login"
                        )
                    else:
                        session_time = log_time - users[user_id]["login_time"]

                        if session_time.total_seconds() < 0:
                            errors.append(
                                f"Строка {line_number}: logout раньше login у пользователя {user_id}"
                            )
                        else:
                            users[user_id]["all_time"] += session_time

                        users[user_id]["login_time"] = None

    except FileNotFoundError:
        print("Файл не найден")
        return {}, ["Файл не найден"]

    for user_id in users:
        if users[user_id]["login_time"] is not None:
            errors.append(f"Пользователь {user_id} вошёл, но не вышел из системы")

    return users, errors


# Дополнительная функция для красивого вывода времени
def time_to_string(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# 4. ИТОГ
def show_result(users, errors):
    sorted_users = sorted(
        users.items(),
        key=lambda item: item[1]["all_time"],
        reverse=True
    )

    print("\nСтатистика по пользователям:")
    print("-" * 40)

    for user_id, info in sorted_users:
        print(f"Пользователь: {user_id}")
        print(f"Общее время в системе: {time_to_string(info['all_time'])}")
        print(f"Количество действий: {info['actions']}")
        print("-" * 40)

    if errors:
        print("\nОшибки:")
        for error in errors:
            print(error)


def main():
    filename = "date.txt"
    users, errors = read_log_file(filename)
    show_result(users, errors)


if __name__ == "__main__":
    main()