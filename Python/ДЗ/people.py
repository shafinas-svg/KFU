people = [
    {"name": "Анна", "age": 19, "hobby": "рисование", "salary": 40000},
    {"name": "Илья", "age": 32, "hobby": "спорт", "salary": 85000},
    {"name": "Катя", "age": 24, "hobby": "фото", "salary": 60000},
    {"name": "Даня", "age": 17, "hobby": "игры", "salary": 0},
    {"name": "Олег", "age": 45, "hobby": "рыбалка", "salary": 120000},
    {"name": "Вика", "age": 28, "hobby": "чтение", "salary": 70000}
]
# # Часть 1 — filter
# Выберите всех, кто старше 25 лет.
# Отфильтруйте тех, у кого зарплата выше 50 000.
# Создайте новый список людей, у которых хобби начинается на букву “р”.

# 1
print('Задание 1')
print('-'*30)
print(list(filter(lambda x: x['age']>25, people)))
# 2
print(list(filter(lambda x: x['salary']>50000,people)))
# 3
print(list(filter(lambda x: x['hobby'][0]=='р', people)))

print('Задание 2')
print('-'*30)
# Часть 2 — map
# Получите список всех имён.
# Увеличьте зарплату каждого на 10% (в новом списке).
# Сделайте список строк вида "Имя: Возраст лет".

print(list(map(lambda x: x['name'],people)))
print(list(map(lambda x: x['salary']*1.10,people)))
print(list(map(lambda x: f" {x['name']} : {x['age']}",people)))

print('Задание 3')
print('-'*30)
from functools import reduce
# Часть 3 — reduce
# Найдите суммарную зарплату всех людей.
# Найдите средний возраст с помощью reduce.
# Найдите имя человека с максимальной зарплатой (через reduce, без max()).
salaries = list(map(lambda x: x["salary"], people))
print(sum(salaries))


people_age=[x['age'] for x in people]
age_summa = reduce(lambda x,y: x + y, people_age)
print(age_summa/len(people_age))

max_salary = reduce(lambda x, y: x if x['salary'] > y['salary'] else y,people)
print(max_salary['name'])



print('Задание 4')
print('-'*30)
# Часть 4 — lambda
# Отсортируйте людей по возрасту.
# Отсортируйте по длине хобби.
# Сделайте новую структуру данных: список из кортежей (имя, количество букв в имени).

print(list(sorted(map(lambda x: f"{x['name']} : {x['age']}",people))))
sorted_hobby = sorted(people, key=lambda x: x['hobby'])
print( list(map(lambda x: f"{x['name']} : {x['hobby']}", sorted_hobby)))
sorted_name= sorted(people,key=lambda x: x['name'])
print( list(map(lambda x: f"{x['name']} : {len(x['name'])}",sorted_name)))

print('Финальное задание')
print('-'*30)
# Финальное задание
# Напишите одну строку кода, которая возвращает имена всех людей старше 20 лет с 
# зарплатой больше 50 000 и хобби длиннее 4 символов.
print([x['name'] for x in people if x['age']>20 and x['salary']>50000 and len(x['hobby'])>4])







people1 = [
    {"name": "Анна", "age": 19, "hobby": "рисование", "salary": 40000, "city": "Казань"},
    {"name": "Илья", "age": 32, "hobby": "спорт", "salary": 85000, "city": "Москва"},
    {"name": "Катя", "age": 24, "hobby": "фото", "salary": 60000, "city": "Казань"},
    {"name": "Даня", "age": 17, "hobby": "игры", "salary": 0, "city": "Казань"},
    {"name": "Олег", "age": 45, "hobby": "рыбалка", "salary": 120000, "city": "Москва"},
    {"name": "Вика", "age": 28, "hobby": "чтение", "salary": 70000, "city": "Казань"}
]


reviews = [
    "Отличный кофе и уютная атмосфера",
    "Очень вкусный капучино",
    "Обслуживание могло быть лучше",
    "Люблю этот кофе",
    "Кафе хорошее, но музыка громкая"
]
print('Задача с классной работы')
print('-'*30)
# Создать новый список, где каждый человек представлен словарём, но зарплата увеличена на 15% (использовать map, filter, reduce или lambda)

print(list(map(lambda person: {
    'name': person['name'],
    'age': person['age'],
    'hobby': person['hobby'], 
    'salary': person['salary'] * 1.15,
    'city': person['city']
}, people1)))
