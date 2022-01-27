from socket import socket
from threading import Thread

class Client():

    def __init__(self):
        self.sock = socket()
        self.SERVER_IP = 'localhost'
        self.SERVER_PORT = 9090


    def send_message(self):
        while True:
            message_text = input("Введите сообщение клиента: ")
            self.sock.send(message_text.encode())


    def receive_message(self):
        while True:
            try:
                data = self.sock.recv(1024).decode()
            except:
                print("Сервер отсоединился!")
                break        
            print(data)


    def start_client(self): 
        self.sock.connect((self.SERVER_IP, self.SERVER_PORT))

        thread1 = Thread(target=self.receive_message)
        thread2 = Thread(target=self.send_message)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        self.sock.close()