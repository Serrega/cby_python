def count_characters(text):
    """
    Функция считает количество символов во входящей строке без учёта пробелов.
    :param text: входящая строка
    :return: длина входящей строки
    """
    return len(text.replace(' ', ''))


if __name__ == '__main__':
    input_text = input('Input text: ')
    print(count_characters(input_text))
