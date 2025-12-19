# tasks/task2.py

    def solve():
    # Ниже пишите решение задачи
    try:
        # Считываем X, Y, Z из одной строки
        line = input().split()
        if not line:
            return
            
        X = int(line[0])
        Y = int(line[1])
        Z = int(line[2])

        # Цены товаров:
        # Карандаш = 3 рубля
        # Ручка = 3 + 2 = 5 рублей
        # Фломастер = 5 + 7 = 12 рублей
        price_pencil = 3
        price_pen = 5
        price_marker = 12

        # Вычисляем общую стоимость
        total_cost = (X * price_pencil) + (Y * price_pen) + (Z * price_marker)

        # Выводим только итоговое число
        print(total_cost)

    except (ValueError, IndexError):
        # Тесты обычно не ожидают сообщений об ошибках, 
        # поэтому оставляем блок пустым или просто выходим
        pass

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
