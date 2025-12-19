# tasks/task1.py

def solve():
# Ниже пишите решение задачи
# Считываем входное число S из стандартного потока ввода
    # int(input()) преобразует введенную строку в целое число
    S = int(input())

    # Используем целочисленное деление для нахождения базового количества (x = S // 6)
    petya_serezha_count = S // 6
    katya_count = 4 * petya_serezha_count

    # Выводим результат в формате трех чисел, разделенных пробелами
    # f-строки (f-strings) в Python 3+ позволяют легко форматировать вывод
    print(f"{petya_serezha_count} {katya_count} {petya_serezha_count}")

    # Альтернативный способ вывода без f-строк:
    # print(petya_serezha_count, katya_count, petya_serezha_count)
    

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
    