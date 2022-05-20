def write_content(file_name: str, data: str):
    try:
        with open(file_name, 'w') as file_w:
            file_w.write(data)
    except BaseException as be:
        print('file not written', be)


if __name__ == '__main__':
    content = '\n'.join([str(i + 1) for i in range(10)])
    write_content('numbers.txt', content)
