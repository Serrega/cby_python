class Counts:
    '''
    Test Class
    '''
    def count_characters(self, text):
        '''
        Функция считает количество символов во входящей строке без учёта пробелов.
        :param text: входящая строка
        :return: длина входящей строки
        '''
        return len(text.replace(' ', ''))


if __name__ == '__main__':
    input_text = input('Input text: ')
    exs_count = Counts()
    print(exs_count.count_characters(input_text))
