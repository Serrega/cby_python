import requests
from requests.exceptions import HTTPError


url = 'https://example.com/'
try:
    response = requests.get(url)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
else:
    for key,val in response.headers.items():
        print(f'{key}:{val}')

