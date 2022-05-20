woman = ('ВА', 'НА', 'АЯ')
with open('surnames.txt', 'r', encoding='utf-8') as file_r, \
        open('woman.txt', 'a', encoding='utf-8') as file_a:
    content = file_r.readlines()
    [file_a.writelines([i[0].casefold().capitalize() + '-' +
                        i[2].casefold().capitalize()
    if i[1] == '-' else i.casefold().capitalize() for i in
        [line.partition('-') if '-' in line else line for line in content]])
            for line in content if line[-3:-1] in woman]

