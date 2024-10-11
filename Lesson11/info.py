import platform

def show_os_info():
    """Показать информацию об операционной системе."""
    print(f"Операционная система: {platform.system()}")
    print(f"Версия: {platform.version()}")
    print(f"Архитектура: {platform.architecture()}")

def show_creator_info():
    """Показать информацию о создателе программы."""
    print("Создатель программы: Ваше Григоpий")