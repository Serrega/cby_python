from colorama import Fore


colors = {'#': Fore.GREEN}
with open('example.py', 'rb') as f:
    c = f.readlines()
for line in c[1:-1]:
    for x in line[:-1].decode("utf-8"):
        print(colors.get(x, '') + x + Fore.RESET, end='')
    print()


