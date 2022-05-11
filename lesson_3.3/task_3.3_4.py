creds = ('__init__', '127.0.0.1', 'admin', 'SupermAn', 'ClOwN',
         'http://site.com', 'humorist', 'https://example.com',
         '192.168.12.101', 12345, 'https://yandex.ru')
print('Login:', creds[2], creds[6], sep='\n')
print('\nPassword:', creds[3], creds[4], sep='\n')
print('\nIP:', creds[1], creds[8], sep='\n')
print('\nHost:', creds[5], creds[7], sep='\n')

"""
print('Login:')
for login in creds:
    if str(login).islower() and str(login).isalpha():
        print(login)
print('\nPassword:')
for passwd in creds:
    if not str(passwd).islower() and str(passwd).isalpha():
        print(passwd)
print('\nIP:')
for ip in creds:
    if '.' in str(ip) and str(ip).replace('.', '').isnumeric():
        print(ip)
print('\nHost:')
for host in creds:
    if str(host).endswith('com'):
        print(host)
"""

