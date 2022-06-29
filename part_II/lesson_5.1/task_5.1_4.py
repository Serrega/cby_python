from multiprocessing import Process, Queue


def soldier(q):
    while not q.empty():
        print(q.get(), end=' ')


if __name__ == '__main__':
    q = Queue()
    ammunitions = 150
    for i in range(1, 6):
        (catrige := 30) if ammunitions >= 30 else (catrige := ammunitions)
        for j in range(1, catrige + 1):
            q.put(j)
            ammunitions -= 1
        p = Process(target=soldier, args=(q,))

        print(f'\nКурсант {i} начал снаряжать магазин')
        p.start()
        p.join()
        print(f'\nКурсант {i} закончил снаряжать магазин')

