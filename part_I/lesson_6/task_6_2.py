def count_time(ammunitions):
    """
    За сколько секунд пулемётчик расстреляет все патроны.
    :param ammunitions: количество патронов
    :return: время в секундах
    """
    if 250 <= ammunitions <= 10000:
        strip = int(ammunitions / 250 - 0.0001)
        work_time = ammunitions * 60 / 1200 + 20 * strip
        print('Потребуется', work_time, 'секунд')
    else:
        print('Введите число от 250 до 10000.')


if __name__ == '__main__':
    input_ammunitions = int(input('количество патронов: '))
    count_time(input_ammunitions)
