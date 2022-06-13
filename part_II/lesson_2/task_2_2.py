import click


@click.command()
@click.argument('ch')
def main(ch):
    mod = {0: 'w', 1: 'r', 2: 'x'}
    res = []
    if len(ch) == 3:
        for dig in ch:
            print(dig)
            string = ['-', '-', '-']
            for ind, bdig in enumerate(bin(int(dig))[2:]):
                if int(bdig):
                    string[ind] = mod[ind]
            res.append(''.join(string))
    print(f'Калькулятор прав доступа\n{ch} this {"".join(res)}')


if __name__ == '__main__':
    main()
    