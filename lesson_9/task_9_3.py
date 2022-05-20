try:
    with open('city.txt', 'r', encoding='utf-8') as file_r, \
            open('city_2.txt', 'a', encoding='utf-8') as file_a:
        content = file_r.readlines()
        [file_a.write(line) for line in content if 'о' not in line]
except BaseException as be:
    print('file i\\o error', be)
