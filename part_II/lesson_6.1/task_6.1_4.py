import re
import requests
from requests.exceptions import HTTPError


url = 'https://belarusbank.by/api/kursExchange'
param = {'city': 'Минск'}
try:
    response = requests.get(url, params=param)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
else:
    print('Курсы валют в Минске сегодня\n')
    for name, curs in response.json()[0].items():
        if re.match('^(USD|EUR|RUB)_(in|out)', name):
            name += ':'
            print(f'{name: <8}  {float(curs):.2f} руб.')

