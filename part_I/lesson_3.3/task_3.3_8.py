# ip_adress - tuple of ip adress
ip_adress = '192.168.1.1', '10.10.1.5', '8.8.8.8', '8.8.4.4'

# response is a dict where key is port and value is tuple of services
response = {'22': ('ssh', 'OpenSSH 7.6')}
response['25'] = ('smtp', 'Postfix smtpd')
response['80'] = ('http', 'Ngnix 1.14.0')
print(response)

# pass is a list for simple adding new values
passwd = ['123456', 'Password', '12345', '123456789', 'password1']

