from colorama import Fore
import requests
from requests.exceptions import HTTPError


def print_status(url, status):
    end = {2: f'{Fore.GREEN}%s Success!',
           3: f'{Fore.GREEN}%s Success!',
           4: f'{Fore.RED}%s Not Found!',
           5: f'{Fore.RED}%s Server Error'}
    print(f'{url} {end[status//100]}{Fore.RESET}'%status)


urls = ('https://codeby.net/forums/',
        'https://geekprank.com/hacker/typer/',
        'https://bowandtie.ru/muzhskie-shlyapyi',
        'https://xakep.ru/',
        'https://sdelaicomp.ru/wi-fi/oshibka')
for url in urls:
    try:
        response = requests.get(url)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        status = response.status_code
        print_status(url, status)


