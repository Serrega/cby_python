import socket


def receive_msg(print_addr=False):
    try:
        msg, addr = sock.recvfrom(1024)
        if print_addr:
            print('Соединение установлено: ', addr)
        print('Клиент UDP:', msg.decode())
        if msg.decode() == 'exit':
            return False
    except Exception as e:
        print('Ошибка: ', e)
        return False
    else:
        return addr


udp_port = 2323
print('Жду подключения...')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', udp_port))

addr = receive_msg(True)

while True:
    data = sock.sendto(input('Сервер UDP: ').encode(), addr)
    if not (addr := receive_msg()):
        break

sock.close()
print('Соединение закрыто.')
