    def solve():
    try:
        # Считываем три числа (X, Y, Z) из одной строки через пробел
        line = input().split()
        if not line:
            return

        x = int(line)
        y = int(line)
        z = int(line)

        # Цены: карандаш=3, ручка=5, фломастер=12
        price_pencil = 3
        price_pen = 5
        price_marker = 12

        # Рассчитываем общую стоимость покупки
        total_cost = x * price_pencil + y * price_pen + z * price_marker

        # Выводим результат
        print(total_cost)

    except (ValueError, IndexError):
        # Обработка ошибок ввода
        pass

# Этот блок позволяет запускать задачу напрямую, если она не импортируется тестами
    if __name__ == "__main__":
    solve()
