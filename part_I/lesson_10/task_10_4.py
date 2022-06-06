import math


if __name__ == '__main__':
    first_year = 15625
    years = 1 + math.log2(1e6 / first_year)
    print(
        f'You need {years} years to earn 1,000,000$ with {first_year}$ '
        f'in the first year')

    need_first_year = 1e6 / 2**9
    print(
        f'You need to ern {need_first_year:.2f}$ in the first year to become '
        f'a millionaire in 10 years ')


