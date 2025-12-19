# tasks/task4.py

    def solve():
    # Считываем 3 строки и сразу кладем их в список
    # Затем объединяем их через разделитель '---'
    lines = [input() for _ in range(3)]
    print("---".join(lines))

if __name__ == "__main__":
    solve()
