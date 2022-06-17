#!/bin/python3

"""
 Description            : TCP listener with handling of clients and xor encryption
 Author                 : ESGI - 4SI2 - Groupe 4 : Tristan KLIEBER ; Quentin CHARLES ; Nicolas TAHON
 Date                   : june 2022
"""

import _thread
import os
import socket

ADRESSE = '0.0.0.0'
PORT = 1337

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((ADRESSE, PORT))
serveur.listen(1)
print("Listening for a new TCP connection ...")
client, adresseClient = serveur.accept()
print('Connexion reçu de ', adresseClient)


def callexit():
    _thread.interrupt_main()
    os._exit(1)


def xored(data):
    data = data + "\0"
    xorkey = "5" * len(data)
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(data, xorkey)])


def handle_client(client):
    while True:
        data = client.recv(1024)
        if not data:
            print('\nReception error. No data received.\nClosing server...')
            serveur.close()
            callexit()
        if data == b'exit\n':
            serveur.close()
            callexit()
        elif data == b'frkerror':
            print("Child process failed on creation\nPlease enter the message again")
        print(data)


if __name__ == "__main__":
    _thread.start_new_thread(handle_client, (client,))
    while True:
        try:
            data_to_send = input("> ")
            if data_to_send == "exit":
                serveur.close()
                try:
                    callexit()
                except KeyboardInterrupt:
                    print("Closing server...")
                break
            else:
                data_to_send = xored(data_to_send)
                print("xored data sent : ", data_to_send)
                client.send(data_to_send.encode('utf-8'))
        except KeyboardInterrupt:
            print("\nProgramme interrompu par l'utilisateur\nServer closed...\n")
            serveur.close()
            callexit()
            break
