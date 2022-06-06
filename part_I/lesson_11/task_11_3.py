class Person:
    def __init__(self, cash, name, position):
        self.__cash = cash
        self.name = name
        self.position = position

    def money(self):
        return self.__cash


people = Person('20000', 'Вася', 'Дворник')
man = Person('150000', 'Жора', 'Гендиректор')
print(f'{people.position} Иван получил зарплату {people.money()} рублей')
print(f'{man.position} Алексей получил зарплату {man.money()} рублей')

