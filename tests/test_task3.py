    def solve():
    try:
        # Читаем строку ввода и разделяем её на числа a и b
        # a - сколько банок прострелил Гарри
        # b - сколько банок прострелил Ларри
        line = input().split()
        if not line:
            return
            
        a = int(line[0])
        b = int(line[1])

        # Поскольку одна банка общая, всего банок: (a + b - 1)
        # Не прострелил Гарри: (всего - a) = (a + b - 1) - a = b - 1
        # Не прострелил Ларри: (всего - b) = (a + b - 1) - b = a - 1
        
        harry_missed = b - 1
        larry_missed = a - 1

        # Выводим результат через пробел
        print(f"{harry_missed} {larry_missed}")
        
    except (ValueError, IndexError):
        pass

# Позволяет запускать файл напрямую
    if __name__ == "__main__":
    solve()
