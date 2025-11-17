# def main():
#     user_input = input().lower()
    
#     # Предварительная обработка строки
#     cleaned_line = user_input.replace(' ', '')
#     words = cleaned_line.split(',')
#     chars_only = cleaned_line.replace(',', '')
    
#     # 1. Список слов без пробелов
#     print('1 Задание', '=' * 40)
#     print(words)
    
#     # 2. Строка в нижнем регистре
#     print('2 Задание', '=' * 40)
#     print(user_input)
    
#     # 3. Количество уникальных символов
#     print('3 Задание', '=' * 40)
#     unique_chars = set(chars_only)
#     print(len(unique_chars))
    
#     # 4. Слово с максимальным количеством 'o'
#     print('4 Задание', '=' * 40)
#     max_o_word = max(words, key=lambda word: word.count('o'))
#     print(max_o_word)
    
#     # 5-6. Словарь с количеством гласных и слово с максимальным количеством гласных
#     print('5-6 Задание', '=' * 40)
#     vowels = 'aeiouy'
#     vowel_counts = {
#         word: sum(word.count(vowel) for vowel in vowels)
#         for word in words
#     }
#     print(vowel_counts)
#     max_vowel_word = max(vowel_counts, key=vowel_counts.get)
#     print(max_vowel_word)
    
#     # 7. Слова длиннее или равные средней длине
#     print('7 Задание', '=' * 40)
#     avg_length = len(chars_only) / len(words)
#     long_words = [word for word in words if len(word) >= avg_length]
#     print(long_words)
    
#     # 8. Кортеж слов в обратном порядке
#     print('8 Задание', '=' * 40)
#     reversed_tuple = tuple(reversed(words))
#     print(reversed_tuple)
    
#     # 9. Слова начинающиеся на 'c' или 'k'
#     print('9 Задание', '=' * 40)
#     ck_words = [word for word in words if word.startswith(('c', 'k'))]
#     print(ck_words if ck_words else 'Нет таких овощей')
    
#     # 10. Слова длиннее заданного числа
#     print('10 Задание', '=' * 40)
#     try:
#         min_length = int(input("Введите минимальную длину слова: "))
#         long_words_user = [word for word in words if len(word) > min_length]
#         print(long_words_user)
#     except ValueError:
#         print("Ошибка: введите целое число")


# main()
a = int(input())

if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)