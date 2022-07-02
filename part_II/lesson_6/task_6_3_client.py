import socket


udp_port = 2323
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('localhost', udp_port))
    print('Соединение установлено!')
except Exception as e:
    print('Ошибка: ', e)
else:
    while True:
        data = s.sendto(p := input('Клиент UDP: ').encode(), ('', udp_port))
        if p.decode() == 'exit':
            break

        msg, addr = s.recvfrom(1024)
        print('Сервер UDP: ', msg.decode())

s.close()
