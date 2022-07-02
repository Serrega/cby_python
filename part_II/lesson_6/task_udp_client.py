import socket
import sys


udp_port = 2323
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', udp_port))

while True:
    data = s.sendto(input('Введите сообщение: ').encode(), ('', udp_port))
    if not data:
        sys.exit()

