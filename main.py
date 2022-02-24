import random


def rand_massive(n):
    output_mas = []
    for item in range(0, n):  # генерация массива до числа n
        output_mas.append(
            [random.randint(0, 1000000) for i in range(0, item + 1)])  # генерация массивов случайных чисел
        # размер массива генерируется от 1 до n+1
    random.shuffle(output_mas)  # перемешивание массивов
    for item in range(0, len(output_mas)):
        output_mas[item].sort(reverse=False if item % 2 == 0 else True)
        # сортировка массива
        # по возрастанию чётных массивов и по убыванию нечётных
    return output_mas
    # возврат массива с массивами


if __name__ == '__main__':
    print(rand_massive(4))
