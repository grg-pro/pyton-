import os

def change_working_directory(path):
    """Сменить рабочую директорию."""
    try:
        os.chdir(path)
        print(f"Рабочая директория изменена на '{path}'.")
    except OSError as e:
        print(f"Ошибка: {e}")

def create_directory(path):
    """Создать новую директорию."""
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Директория '{path}' успешно создана.")
    except OSError as e:
        print(f"Ошибка: {e}")


def list_directory(path='.'):
    """Список файлов и директорий в указанном пути."""
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")



def list_only_directories(path='.'):
    """Список только директорий в указанном пути."""
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(entry.name)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")