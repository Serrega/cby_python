if __name__ == '__main__':
    with open('symbol.txt', 'r', encoding='utf-8') as file_r:
        contents = file_r.read()
    for sub in range(0, len(contents) - 1, 8):
        print(f'{contents[sub: sub + 8].ljust(16, "."):,>24}')

    with open('symbol.txt', 'r') as reader:
        while first_8 := reader.read(8):
            print(f'{first_8[:4]:,>12}{first_8[4:]:.<12}')

