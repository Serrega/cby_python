import argparse
import itertools
import random
import time


class RandomNum:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('length', help='length combinations', type=int)
        args = parser.parse_args()
        self.lenght = args.length
        list_numbers = self.construct()
        self.write_file(list_numbers)

    def timer(fun):
        def speed(*args):
            start = time.time()
            fun(*args)
            print(f'Completed in: {time.time() - start:.2f} sec.')

        return speed

    def construct(self) -> list:
        lst = list(itertools.product('0123456789', repeat=self.lenght))
        random.shuffle(lst)
        for i, sequens in enumerate(lst):
            lst[i] = ''.join(sequens) + '\n'
        return lst

    @timer
    def write_file(self, lst):
        print('Start process...')
        print(f'Количество комбинаций: {len(lst)}')
        with open(f'num_dict{str(self.lenght)}.txt', 'w', encoding='utf-8') as file_w:
            file_w.write(''.join(lst))


if __name__ == '__main__':
    p = RandomNum()
