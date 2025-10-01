import csv

library = {
    		"Война и мир": {
			"author": "Л. Толстой", 
			"year": 1869, 
			"ratings": [5, 4, 5]
		},
    		"Преступление и наказание": {
			"author": "Ф. Достоевский", 
			"year": 1866, 
			"ratings": [5, 5, 4]
		}
}



def new_book():
    name = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = int(input("Введите год издания: "))
    ratings_input = input("Введите оценки через пробел: ")
    ratings = list(map(int, ratings_input.split())) 
    library[name] = {
        "author": author, 
        "year": year, 
        "ratings": ratings
    }

def show_lib():
    if not library:
        print("Библиотека пуста")
        return
        
    for name in library:
        print(f"Название: {name}")
        print(f"Автор: {library[name]['author']}")
        print(f"Год: {library[name]['year']}")
        print(f"Оценки: {library[name]['ratings']}")
        print(f"Средний рейтинг: {sum(library[name]['ratings'])/len(library[name]['ratings']):.1f}")
        print("-" * 30)

def search_book():
    s_name = input("Введите название книги для поиска: ")
    if s_name in library:
        print(f"Название: {s_name}")
        print(f"Автор: {library[s_name]['author']}")
        print(f"Год: {library[s_name]['year']}")
        print(f"Оценки: {library[s_name]['ratings']}")
    else:
        print("Книга не найдена")

def del_book():
    s_name = input("Введите название книги для удаления: ")
    if s_name in library:
        del library[s_name]
        print("Книга удалена")
    else:
        print("Книга не найдена")

def add_rating():
    s_name = input("Введите название книги: ")
    if s_name in library:
        ratings_input = input("Введите новые оценки через пробел: ")
        ratings = list(map(int, ratings_input.split()))
        library[s_name]["ratings"].extend(ratings) 
        print("Оценки добавлены")
    else:
        print("Книга не найдена")

def year_book():    
    s_year = int(input("Введите год: "))
    found = False
    
    for name in library:
        if library[name]["year"] > s_year:
            print(f"Название: {name}")
            print(f"Автор: {library[name]['author']}")
            print(f"Год: {library[name]['year']}")
            print(f"Оценки: {library[name]['ratings']}")
            print("-" * 30)
            found = True
    
    if not found:
        print("Книги не найдены")

def rating_book():
    s_rating = float(input("Введите минимальный рейтинг: "))
    found = False
    
    for name in library:
        ratings_list = library[name]["ratings"]
        avg_rating = sum(ratings_list) / len(ratings_list)
        
        if avg_rating > s_rating:
            print(f"Название: {name}")
            print(f"Автор: {library[name]['author']}")
            print(f"Год: {library[name]['year']}")
            print(f"Оценки: {library[name]['ratings']}")
            print(f"Средний рейтинг: {avg_rating:.1f}")
            print("-" * 30)
            found = True
    
    if not found:
        print('Книги не найдены')

def export_csv():
    try:
        with open('library.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Автор', 'Год', 'Оценки'])
            
            for name, info in library.items():
                writer.writerow([name, info['author'], info['year'], ';'.join(map(str, info['ratings']))])
        
        print("CSV файл создан успешно!")
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def import_csv():
    try:
        with open('library.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            
            imported_count = 0
            for row in reader:
                if len(row) >= 4:
                    name, author, year, ratings_str = row
                    ratings = list(map(int, ratings_str.split(';')))
                    
                    library[name] = {
                        'author': author,
                        'year': int(year),
                        'ratings': ratings
                    }
                    imported_count += 1
            
            print(f"Импортировано {imported_count} книг")
            
    except FileNotFoundError:
        print("Файл не найден. Сначала экспортируйте данные.")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")

while True:
    print("\n" + "="*50)
    print("БИБЛИОТЕКА КНИГ")
    print("="*50)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу по названию")
    print("4. Удалить книгу")
    print("5. Добавить новую оценку книге")
    print("6. Книги выпущенные после определённого года")
    print("7. Книги с рейтингом выше определённого порога")
    print("8. Экспортировать в CSV")
    print("9. Импортировать из CSV")
    print("10. Выход")
    print("="*50)
    
    try:
        user = int(input("Выберите действие (1-10): "))
        
        if user == 1:
            new_book()
        elif user == 2:
            show_lib()
        elif user == 3:
            search_book()
        elif user == 4:
            del_book()
        elif user == 5:
            add_rating()
        elif user == 6:
            year_book()
        elif user == 7:
            rating_book()
        elif user == 8:
            export_csv()
        elif user == 9:
            import_csv()
        elif user == 10:
            print("Выход из программы")
            break
        else:
            print("Неверный выбор. Введите число от 1 до 10.")
            
    except ValueError:
        print("Ошибка: введите число")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
