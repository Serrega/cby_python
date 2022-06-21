import re


if __name__ == '__main__':
    text = 'Сначала был адрес http://yandex.ru, потом стал https://yandex.ru. \
            Гугл https://google.com имеет шире охват чем https://yandex.ru.'
    res = re.findall(r'(\d+:){2}\d+', text)
    print(res.group())

