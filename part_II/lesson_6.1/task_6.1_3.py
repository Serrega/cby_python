from ftplib import FTP
import requests
from requests.exceptions import HTTPError


def write_file(file, res):
    with open(file, 'wb') as file_wb:
        for i in res.iter_content():
            file_wb.write(i)


def save_ftp(file):
    ftp = FTP('localhost')
    ftp.login('ftpuser', 'gurri')
    ftp.cwd('files')

    try:
        with open(file, 'rb') as fp:
            ftp.storlines('STOR hosts.txt', fp)
    except Exception as e:
        print('Error', e)
    ftp.quit()


img = 'https://i.ytimg.com/vi/VKErEwtJ-Nw/maxresdefault.jpg'
filename = 'winner.jpg'
try:
    response = requests.get(img, stream=True)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
else:
    write_file(filename, response)
    save_ftp(filename)
    print('Файл скачан и загружен на FTP-сервер')
