#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import threading

def receive_messages(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024)
            for client in clients:
                if client == client_socket:
                    client.send(message)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast("{} left the chat!".format(nickname).encode('utf-8'))
            break

def broadcast(message):
    for client in clients:
        client.send(message)

def main():
    server = "tharun"
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server, port))
    server_socket.listen()

    clients = []
    nicknames = []

    def handle_new_client(client_socket, address):
        client_socket.send("sam".encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client_socket)

        print("Nickname is: {}".format(nickname))
        broadcast("{} joined the chat!".format(nickname).encode('utf-8'))
        client_socket.send("Connected to the server!".encode('utf-8'))

        client_socket_thread = threading.Thread(target=receive_messages, args=(client_socket, address))
        client_socket_thread.start()

    print("Server started!")

    while True:
        client_socket, address = server_socket.accept()
        print("Connected with {}".format(address))

        threading.Thread(target=handle_new_client, args=(client_socket, address)).start()

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




