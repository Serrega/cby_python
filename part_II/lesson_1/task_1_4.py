import argparse
import itertools
import random
import string
import time


class RandomNum:
    def __init__(self):
        list_numbers = self.construct()
        self.write_file(list_numbers)

    def timer(fun):
        def speed(*args):
            start = time.time()
            fun(*args)
            print(f'Completed in: {time.time() - start:.2f} sec.')
        return speed

    def construct(self) -> list:
        lst = list(itertools.product(string.digits, repeat=args.length))
        random.shuffle(lst)
        for i, sequens in enumerate(lst):
            lst[i] = ''.join(sequens) + '\n'
        return lst

    @timer
    def write_file(self, lst):
        print('Start process...')
        print(f'Количество комбинаций: {10**args.length}')
        with open(f'num_dict{str(args.length)}.txt', 'w') as file_w:
            file_w.write(''.join(lst))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('length', help='length combinations', type=int)
    args = parser.parse_args()
    p = RandomNum()
