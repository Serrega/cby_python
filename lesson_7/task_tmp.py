def none_func(x):
    return x


def func_my_encoding(text: str):
    return text[::-1]


def my_func(url: str, func=none_func):
    if func != none_func:
        url = func(url)
    print(url)


def main():
    url = '127.0.0.1'
    my_func(url, func_my_encoding)
    my_func(url)


if __name__ == '__main__':
    main()

