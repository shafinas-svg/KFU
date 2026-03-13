numbers = [5, 12, 7, 20, 3, 18, 2, 15, 9, 30, 11, 6]

# Напишите генератор greater_than_ten(numbers), который возвращает только 
# числа больше 10.

def greater_than_ten(numbers):
    for num in numbers:
        if num > 10:
            yield num

#  Напишите генератор square_numbers(numbers), который возвращает
#  квадраты чисел.
def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

# С помощью filter оставьте только чётные квадраты чисел.

chet = filter(lambda x: x % 2 == 0, square_numbers(greater_than_ten(numbers)))
# Используя map, преобразуйте числа: число → строка вида "value=ЧИСЛО"

values = map(lambda x: f"value={x}", chet)
print("Результат пунктов 1-4:")
for item in values:
    print(item)

from functools import reduce
# Используя reduce, найдите:
# сумму всех чисел списка
# максимальное число списка

sum_numbers = reduce(lambda a, b: a + b, numbers)
max_number = reduce(lambda a, b: a if a > b else b, numbers)
print("\n5a) Сумма всех чисел списка:", sum_numbers)
print("5b) Максимальное число списка:", max_number)

# Напишите генератор multiples_of_three(n), который возвращает первые n чисел, кратных 3.
def multiples_of_three(n):
    for i in range(1, n + 1):
        yield i * 3
print("\n6) Первые 10 чисел, кратных 3:")
for num in multiples_of_three(10):
    print(num)

# Напишите генератор word_generator(text), который возвращает слова строки по одному.
def word_generator(text):
    for word in text.split():
        yield word

text = 'I love programming'
for word in word_generator(text):
    print(word)

# Используя map и filter, обработайте текст в следующей последовательности:
# оставить слова длиной > 4
# преобразовать в верхний регистр

processed_words = map(lambda word: word.upper(), filter(lambda word: len(word) > 4, word_generator(text)))

print("\n8) Обработанный текст:")
for word in processed_words:
    print(word)