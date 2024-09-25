import random
from directory import change_working_directory, create_directory, list_directory, list_only_directories
from path import copy_path, delete_path, list_only_files
from info import show_creator_info, show_os_info
from bank_account import deposit, purchase, show_history
from quiz import famous_people, format_date


def main():

    while True:
        print("\nКонсольный файловый менеджер")
        print("1. Список директорий")
        print("2. Создать директорию")
        print("3. Удалить файл/директорию")
        print("4. Копировать файл/директорию")
        print("5. Список содержимого рабочей директории")
        print("6. Список только директорий")
        print("7. Список только файлов")
        print("8. Информация об операционной системе")
        print("9. Создатель программы")
        print("10. Играть в викторину")
        print("11. Мой банковский счет")
        print("12. Сменить рабочую директорию")
        print("13. Выйти")
        choice = input("Введите ваш выбор: ")

        if choice == '1':
            path = input("Введите путь к директории: ")
            list_directory(path)
        elif choice == '2':
            path = input("Введите путь для создания директории: ")
            create_directory(path)
        elif choice == '3':
            path = input("Введите путь для удаления: ")
            delete_path(path)
        elif choice == '4':
            src = input("Введите путь источника: ")
            dst = input("Введите путь назначения: ")
            copy_path(src, dst)
        elif choice == '5':
            list_directory()
        elif choice == '6':
            path = input("Введите путь к директории: ")
            list_only_directories(path)
        elif choice == '7':
            path = input("Введите путь к директории: ")
            list_only_files(path)
        elif choice == '8':
            show_os_info()
        elif choice == '9':
            show_creator_info()
        elif choice == '10':
            while True:
                # Приветствие и описание задания
                print(
                    "Добро пожаловать в Викторину! В этой программе вы будете угадывать даты рождения известных людей.")
                print(
                    "Программа выберет 5 случайных людей из списка, и вам нужно будет ввести их дату рождения в формате 'dd.mm.yyyy'.")
                print("Если вы ошибетесь, программа покажет правильный ответ в формате 'третье января 2009 года'.")
                print(
                    "В конце будет подсчитано количество правильных и неправильных ответов, и вы сможете начать снова.")

                # Select 5 random people
                selected_people = random.sample(famous_people, 5)

                correct_answers = 0
                incorrect_answers = 0

                for person, birthdate in selected_people:
                    while True:
                        try:
                            user_input = input(f"Введите дату рождения {person} (в формате 'dd.mm.yyyy'): ")
                            if user_input == birthdate:
                                print("Верно!")
                                correct_answers += 1
                                break
                            else:
                                raise ValueError(f"Неверно! Правильный ответ: {format_date(birthdate)}")
                        except ValueError as e:
                            print(e)
                            incorrect_answers += 1

                print(f"\nПравильных ответов: {correct_answers}")
                print(f"Неправильных ответов: {incorrect_answers}")

                play_again = input("Хотите начать снова? (да/нет): ").strip().lower()
                if play_again != 'да':
                    break

        elif choice == '11':
            balance = 0
            history = []

            print("Добро пожаловать в программу 'Личный счет'!")
            print("Вы можете пополнять счет, совершать покупки и просматривать историю покупок.")

            while True:
                print("\n1. пополнение счета")
                print("2. покупка")
                print("3. история покупок")
                print("4. выход")

                choice = input("Выберите пункт меню: ")
                if choice == '1':
                    balance = deposit(balance)
                elif choice == '2':
                    balance, history = purchase(balance, history)
                elif choice == '3':
                    show_history(history)
                elif choice == '4':
                    print("Выход из программы.")
                    break
                else:
                    print("Неверный пункт меню")
        elif choice == '12':
            path = input("Введите путь для смены рабочей директории: ")
            change_working_directory(path)
        elif choice == '13':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()