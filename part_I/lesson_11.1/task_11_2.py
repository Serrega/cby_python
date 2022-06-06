class MyClass:
    def __init__(self, name, prepayment, summa):
        self.name = name
        self.prepay = prepayment
        self.summa = summa


class My2Class(MyClass):
    def __init__(self, name, prepayment, summa, salary, summa2):
        self.salary = salary
        self.summa2 = summa2
        super().__init__(name, prepayment, summa)


if __name__ == '__main__':
    guy_1 = MyClass('Егор Конюхов', 'аванс', '10500')
    guy_2 = My2Class('Мария Илюшина', 'аванс', '15000', 'зарплата', '35000')
    print(f"{guy_1.name} - {guy_1.prepay} {guy_1.summa} рублей")
    print(f"{guy_2.name} - {guy_2.prepay} {guy_2.summa} рублей, "
          f"{guy_2.salary} {guy_2.summa2} рублей")
