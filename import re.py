import re
from datetime import datetime, timedelta
from functools import wraps
import time



#  2. РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
LOG_PATTERN = re.compile(r"^\[(.*?)\]\s+(\w+):\s+(\w+)$")

# 3. ДЕКОРАТОРЫ
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнена за {execution_time:.6f} секунд")

        return result

    return wrapper

# 1. РАБОТА С DATETIME
def parse_log_line(line):
    line = line.strip()
    match = LOG_PATTERN.match(line)

    if not match:
        raise ValueError(f"Неверный формат строки: {line}")

    date_str, user_id, action = match.groups()

# 1. Работа с datetime:
    try:
        timestamp = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(f"Неверный формат даты: {date_str}")

    return {
        "timestamp": timestamp,
        "user_id": user_id,
        "action": action
    }

# 4. ИТОГОВАЯ ОБРАБОТКА ЛОГА