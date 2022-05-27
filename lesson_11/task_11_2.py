class Counts:
    '''
    Класс Аммуниции
    '''
    def __init__(self):
        self.ammunitions = int(input('количество патронов: '))
        if 250 <= self.ammunitions <= 10000:
            self.count_time()
        else:
            print('Введите число от 250 до 10000.')

    def count_time(self):
        strip = int(self.ammunitions / 250 - 0.0001)
        work_time = self.ammunitions * 60 / 1200 + 20 * strip
        print('Потребуется', work_time, 'секунд')


if __name__ == '__main__':
    exs_count = Counts()
