import socket
import _thread

ADRESSE = '0.0.0.0'
PORT = 4444

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((ADRESSE, PORT))
serveur.listen(1)
client, adresseClient = serveur.accept()
print('Connexion de ', adresseClient)


def handle_client(client):
    while True:
        data = client.recv(1024)
        if not data:
            print('Erreur de reception. Aucune donnée reçu')
            serveur.close()
            break
        if data == b'exit\n':
            break
        print(data)
    serveur.close()


_thread.start_new_thread(handle_client, (client,))
while True:
    try :
        data_to_send = input("Entrez ce que vous voulez envoyer ...\n")
        data_to_send = data_to_send + "\0"
        #data_to_send =bytes(data_to_send, 'utf-8')
        data_to_send = data_to_send.encode('utf-8')
        print(data_to_send)
        client.send(data_to_send)
    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur")
        serveur.close()
        break