import os


class NotesManager:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        self.folder_name = os.path.join(base_dir, "notes")

        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
            print("Папка notes создана.")
        else:
            print("Папка notes уже существует.")

    def add_note(self, title, text):
        if title == "":
            print("Название заметки не должно быть пустым.")
            return

        file_path = os.path.join(self.folder_name, title + ".txt")

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)
            print("Заметка успешно создана.")
        except Exception as error:
            print("Ошибка при создании заметки:", error)

    def list_notes(self):
        try:
            files = os.listdir(self.folder_name)

            if len(files) == 0:
                print("Заметок нет.")
                return

            print("Список заметок:")
            for file_name in files:
                print(file_name)
        except Exception as error:
            print("Ошибка при выводе списка заметок:", error)

    def read_note(self, title):
        file_path = os.path.join(self.folder_name, title + ".txt")

        if not os.path.exists(file_path):
            print("Такой заметки нет.")
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            print("Содержимое заметки:")
            print(text)
        except Exception as error:
            print("Ошибка при чтении заметки:", error)

    def delete_note(self, title):
        file_path = os.path.join(self.folder_name, title + ".txt")

        if not os.path.exists(file_path):
            print("Такой заметки нет.")
            return

        try:
            os.remove(file_path)
            print("Заметка удалена.")
        except Exception as error:
            print("Ошибка при удалении заметки:", error)

    def clear_notes(self):
        try:
            files = os.listdir(self.folder_name)

            if len(files) == 0:
                print("Папка уже пустая.")
                return

            for file_name in files:
                file_path = os.path.join(self.folder_name, file_name)
                os.remove(file_path)

            print("Все заметки удалены.")
        except Exception as error:
            print("Ошибка при удалении всех заметок:", error)


def show_menu():
    print("\n--- Менеджер заметок ---")
    print("1 - Добавить заметку")
    print("2 - Показать все заметки")
    print("3 - Прочитать заметку")
    print("4 - Удалить заметку")
    print("5 - Удалить все заметки")
    print("0 - Выход")


def main():
    manager = NotesManager()

    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название заметки: ")
            text = input("Введите текст заметки: ")
            manager.add_note(title, text)

        elif choice == "2":
            manager.list_notes()

        elif choice == "3":
            title = input("Введите название заметки: ")
            manager.read_note(title)

        elif choice == "4":
            title = input("Введите название заметки: ")
            manager.delete_note(title)

        elif choice == "5":
            answer = input("Удалить все заметки? (да/нет): ")
            if answer.lower() == "да":
                manager.clear_notes()
            else:
                print("Удаление отменено.")

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()