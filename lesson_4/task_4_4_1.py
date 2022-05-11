len_word = len(input('input str: '))
if len_word > 100:
    print('the number of characters must not exceed 100')
else:
    last_character = len_word % 10
    if last_character in (0, 5, 6, 7, 8, 9) or 10 < len_word < 15:
        print('str has', len_word, ' символов')
    elif last_character == 1:
        print('str has', len_word, ' символ')
    else:
        print('str has', len_word, ' символa')

