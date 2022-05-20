if __name__ == '__main__':
    try:
        with open('city.txt', 'r', encoding='utf-8') as file_r:
            print(file_r.read().count('\n'))
    except BaseException as be:
        print('file not opened', be)

    print(sum(1 for lines in open('city.txt', 'r', encoding='utf-8')))
