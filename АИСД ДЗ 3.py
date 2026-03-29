
animals = [
    ["Барсик", "рысь", 18],
    ["Слоник", "слон", 5400],
    ["Луна", "волк", 32],
    ["Грибочек", "лиса", 18],
    ["Миша", "медведь", 310],
    ["Тигра", "тигр", 220],
    ["Король", "лев", 205],
    ["Снежок", "заяц", 4],
    ["Гром", "бизон", 720],
    ["Норка", "енот", 9],
    ["Марта", "жираф", 810],
    ["Шторм", "носорог", 2100],
    ["Дымка", "пума", 68],
    ["Мила", "лама", 130],
    ["Кузя", "кабан", 140],
    ["Зевс", "орел", 6],
    ["Плюша", "панда", 115],
    ["Искра", "антилопа", 95],
    ["Яша", "ягуар", 96],
    ["Няня", "обезьяна", 27],
    ["Тор", "лось", 430],
    ["Лада", "косуля", 34],
    ["Шура", "сурикат", 5],
    ["Гоша", "бегемот", 1600],
    ["Рада", "зебра", 280],
    ["Туман", "волк", 41],
    ["Кира", "рысь", 21],
    ["Мишка", "медведь", 360],
    ["Феня", "лиса", 14],
    ["Арчи", "тигр", 240],
    ["Веста", "леопард", 72],
    ["Птичка", "соболь", 8],
    ["Пороро", "пингвин", 12],
    ["Ева", "кенгуру", 85],
    ["Грант", "верблюд", 540],
    ["Оскар", "осел", 190],
    ["Шустрик", "лама", 145],
    ["Тюльпан", "альпака", 62],
    ["Милашка", "сурикат", 6],
    ["Умник", "шимпанзе", 48],
    ["Великан", "слон", 4900]
]

def is_less(animal1, animal2):
    if animal1[2] < animal2[2]:
        return True
    elif animal1[2] == animal2[2]:
        return animal1[0] < animal2[0]
    else:
        return False

def insertion_sort(arr):
    result = arr[:] 

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        while j >= 0 and is_less(current, result[j]):
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result


def print_animal(animal):
    print(f"Кличка: {animal[0]}, Вид: {animal[1]}, Масса: {animal[2]}")


def print_all_animals(arr):
    for animal in arr:
        print_animal(animal)


def print_lightest_3(arr):
    print("\n3 самых лёгких животных:")
    count = 3
    if len(arr) < 3:
        count = len(arr)

    for i in range(count):
        print_animal(arr[i])


def print_heaviest_3(arr):
    print("\n3 самых тяжёлых животных:")
    count = 3
    start = len(arr) - count
    if start < 0:
        start = 0

    for i in range(len(arr) - 1, start - 1, -1):
        print_animal(arr[i])


def find_by_weight(arr, weight):
    found = []

    for animal in arr:
        if animal[2] == weight:
            found.append(animal)

    return found

def print_same_weight_groups(arr):
    print("\nГруппы животных с одинаковой массой:")

    has_groups = False
    i = 0

    while i < len(arr):
        group = [arr[i]]
        j = i + 1

        while j < len(arr) and arr[j][2] == arr[i][2]:
            group.append(arr[j])
            j += 1

        if len(group) > 1:
            has_groups = True
            print(f"\nМасса {arr[i][2]} кг:")
            for animal in group:
                print_animal(animal)

        i = j

    if not has_groups:
        print("Нет животных с одинаковой массой.")


# Основная часть программы
sorted_animals = insertion_sort(animals)

print("Все животные в отсортированном порядке:\n")
print_all_animals(sorted_animals)

print_lightest_3(sorted_animals)
print_heaviest_3(sorted_animals)

# Поиск по массе
weight = int(input("\nВведите массу для поиска: "))
found_animals = find_by_weight(sorted_animals, weight)

print(f"\nЖивотные с массой {weight} кг:")
if len(found_animals) == 0:
    print("Таких животных нет.")
else:
    for animal in found_animals:
        print_animal(animal)

print_same_weight_groups(sorted_animals)