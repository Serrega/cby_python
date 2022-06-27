from colorama import Fore
import threading
import time


def road(auto, sec):
    print(f'Автомобиль {auto} стартовал')
    time.sleep(sec)
    print(f'\nКоличество активных авто ', p := threading.activeCount())
    print(f'Автомобиль {Fore.GREEN}{auto}{Fore.RESET} финишировал {7 - p}')
    print(f'{Fore.LIGHTMAGENTA_EX}Доехал до финиша за: '
          f'{time.time() - start:.3f} sec{Fore.RESET}')


automobile = {'MAZDA': 15, 'HONDA': 18, 'TOYOTA': 19}
start = time.time()
for auto, sec in automobile.items():
    threading.Thread(target=road, args=(auto, sec)).start()

