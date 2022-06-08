import click
import itertools
import glob
import os
import random
import string
import time


@click.command()
@click.option('-l', '--length')
class RandomNum:
    def __init__(self, length):
        self.length = int(length)
        self.num_comb = 10**self.length
        self.construct()
        self.write_file()

    def timer(fun):
        def speed(*args):
            start = time.time()
            fun(*args)
            print(f'Completed in: {time.time() - start:.2f} sec.')
        return speed

    def construct(self) -> list:
        for comb in itertools.product(string.digits, repeat=self.length):
            p = ''.join(comb)
            with open(f'task4_{p}.tmp', 'w') as file_w:
                file_w.write(p)

    @timer
    def write_file(self):
        print('Start process...')
        print(f'Количество комбинаций: {self.num_comb}')
        with open(f'num_dict{str(self.length)}.txt', 'a') as file_a:
            while glob.glob('./task4_*.tmp'):
                rand_list = set([str(random.randint(0, self.num_comb - 1)
                                     ).zfill(self.length) for _ in range(10**(self.length - 1))])
                for r_num in rand_list:
                    if glob.glob(f'./task4_{r_num}.tmp'):
                        file_a.writelines(f'{r_num}\n')
                        os.remove(f'./task4_{r_num}.tmp')


if __name__ == '__main__':
    p = RandomNum()
