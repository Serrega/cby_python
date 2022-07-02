import socket


s = socket.socket()
print('Жду подключения...')
s.bind(('0.0.0.0', 4444))
s.listen(1)
conn, addr = s.accept()
try:
    print('Соединение установлено:', addr)
    while True:
        client_mes = conn.recv(1024).decode()
        if not client_mes:
            break
        print('Клиент:', client_mes)
        if client_mes == 'exit':
            break
        conn.send(input('Сервер: ').encode())
    print('Соединение закрыто.')
except Exception as e:
    print('Ошибка: ', e)
finally:
    conn.close()
