import click


@click.command()
@click.argument('ch')
def main(ch):
    mod = {0: '---', 1: '--x', 2: 'r--', 3: 'r-x', 4: '-w-', 5: '-wx', 6: 'rw-', 7: 'rwx'}
    res = []
    if len(ch) == 3:
        for dig in ch:
          res.append(mod[int(dig)])
    print(f'Калькулятор прав доступа\n{ch} this {"".join(res)}')


if __name__ == '__main__':
    main()
