import socket

s = socket.socket()
try:
    s.connect(('127.0.0.1', 4444))
    print('Соединение установлено!')
    while True:
        client_mes = input('Клиент:')
        s.send(client_mes.encode())
        if client_mes == 'exit':
            break
        server_mes = s.recv(1024).decode()
        print('Сервер:', server_mes)
except Exception as e:
    print('Ошибка: ', e)
finally:
    s.close()
