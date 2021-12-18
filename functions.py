import sys


def open_file(file_name):
    try:
        with open(file_name, 'r') as numbers:
            number_list = numbers.read()
    except FileNotFoundError:
        print("Файл не найден")
        sys.exit(1)
    else:
        int_number_list = []
        number_str = ""
        for each in number_list:
            if each != " ":
                number_str += each
            else:
                try:
                    int_number_list.append(float(number_str))
                except ValueError:
                    print("Файл должен содержать только числа и пробелы")
                    sys.exit(1)
                number_str = ""
        try:
            int_number_list.append(float(number_str))
        except ValueError:
            print("Файл должен содержать только числа и пробелы")
            sys.exit(1)
    return int_number_list


def minimum_number(number_list):
    min_num = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] < min_num:
            min_num = number_list[i]
    return min_num


def maximum_number(number_list):
    max_num = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] > max_num:
            max_num = number_list[i]
    return max_num


def sum_of_numbers(number_list):
    sum_value = 0
    for i in range(len(number_list)):
        sum_value += number_list[i]
    return sum_value


def numbers_multiply(number_list):
    if len(number_list) == 0:
        return 0
    multiply_value = 1
    for i in range(len(number_list)):
        try:
            multiply_value *= number_list[i]
        except ArithmeticError:
            print("Ошибка переполнения")
            sys.exit(1)
    return multiply_value

print(open_file("open_file_test.txt"))