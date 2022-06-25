import re


if __name__ == '__main__':
    text = 'Сначала был адрес http://yandex.ru, потом стал https://yandex.ru. \
            Гугл https://google.com имеет шире охват чем https://yandex.ru.'
    res = set(re.findall(r'https?://[\w]+[.][\w]{2,3}', text))
    print(*res, sep='\n')

