import socket


udp_port = 2323
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', udp_port))
print('Жду сообщение...')
while True:
    msp, addr = sock.recvfrom(1024)
    if not msp:
        break
    print(msg.decode())

sock.close()
