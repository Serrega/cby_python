def check_input(text: str, max_lenght, min_lenght=1, ret_non_diap=0) -> int:
    '''
    :param text: входящая строка
    :param max_lenght: значение диапазона справа
    :param min_lenght: значение диапазона слева
    :param ret_non_diap: флаг, возврашать ли число не из диапазона
    :return: -1 прерывание или EOF, число при удаче, False при ошибке
    '''
    try:
        num = int(input(text))
    except ValueError as ve:
        print('\nYou must enter number, not string - ', ve.args)
    except(EOFError, KeyboardInterrupt) as eo:
        print('\nEOF or Interrupt - ', eo.args)
        return -1
    except BaseException as be:
        # for Ctrl+C in PyCharm in Windows
        print('\nBaseException - ', be.args)
        return -1
    else:
        if min_lenght <= num <= max_lenght:
            return num
        print(f'\nYou must enter a number from {min_lenght} to {max_lenght}:')
        if ret_non_diap:
            return num
    return False
