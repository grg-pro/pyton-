import os
import shutil

def list_only_files(path='.'):
    """Список только файлов в указанном пути."""
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(entry.name)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")



def delete_path(path):
    """Удалить существующий файл или директорию."""
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Директория '{path}' успешно удалена.")
        elif os.path.isfile(path):
            os.remove(path)
            print(f"Файл '{path}' успешно удален.")
        else:
            print(f"Путь '{path}' не существует.")
    except OSError as e:
        print(f"Ошибка: {e}")

def copy_path(src, dst):
    """Копировать файл или директорию."""
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst)
            print(f"Директория '{src}' успешно скопирована в '{dst}'.")
        elif os.path.isfile(src):
            shutil.copy2(src, dst)
            print(f"Файл '{src}' успешно скопирован в '{dst}'.")
        else:
            print(f"Путь '{src}' не существует.")
    except OSError as e:
        print(f"Ошибка: {e}")