import threading
from PIL import Image


def my_func():
    print('Привет Бро! Я занял первое место в конкурсе!')
    img = Image.open(r'nb.png')
    img.show()


if __name__ == '__main__':
    p = threading.Thread(target=my_func)
    p.start()