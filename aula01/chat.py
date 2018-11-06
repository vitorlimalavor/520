#!/usr/bin/python3
import server_chat
import threading

if __name__ == '__main__':
    user= input('Nickname ')

    f = threading.Thread(target=server_chat.visualizar)
    f.start()
    while f.isAlive:
        mens = input()
        server_chat.cadastrar(user,mens)
        