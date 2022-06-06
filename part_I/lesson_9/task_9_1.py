def write_content(file_name: str, data: list):
    try:
        with open(file_name, 'a') as file_a:
            for line in data:
                file_a.write(line + '\n')
    except BaseException as be:
        print('file not written', be)


if __name__ == '__main__':
    content = [str(i + 1) for i in range(10)]
    write_content('numbers.txt', content)
