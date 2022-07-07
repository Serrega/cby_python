from colorama import Fore
import requests
from requests.exceptions import HTTPError


urls = ('https://www.rk-ny.org/whatsnew.php?id=1',
       'https://www.genecards.org/cgi-bin/carddisp.pl?gene=ID1',
       'http://www.meggieschneider.com/php/detail.php?id=1',
       'https://kodamo.org/product.php?id=1')

for url in urls:
    try:
        res = requests.get(url + "'")
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        inj = 'Vulnerable!'
        if 'SQL' not in res.text:
            inj = f'{Fore.RED}Not ' + inj
        print(f"{url}' ===> {Fore.GREEN}{inj}{Fore.RESET}")

