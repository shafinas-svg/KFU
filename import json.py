import json
from datetime import datetime

class Task:
    # МЕТОД: КОНСТРУКТОР - создание новой задачи
    def __init__(self, title, description, deadline, priority="средний"):
        self.title = title
        self.description = description
        self.created_at = datetime.now().strftime("%Y-%m-%d")
        self.deadline = deadline
        self.status = "новая"
        self.priority = priority
        self.__progress_value = 0
    
    # МЕТОД: ОТМЕТИТЬ ВЫПОЛНЕННОЙ - меняет статус на "выполнено" и прогресс на 100%
    def mark_done(self):
        self.status = "выполнено"
        self.__progress_value = 100
        print(f"Задача '{self.title}' выполнена!")
    
    # МЕТОД: ПРОВЕРИТЬ ПРОСРОЧКУ - возвращает True если задача просрочена
    def check_overdue(self):
        if self.status == "выполнено":
            return False
        today = datetime.now().strftime("%Y-%m-%d")
        return today > self.deadline
    
    # МЕТОД: ПОЛУЧИТЬ ПРОГРЕСС - возвращает текущее значение прогресса
    def get_progress(self):
        return self.__progress_value
    
    # МЕТОД: УСТАНОВИТЬ ПРОГРЕСС - изменяет значение прогресса с проверками
    def set_progress(self, percent):
        if percent < 0:
            print("Не может быть меньше 0!")
            return
        if percent > 100:
            print("Не может быть больше 100!")
            return
        
        self.__progress_value = percent
        if self.__progress_value == 100:
            self.mark_done()
    
    # МЕТОД: ПОКАЗАТЬ ИНФОРМАЦИЮ - возвращает строку с информацией о задаче
    def show_info(self):
        overdue = " (ПРОСРОЧЕНА!)" if self.check_overdue() else ""
        return f"{self.title} - {self.status} - Приоритет: {self.priority} - Прогресс: {self.__progress_value}%{overdue}"

class WorkTask(Task):
    # МЕТОД: КОНСТРУКТОР РАБОЧЕЙ ЗАДАЧИ - создает рабочую задачу с проектом
    def __init__(self, title, description, deadline, project, priority="средний"):
        super().__init__(title, description, deadline, priority)
        self.project = project
    
    # МЕТОД: ПОКАЗАТЬ ИНФОРМАЦИЮ - переопределяет метод для показа информации о рабочей задаче
    def show_info(self):
        base = super().show_info()
        return f"{base} - Проект: {self.project}"

class PersonalTask(Task):
    # МЕТОД: КОНСТРУКТОР ЛИЧНОЙ ЗАДАЧИ - создает личную задачу с категорией
    def __init__(self, title, description, deadline, category, priority="средний"):
        super().__init__(title, description, deadline, priority)
        self.category = category
    
    # МЕТОД: ПОКАЗАТЬ ИНФОРМАЦИЮ - переопределяет метод для показа информации о личной задаче
    def show_info(self):
        base = super().show_info()
        return f"{base} - Категория: {self.category}"

