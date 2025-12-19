# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    # Считываем входные данные X, Y, Z из одной строки, разделенные пробелами
    # map(int, input().split()) преобразует строку ввода в список целых чисел
    try:
    X, Y, Z = map(int, input().split())

    # Цены товаров:
    price_pencil = 3
    price_pen = 5
    price_marker = 12

    # Вычисляем общую стоимость покупки
    total_cost = (X * price_pencil) + (Y * price_pen) + (Z * price_marker)

    # Выводим результат
    print(total_cost)

    except ValueError:
    print("Ошибка ввода. Пожалуйста, введите три целых числа, разделенных пробелами.")

   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()