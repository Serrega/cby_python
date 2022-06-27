import threading
import time


def plus_one():
    global x
    x += 1


def minus_one():
    global x
    x -= 1


def thread_task(num, func):
    with lock:
        for _ in range(num):
            func()


def main_task():
    global x
    x = 500000
    p1 = threading.Thread(target=thread_task(500000, plus_one))
    p1.start()
    time.sleep(3)
    p2 = threading.Thread(target=thread_task(300000, minus_one))
    p2.start()
    p1.join()
    p2.join()


x = 0
print('Start of the process...')
lock = threading.Lock()
for i in range(1, 11):
    main_task()
    print(f'Iteration {i:>2}: x={x}')
print('Done!')
