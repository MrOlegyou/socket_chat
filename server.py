from _thread import start_new_thread
from socket import socket
from threading import Thread

class Server():

    def __init__(self):
        self.clients_list = []
        self.sock = socket()
        self.SERVER_IP = ''
        self.SERVER_PORT = 9090


    def start_new_connection(self, conn, addr):
        thread1 = Thread(target=self.receive_message, args=(conn, addr))
        thread2 = Thread(target=self.send_group_message)    

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()


    def receive_message(self, conn, addr):
        while True:
            try:
                data = conn.recv(1024).decode()
            except:
                print("Пользователь {0}:{1} отсоединился!".format(addr[0], addr[1]))
                break
            user_message = "Пользователь {0}:{1} пишет: {2}".format(addr[0], addr[1], data)
            print(user_message)
            self.send_user_message(user_message, conn)


    def send_user_message(self, user_message, conn):
        for client in self.clients_list:
            if client != conn:
                client.send(user_message.encode())


    def send_group_message(self):
        while True:
            server_message = "Сервер пишет: " + input("Введите сообщение сервера: ")
            for conn in self.clients_list:
                conn.send(server_message.encode())


    def start_server(self):
        self.sock.bind((self.SERVER_IP, self.SERVER_PORT))
        self.sock.listen()

        print("Сервер запущен!")

        while True:
            conn, addr = self.sock.accept()
            self.clients_list.append(conn)
            print("Пользователь {0}:{1} присоединился к чату!".format(addr[0], addr[1]))
            start_new_thread(self.start_new_connection, (conn, addr))

        conn.close()