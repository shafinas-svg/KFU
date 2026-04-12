import os
import csv
import time
import matplotlib.pyplot as plt

from comb_sort import comb_sort


def read_array_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read().strip()

    if data == "":
        return []

    arr = list(map(int, data.split()))
    return arr


def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def main():
    input_folder = "input_data"
    result_folder = "results"

    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    all_files = os.listdir(input_folder)
    txt_files = []

    for file_name in all_files:
        if file_name.endswith(".txt"):
            txt_files.append(file_name)

    txt_files.sort(key=lambda name: int(name.split("_")[1].split(".")[0]))

    results = []

    for test_number, file_name in enumerate(txt_files, start=1):
        file_path = os.path.join(input_folder, file_name)

        # Считываем данные из файла ДО измерения времени
        arr = read_array_from_file(file_path)
        size = len(arr)

        # Замеряем только время сортировки
        start_time = time.perf_counter()
        sorted_arr, comparisons, swaps, steps = comb_sort(arr.copy())
        end_time = time.perf_counter()

        sorting_time = end_time - start_time

        if not check_sorted(sorted_arr):
            print(f"Ошибка: массив из файла {file_name} отсортирован неправильно.")
            return

        results.append([test_number, size, sorting_time, comparisons, swaps, steps])

        print(
            f"Тест {test_number}: "
            f"размер = {size}, "
            f"время = {sorting_time:.8f} сек, "
            f"сравнения = {comparisons}, "
            f"обмены = {swaps}, "
            f"шаги = {steps}"
        )

    # Сохраняем результаты в CSV
    csv_file = os.path.join(result_folder, "results.csv")

    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Номер теста", "Размер массива", "Время (сек)", "Сравнения", "Обмены", "Шаги"])
        writer.writerows(results)

    print(f"\nРезультаты сохранены в файл: {csv_file}")

    # Подготовка данных для графиков
    sizes = []
    times = []
    steps_list = []

    for row in results:
        sizes.append(row[1])
        times.append(row[2])
        steps_list.append(row[5])

    # График времени
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker="o")
    plt.xlabel("Размер массива")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Зависимость времени выполнения Comb sort от размера массива")
    plt.grid(True)
    plt.savefig(os.path.join(result_folder, "time_graph.png"))
    plt.show()

    # График количества шагов
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, steps_list, marker="o")
    plt.xlabel("Размер массива")
    plt.ylabel("Количество шагов")
    plt.title("Зависимость количества шагов Comb sort от размера массива")
    plt.grid(True)
    plt.savefig(os.path.join(result_folder, "steps_graph.png"))
    plt.show()

    print("Графики сохранены в папке results.")


if __name__ == "__main__":
    main()