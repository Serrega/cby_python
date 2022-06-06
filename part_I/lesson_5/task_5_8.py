#for word in (text := input('Input str: ')).split(' '):
#    print(word[::-1], end=' ')

print(' '.join([n[::-1] for n in input('Input str: ').split()]))

print(' '.join([''.join(reversed(n)) for n in input('Input str: ').split()]))

