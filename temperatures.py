import numpy as np
from functools import reduce

# 1. Генерация исходных данных
temperatures = np.random.randint(-20, 40, 10000)

# 2. Генератор потока данных
def temperature_stream(data):
    for temp in data:
        yield temp

# 3. Проверка корректности температуры
def is_valid_temperature(temp):
    return -15 <= temp <= 35

# 4. Нормализация данных
def normalize_data(data):
    mean_value = np.mean(data)
    std_value = np.std(data)

    if std_value == 0:
        std_value = 1

    return map(lambda x: (x - mean_value) / std_value, data)

# 5. Дополнительное преобразование
def transform_data(data):
    return map(lambda x: np.sin(x) + x**2, data)

# 6. Генератор окон по 30 элементов
def window_generator(data, window_size=30):
    window = []

    for value in data:
        window.append(value)

        if len(window) == window_size:
            yield window
            window = []

# 7. Анализ одного окна
def analyze_window(window):
    arr = np.array(window)

    return {
        "mean": np.mean(arr),
        "median": np.median(arr),
        "std": np.std(arr),
        "min": np.min(arr),
        "max": np.max(arr)
    }

# 8. Проверка на аномальность
def is_anomalous(stat):
    return abs(stat["mean"]) > 1 or stat["std"] > 1

# 9. Функция для reduce
def reduce_anomalies(accumulator, stat):
    return {
        "count": accumulator["count"] + 1,
        "sum_mean": accumulator["sum_mean"] + stat["mean"],
        "max_mean": max(accumulator["max_mean"], stat["mean"])
    }

# 10. Основная часть программы
# создается
stream = temperature_stream(temperatures) 
# удалить неправильные температуры
filtered_data = list(filter(lambda x: is_valid_temperature(x), stream))
# нормализовать данные
normalized_data = normalize_data(filtered_data)
# преобразовать данные  
transformed_data = transform_data(normalized_data)
# разбитие на окна
windows = list(window_generator(transformed_data, 30))
# сколько всего окон
total_windows = len(windows)
# статистика
window_stats = list(map(analyze_window, windows))
# только аномальные окна
anomalous_windows = list(filter(lambda stat: is_anomalous(stat), window_stats))

# 11. Итоговая статистика через reduce
result = reduce(
    lambda acc, stat: reduce_anomalies(acc, stat),
    anomalous_windows,
    {
        "count": 0,
        "sum_mean": 0,
        "max_mean": float("-inf")
    }
)

# 12. Обработка случая без аномалий
if result["count"] == 0:
    result["max_mean"] = 0

# 13. Финальный вывод
print(f"Всего окон: {total_windows}")
print(f"Аномальных окон: {result['count']}")
print(f"Максимальное среднее значение: {result['max_mean']:.4f}")
print(f"Сумма средних значений: {result['sum_mean']:.4f}")