class TaskList:
    # МЕТОД: КОНСТРУКТОР МЕНЕДЖЕРА - создает пустой список задач
    def __init__(self):
        self.all_tasks = []
    
    # МЕТОД: ДОБАВИТЬ ЗАДАЧУ - добавляет задачу в список
    def add(self, task):
        self.all_tasks.append(task)
        print(f"Добавлена: {task.title}")
    
    # МЕТОД: УДАЛИТЬ ЗАДАЧУ - удаляет задачу по названию
    def delete(self, title):
        found = False
        for t in self.all_tasks:
            if t.title == title:
                self.all_tasks.remove(t)
                print(f"Удалена: {title}")
                found = True
                break
        if not found:
            print("Не найдена!")
    
    # МЕТОД: ПОКАЗАТЬ ВСЕ ЗАДАЧИ - выводит все задачи с сортировкой по приоритету
    def show_all(self):
        if not self.all_tasks:
            print("Нет задач")
            return
        
        priority_num = {"высокий": 3, "средний": 2, "низкий": 1}
        sorted_list = sorted(self.all_tasks, key=lambda x: priority_num[x.priority], reverse=True)
        
        print("\n--- ВСЕ ЗАДАЧИ ---")
        for i, t in enumerate(sorted_list, 1):
            print(f"{i}. {t.show_info()}")
    
    # МЕТОД: ПОКАЗАТЬ ПРОСРОЧЕННЫЕ - выводит только просроченные задачи
    def show_late(self):
        late_tasks = [t for t in self.all_tasks if t.check_overdue()]
        
        if not late_tasks:
            print("Нет просроченных задач")
            return
        
        print("\n--- ПРОСРОЧЕННЫЕ ЗАДАЧИ ---")
        for i, t in enumerate(late_tasks, 1):
            print(f"{i}. {t.show_info()}")
    
    # МЕТОД: СОХРАНИТЬ В ФАЙЛ - сохраняет все задачи в JSON файл
    def save_tasks(self, file_name):
        data = []
        for t in self.all_tasks:
            task_data = {
                "название": t.title,
                "описание": t.description,
                "создана": t.created_at,
                "срок": t.deadline,
                "статус": t.status,
                "приоритет": t.priority,
                "прогресс": t.get_progress()
            }
            
            if isinstance(t, WorkTask):
                task_data["тип"] = "рабочая"
                task_data["проект"] = t.project
            elif isinstance(t, PersonalTask):
                task_data["тип"] = "личная"
                task_data["категория"] = t.category
            
            data.append(task_data)
        
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Сохранено в {file_name}")
        self.save_done()
    
    # МЕТОД: СОХРАНИТЬ ВЫПОЛНЕННЫЕ - сохраняет выполненные задачи в отдельный файл
    def save_done(self):
        done_tasks = [t for t in self.all_tasks if t.status == "выполнено"]
        
        if done_tasks:
            done_data = []
            for t in done_tasks:
                task_data = {
                    "название": t.title,
                    "описание": t.description,
                    "создана": t.created_at,
                    "срок": t.deadline,
                    "статус": t.status,
                    "приоритет": t.priority,
                    "прогресс": t.get_progress()
                }
                
                if isinstance(t, WorkTask):
                    task_data["тип"] = "рабочая"
                    task_data["проект"] = t.project
                elif isinstance(t, PersonalTask):
                    task_data["тип"] = "личная"
                    task_data["категория"] = t.category
                
                done_data.append(task_data)
            
            with open('выполненные_задачи.json', 'w', encoding='utf-8') as f:
                json.dump(done_data, f, ensure_ascii=False, indent=2)
            print("Выполненные задачи сохранены в выполненные_задачи.json")
    
    # МЕТОД: ЗАГРУЗИТЬ ИЗ ФАЙЛА - загружает задачи из JSON файла
    def load_tasks(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.all_tasks = []
            for item in data:
                if item.get("тип") == "рабочая":
                    task = WorkTask(
                        title=item["название"],
                        description=item["описание"],
                        deadline=item["срок"],
                        project=item["проект"],
                        priority=item["приоритет"]
                    )
                elif item.get("тип") == "личная":
                    task = PersonalTask(
                        title=item["название"],
                        description=item["описание"],
                        deadline=item["срок"],
                        category=item["категория"],
                        priority=item["приоритет"]
                    )
                
                task.created_at = item["создана"]
                task.status = item["статус"]
                task.set_progress(item["прогресс"])
                
                self.all_tasks.append(task)
            
            print(f"Загружено из {file_name}")
        
        except FileNotFoundError:
            print("Файл не найден!")

# ГЛАВНЫЙ МЕТОД: ЗАПУСК ПРОГРАММЫ
task_manager = TaskList()

# МЕТОД: ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ
while True:
    print("\n*** МЕНЕДЖЕР ЗАДАЧ ***")
    print("1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Показать все")
    print("4. Показать просроченные")
    print("5. Обновить прогресс")
    print("6. Сохранить")
    print("7. Загрузить")
    print("8. Выйти")
    
    choice = input("Выберите: ")
    
    if choice == "1":
        print("1 - Рабочая, 2 - Личная")
        type_choice = input("Тип: ")
        
        name = input("Название задачи: ")
        details = input("Описание: ")
        due = input("Срок (гггг-мм-дд): ")
        imp = input("Приоритет (высокий/средний/низкий): ")
        
        if type_choice == "1":
            proj = input("Проект: ")
            new_task = WorkTask(name, details, due, proj, imp)
        else:
            cat = input("Категория: ")
            new_task = PersonalTask(name, details, due, cat, imp)
        
        task_manager.add(new_task)
    
    elif choice == "2":
        name = input("Название задачи для удаления: ")
        task_manager.delete(name)
    
    elif choice == "3":
        task_manager.show_all()
    
    elif choice == "4":
        task_manager.show_late()
    
    elif choice == "5":
        task_manager.show_all()
        if task_manager.all_tasks:
            try:
                num = int(input("Номер задачи: ")) - 1
                if 0 <= num < len(task_manager.all_tasks):
                    p = int(input("Процентов добавить: "))
                    task_manager.all_tasks[num].set_progress(p)
                else:
                    print("Неверный номер!")
            except:
                print("Ошибка!")
    
    elif choice == "6":
        fname = input("Имя файла: ")
        task_manager.save_tasks(fname)
    
    elif choice == "7":
        fname = input("Имя файла: ")
        task_manager.load_tasks(fname)
    
    elif choice == "8":
        print("Пока!")
        break
    
    else:
        print("Неверный выбор!")