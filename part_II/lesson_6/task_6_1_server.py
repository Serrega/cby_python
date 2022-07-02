import socket


s = socket.socket()
print('Жду подключения...')
s.bind(('0.0.0.0', 4444))
s.listen(1)
conn, addr = s.accept()
try:
    print('Соединение установлено:', addr)

    client_mes = conn.recv(1024).decode()

    print('Клиент:', client_mes)
    print('Соединение закрыто.')
except Exception as e:
    print('Ошибка: ', e)
finally:
    conn.close()
