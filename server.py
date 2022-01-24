import socket
import threading

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

conn, addr = sock.accept()

print(addr, "присоединился")

def receive_message():
    while True:
        data = conn.recv(1024).decode()
        if not data:
            print(addr, "отсоединился")
            break
        print(data)

def send_message():
    while True:
        message_text = input("Введите сообщение сервера: ")
        conn.send(message_text.encode())

thread1 = threading.Thread(target=send_message)
thread2 = threading.Thread(target=receive_message)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

conn.close()