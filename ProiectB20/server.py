import socket
import threading
from random import randint

options = ["rock", "paper", "scissors", "lizard", "spock"]

def verifica_castigator(player, computer):
    if player == computer:
        return "tie!", None
    elif player == "rock":
        if computer in ["paper", "spock"]:
            return "you lose!", False
        else:
            return "you win!", True
    elif player == "paper":
        if computer in ["scissors", "lizard"]:
            return "you lose!", False
        else:
            return "you win!", True
    elif player == "scissors":
        if computer in ["rock", "spock"]:
            return "you lose!", False
        else:
            return "you win!", True
    elif player == "lizard":
        if computer in ["rock", "scissors"]:
            return "you lose!", False
        else:
            return "you win!", True
    elif player == "spock":
        if computer in ["paper", "lizard"]:
            return "you lose!", False
        else:
            return "you win!", True
    else:
        return "invalid play!", None

def gestioneaza_client(client_socket, adresa):
    print(f"client conectat de la {adresa}")
    scor_jucator = 0
    scor_server = 0

    while scor_jucator < 2 and scor_server < 2: 
        try:
            player = client_socket.recv(1024).decode("utf-8").lower()
            if not player:
                break

            if player not in options:
                client_socket.send("invalid option. choose rock, paper, scissors, lizard, or spock.".encode("utf-8"))
                continue

            computer = options[randint(0, 4)]
            print(f"jucatorul a ales: {player}, serverul a ales: {computer}")

            rezultat, castigator = verifica_castigator(player, computer)
            if castigator is True:
                scor_jucator += 1
            elif castigator is False:
                scor_server += 1

            mesaj = f"{rezultat} (player: {scor_jucator}, server: {scor_server})"
            client_socket.send(mesaj.encode("utf-8"))
        except Exception as e:
            print(f"eroare cu clientul {adresa}: {e}")
            break

    if scor_jucator == 2:
        client_socket.send("game over! you win the match!".encode("utf-8"))
    else:
        client_socket.send("game over! you lose the match!".encode("utf-8"))

    client_socket.close()
    print(f"conexiunea cu clientul {adresa} s-a inchis.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 1234))
server.listen(3)
print("serverul a pornit si asculta conexiuni...")

while True:
    client_socket, adresa = server.accept()
    thread = threading.Thread(target=gestioneaza_client, args=(client_socket, adresa))
    thread.start()