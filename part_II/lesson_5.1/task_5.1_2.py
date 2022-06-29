from queue import LifoQueue


if __name__ == '__main__':
    q = LifoQueue()
    print('Собираем стопку монет...')
    for i in range(1, 11):
        q.put(i)
        print(i, end=' ')
    print('\nРазбираем стопку монет...')
    while not q.empty():
        print(q.get(), end=' ')

