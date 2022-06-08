import argparse
import itertools
import glob
import os
import random
import string
import time


class RandomNum:
    def __init__(self):
        self.num_comb = 10**args.length
        self.construct()
        self.write_file()

    def timer(fun):
        def speed(*args):
            start = time.time()
            fun(*args)
            print(f'Completed in: {time.time() - start:.2f} sec.')
        return speed

    def construct(self):
        for comb in itertools.product(string.digits, repeat=args.length):
            p = ''.join(comb)
            with open(f'task4_{p}.tmp', 'w') as file_w:
                file_w.write(p)

    @timer
    def write_file(self):
        print('Start process...')
        print(f'Количество комбинаций: {self.num_comb}')
        with open(f'num_dict{str(args.length)}.txt', 'a') as file_a:
            while glob.glob('./task4_*.tmp'):
                r_num = str(random.randint(0, self.num_comb - 1)
                            ).zfill(args.length)
                if glob.glob(f'./task4_{r_num}.tmp'):
                    file_a.writelines(f'{r_num}\n')
                    os.remove(f'./task4_{r_num}.tmp')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('length', help='length combinations', type=int)
    args = parser.parse_args()
    p = RandomNum()
