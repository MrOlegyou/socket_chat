import socket
import threading

sock = socket.socket()
sock.connect(('localhost', 9090))

def send_message():
    while True:
        message_text = input("Введите сообщение клиента: ")
        if message_text == "stop":
            break
        sock.send(message_text.encode())

def receive_message():
    while True:
        data = sock.recv(1024).decode()
        print(data)

thread1 = threading.Thread(target=send_message)
thread2 = threading.Thread(target=receive_message)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

sock.close()