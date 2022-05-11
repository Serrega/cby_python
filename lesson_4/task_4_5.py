our = input('input ours: ')
minute = input('input minutes: ')
second = input('input seconds: ')
if 0 <= int(our) <= 23 and 0 <= int(minute) <= 59 and 0 <= int(second) <= 59:
    if int(our) < 10:
        our = '0' + our
    if int(minute) < 10:
        minute = '0' + minute
    if int(second) < 10:
        second = '0' + second
    print(our + ':' + minute + ':' + second)
else:
    print('input numbers for ours from 0 to 23,'
          ' for minutes and seconds from 0 to 59')
