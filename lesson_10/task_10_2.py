if __name__ == '__main__':
    kurs = float(input('Enter rub/usd: '))
    usd = float(input('Enter usd: '))
    print('By course %.2f rub/usd you get %.2f rubles' % (kurs, usd * kurs))
    print(
        'By course {:.2f} rub/usd you get {:.2f} rubles'.format(kurs, usd * kurs))
    print(f'By course {kurs:.2f} rub/usd you get {usd*kurs:.2f} rubles')
