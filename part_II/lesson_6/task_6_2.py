from ftplib import FTP
import socket
from urllib.parse import urlsplit


def save_ftp():
    ftp = FTP('localhost')
    ftp.login('ftpuser', 'gurri')
    ftp.cwd('files')

    try:
        with open('hosts.txt', 'rb') as fp:
            ftp.storlines('STOR hosts.txt', fp)
    except Exception as e:
        print('Error', e)
    ftp.quit()


url = ('https://www.hackthebox.eu/',
       'https://hack.me/',
       'http://www.gameofhacks.com/',
       'http://www.itsecgames.com/')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with open('hosts.txt', 'a') as file_a:
    for host in url:
        host = urlsplit(host).netloc
        remote_ip = socket.gethostbyname(host)
        print(f"ip address of {host} is {remote_ip}")
        file_a.writelines(f'{host} {remote_ip}\n')
save_ftp()
