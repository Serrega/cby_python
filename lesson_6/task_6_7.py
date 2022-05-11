def func_input():
    user_input = input('enter a sentence: ')
    count_symbols(user_input)
    count_words(user_input)
    count_frequency(user_input)


def count_symbols(my_str):
    print('symbols in sentence: ', len(set(my_str)))


def count_words(my_str):
    print('words in sentence: ', len(my_str.split()))


def count_frequency(my_str):
    for symbol in sorted(set(my_str)):
        print(symbol, ' - ', my_str.count(symbol))


if __name__ == '__main__':
    func_input()


