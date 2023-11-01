#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Error receiving messages.")
            break

def send_messages(client_socket, username):
    while True:
        message = input()
        client_socket.send(bytes(username + ": " + message, 'utf-8'))

def main():
    server = "tharun"
    port = 5555

    username = input("Enter your username: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_messages(client_socket, username)

if __name__ == '__main__':
    main()


# In[ ]:




