from functions import minimum_number, maximum_number, sum_of_numbers, numbers_multiply, open_file
import random
import time
from datetime import datetime
import matplotlib.pyplot as plt


def time_of_performance():
    performance_durations = []
    for each in nums_in_file:
        test_file = open("test_file.txt", "w+")
        file_nums = [round(random.uniform(-100, 100), 2) for i in range(each)]
        file_nums_str = ""
        for num in file_nums:
            file_nums_str += f"{num} "
        test_file.write(file_nums_str)
        test_file.close()
        start_time = time.time()
        test_list = open_file("test_file.txt")
        exec("minimum_number(test_list)")
        exec("maximum_number(test_list)")
        exec("sum_of_numbers(test_list)")
        exec("numbers_multiply(test_list)")
        performance_durations.append(time.time() - start_time)
    return performance_durations


nums_in_file = [1000, 2000, 3000, 4000, 5000]

plt.plot(time_of_performance(), nums_in_file)
plt.title("Зависимость время выполнения от размера входгого файла")
plt.ylabel("Кол-во чисел в файле")
plt.xlabel("Время выполнения (сек)")
plt.savefig(f"outputs/chart.png")
