import datetime


def decor(fun):
    def print_data(*args):
        result = fun(*args)
        now = datetime.datetime.today().strftime("%a %b %d %H:%M:%S %Y")
        print(f"\t {now}")
        return result
    return print_data

@decor
class MyClass:
    def __init__(self, text):
        print("\t", text)

@decor
def my_func(arg_1, arg_2):
    print(f"\t складываем числа {arg_1} + {arg_2}")
    return  arg_1 + arg_2


if __name__ == '__main__':
    print()
    MyClass("python")
    print()
    answer = my_func(10, 20)
    print("\t\n\t результат сложения равен =", answer)
