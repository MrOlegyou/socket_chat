from _thread import *
import threading
import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()

def start_new_connection(conn, addr):
    thread1 = threading.Thread(target=send_message)
    thread2 = threading.Thread(target=receive_message, args=(conn, addr))

    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

def receive_message(conn, addr):
    while True:
        try:
            data = conn.recv(1024).decode()
        except:
            print("Пользователь {0}:{1} отсоединился!".format(addr[0], addr[1]))
            break
        print("Пользователь {0}:{1} пишет: {2}".format(addr[0], addr[1], data))

def send_message():
    while True:
        message_text = input("Введите сообщение сервера: ")
        for conn in clients_list:
            conn.send(message_text.encode())

clients_list = []

print("Сервер запущен!")

while True:
    conn, addr = sock.accept()
    clients_list.append(conn)
    print("Пользователь {0}:{1} присоединился к чату!".format(addr[0], addr[1]))
    start_new_thread(start_new_connection, (conn, addr))

conn.close()