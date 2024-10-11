def deposit(balance):
        try:
            amount = float(input("Введите сумму для пополнения счета: "))
            if amount < 0:
                raise ValueError("Сумма не может быть отрицательной.")
            balance += amount
            print(f"Счет пополнен на {amount}. Текущий баланс: {balance}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        return balance

def purchase(balance, history):
        try:
            amount = float(input("Введите сумму покупки: "))
            if amount < 0:
                raise ValueError("Сумма не может быть отрицательной.")
            if amount > balance:
                print("Недостаточно средств на счете.")
            else:
                name = input("Введите название покупки: ")
                balance -= amount
                history.append((name, amount))
                print(f"Покупка '{name}' на сумму {amount} совершена. Текущий баланс: {balance}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        return balance, history

def show_history(history):
        if not history:
            print("История покупок пуста.")
        else:
            print("История покупок:")
            for name, amount in history:
                print(f"{name}: {amount}")

