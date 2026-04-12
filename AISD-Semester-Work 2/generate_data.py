import os
import random


def generate_files():
    folder_name = "input_data"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    number_of_files = 100
    min_size = 100
    max_size = 10000

    step = (max_size - min_size) // (number_of_files - 1)

    for i in range(number_of_files):
        size = min_size + i * step

        if i == number_of_files - 1:
            size = max_size

        arr = []

        for _ in range(size):
            value = random.randint(-10000, 10000)
            arr.append(value)

        file_name = f"data_{i + 1}.txt"
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(" ".join(map(str, arr)))

    print("100 файлов с входными данными успешно созданы в папке input_data.")


if __name__ == "__main__":
    generate_files()