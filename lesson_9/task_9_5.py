woman = ('ВА', 'НА', 'АЯ')
try:
    with open('surnames.txt', 'r', encoding='utf-8') as file_r, \
            open('woman.txt', 'a', encoding='utf-8') as file_a:
        content = file_r.readlines()
        [file_a.write(line.casefold().capitalize())
         for line in content if line[-3:-1] in woman]
except BaseException as be:
    print('file i\\o error', be)
