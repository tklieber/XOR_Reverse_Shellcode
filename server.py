#!/bin/python3

"""
 Description            : TCP listener with handling of clients and xor encryption
 Author                 : ESGI - 4SI2 - Groupe 4 : Tristan KLIEBER ; Quentin CHARLES ; Nicolas TAHON
 Date                   : june 2022
"""

import socket
import _thread

ADRESSE = '0.0.0.0'
PORT = 1337

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((ADRESSE, PORT))
serveur.listen(1)
print("Listening for a new TCP connection ...")
client, adresseClient = serveur.accept()
print('Connexion reçu de ', adresseClient)


def callexit():
    exit(1)


def xored(data):
    data = data + "\0"
    xorkey = "5" * len(data)
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(data, xorkey)])


def handle_client(client):
    i = 0
    while i == 0:
        data = client.recv(1024)
        if not data:
            print('Erreur de reception. Aucune donnée reçu.\nFermeture du serveur...')
            serveur.close()
            callexit()
            i = 1
            break
        if data == b'exit\n':
            serveur.close()
            callexit()
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
            data_to_send = xored(data_to_send)
            print("xored data sent : ", data_to_send)
            xored_string = data_to_send
            xor_key = "555"
            print("un-xored data : ", ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(xored_string, xor_key)]))
            client.send(data_to_send.encode('utf-8'))
    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur\nServer closed...\n")
        serveur.close()
        callexit()
        break
