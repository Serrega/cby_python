import threading
from PIL import Image


def my_func():
    img = Image.open('nb.png')
    img.show()


if __name__ == '__main__':
    print('Привет Бро! Я занял первое место в конкурсе!')
    p = threading.Timer(5, my_func)
    p.start()
    p.join()