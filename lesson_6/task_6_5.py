def count_characters(text='python'):
    all_text = [text]
    while True:
        input_text = input('Input new word: ')
        if input_text == '':
            print(all_text)
            return
        elif input_text in all_text:
            print('Строка', input_text, 'уже присутствует в списке на позиции',
                  all_text.index(input_text))
        else:
            all_text.append(input_text)


if __name__ == '__main__':
    count_characters()
