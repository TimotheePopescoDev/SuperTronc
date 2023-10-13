import socket
from _thread import *
from player import Player
import pickle
import time

server = "172.21.72.234"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

# Initialisez les états de jeu
joueurs_prets = {"joueur1": False, "joueur2": False}

players = [Player(50, 450, 10, 10, (255, 255, 255), (255, 0, 0), 500, 500), Player(50, 50, 10, 10, (255, 255, 255), (0, 0, 255), 500, 500)]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    
    while not all([p.ready for p in players]):
        try:
            # Recevoir l'état "prêt" du client
            data = pickle.loads(conn.recv(4096))
            print(f"Reçu de {addr}: {data}")  # Afficher les données reçues
        
            # Mettre à jour l'état du joueur
            players[player].ready = data.ready
            print(f"Statut mis à jour pour le joueur {player}: {data.ready}")  # Afficher le statut mis à jour

            # Vérifier l'état de préparation de tous les joueurs
            if all([p.ready for p in players]):
                conn.sendall(pickle.dumps(True))  # Les deux joueurs sont prêts
                print("Tous les joueurs sont prêts. Envoi de la confirmation.")  # Débogage
                break  # Sortir de la boucle de préparation
            else:
                conn.sendall(pickle.dumps(False))  # Au moins un joueur n'est pas prêt
                print("Tous les joueurs ne sont pas encore prêts. En attente.")  # Débogage

            time.sleep(0.1)
        except Exception as e:  # Capturer l'exception pour la déboguer
            print(f"Une erreur est survenue : {e}")
            break
    
    if players[0].ready and players[1].ready:
        players[0].reset_player(50, 450)  # Réinitialisez le joueur 0 à la position (50, 450)
        players[1].reset_player(50, 50)


    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending: ", reply)

                # Si le joueur a perdu, mettez fin à la partie pour les deux joueurs
                if data.game_over:
                    for p in players:
                        p.game_over = True

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
