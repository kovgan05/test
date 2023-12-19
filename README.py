def filter_strings(input_array):
    # Инициализация пустого массива для результата
    result_array = []

    # Фильтрация строк длиной меньше или равной 3 символам
    for string in input_array:
        if len(string) <= 3:
            result_array.append(string)

    return result_array

def main():
    # Ввод массива строк с клавиатуры
    n = int(input("Введите количество строк в массиве: "))
    input_array = []

    for i in range(n):
        input_string = input(f"Введите строку {i + 1}: ")
        input_array.append(input_string)

    # Вызов функции фильтрации
    filtered_array = filter_strings(input_array)

    # Вывод результата
    print("\nРезультирующий массив:")
    for string in filtered_array:
        print(string)

if __name__ == "__main__":
    main()
