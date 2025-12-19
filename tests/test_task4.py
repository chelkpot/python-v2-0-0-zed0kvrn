    def solve():
    # Последовательно считываем три строки, удаляя лишние пробелы по краям
    a = input().strip()
    b = input().strip()
    c = input().strip()
    
    # Выводим их, соединяя через три дефиса
    print(f"{a}---{b}---{c}")

    if __name__ == "__main__":
    solve()
