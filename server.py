#!/bin/python3

"""
 Description            : TCP listener with handling of clients and xor encryption
 Author                 : ESGI - 4SI2 - Groupe 4 : Tristan KLIEBER ; Quentin CHARLES ; Nicolas TAHON
 Date                   : june 2022
"""

import socket
import _thread

ADRESSE = '0.0.0.0'
PORT = 4444

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((ADRESSE, PORT))
serveur.listen(1)
print("Listening for a new TCP connection ...")
client, adresseClient = serveur.accept()
print('Connexion reçu de ', adresseClient)


"""def xored(data):
    data = data + "\0"
    xor = "ff"
    data = chr(ord(data) ^ ord(xor))
    return data"""


def handle_client(client):
    i = 0
    while i == 0:
        data = client.recv(1024)
        if not data:
            print('Erreur de reception. Aucune donnée reçu.\nFermeture du serveur...')
            serveur.close()
            exit(1)
            i = 1
            break
        if data == b'exit\n':
            serveur.close()
            exit(1)
            i = 1
            break
        print(data)
    serveur.close()


_thread.start_new_thread(handle_client, (client,))
while True:
    try:
        data_to_send = input("> ")
        if data_to_send == "exit":
            serveur.close()
            break
        else:
            """xorkey = 'F'
            data_to_send = ord(data_to_send)
            for i in range(len(data_to_send)):
                data_to_send = (data_to_send[:i]
                                + chr(data_to_send[i] ^ ord(xorkey))
                                + data_to_send[i + 1:])
            print(data_to_send)"""
            # data_to_send = xored(data_to_send)
            # print("xored data : ", data_to_send)
            data_to_send += "\0"
            client.send(data_to_send.encode('utf-8'))
    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur\nServer closed...\n")
        serveur.close()
        break
