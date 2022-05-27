from random import randint


class Target:
    _name = ('Artur', 'Dan', 'Semen')

    def __init__(self):
        self.count = {x: y for x in self._name for y in
                      [[randint(5, 10) for _ in range(3)] for j in range(3)]}
        for name in self._name:
            self.result(name)
        self.win()

    def result(self, name):
        print(f'\nСтреляет {name}:')
        for ind, num in enumerate(self.count[name], 1):
            print(f'Попытка {ind}: {num:0>2} оч. ', end='')
            if num == 10:
                print('Меткий выстрел')
            elif num == 8 or num == 9:
                print('Неплохо')
            elif 0 < num < 8:
                print('Так себе')
            else:
                print('Мазила!')

    def win(self):
        p = sorted(self.count.items(), key=lambda x: sum(x[1]), reverse=True)
        print('-'*30)
        for ind, guy in enumerate(p, 1):
            print(f'{ind} место в стрельбе из лука: '
                  f'{guy[0]} - {sum(guy[1])} оч.')


if __name__ == '__main__':
    my_target = Target()


