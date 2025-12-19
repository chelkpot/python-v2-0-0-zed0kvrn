# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    # Считываем три строки из стандартного ввода, каждая на своей строке
    line1 = input()
    line2 = input()
    line3 = input()

    # Объединяем строки с помощью метода .join() или просто через конкатенацию
    separator = "---"

    # Использование f-строки (самый читаемый способ):
    output_string = f"{line1}{separator}{line2}{separator}{line3}"

    # Альтернативный способ с использованием .join()
    # output_string = separator.join([line1, line2, line3])

    # Выводим результат
    print(output_string)
    

    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
    