import socket
import threading
from random import randint

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

numar_clienti = 0
lock = threading.Lock()  

def verifica_castigator(player, computer):
    if player == computer:
        return "Tie!", None
    elif player == "Rock":
        if computer in ["Paper", "Spock"]:
            return "You lose!", False
        else:
            return "You win!", True
    elif player == "Paper":
        if computer in ["Scissors", "Lizard"]:
            return "You lose!", False
        else:
            return "You win!", True
    elif player == "Scissors":
        if computer in ["Rock", "Spock"]:
            return "You lose!", False
        else:
            return "You win!", True
    elif player == "Lizard":
        if computer in ["Rock", "Scissors"]:
            return "You lose!", False
        else:
            return "You win!", True
    elif player == "Spock":
        if computer in ["Paper", "Lizard"]:
            return "You lose!", False
        else:
            return "You win!", True
    else:
        return "Invalid play!", None

def gestioneaza_client(client_socket, adresa):
    global numar_clienti
    with lock:
        numar_clienti += 1
    print(f"Client conectat de la {adresa}. Numar clienti activi: {numar_clienti}")

    scor_jucator = 0
    scor_server = 0

    while scor_jucator < 2 and scor_server < 2:
        try:
            player = client_socket.recv(1024).decode("utf-8").capitalize()
            if not player:
                break

            if player not in options:
                client_socket.send("Invalid option. Try again.".encode("utf-8"))
                continue

            computer = options[randint(0, 4)]
            print(f"Jucătorul a ales: {player}, Serverul a ales: {computer}")

            rezultat, castigator = verifica_castigator(player, computer)
            if castigator is True:
                scor_jucator += 1
            elif castigator is False:
                scor_server += 1

            mesaj = f"{rezultat} (Player: {scor_jucator}, Server: {scor_server})"
            client_socket.send(mesaj.encode("utf-8"))
        except Exception as e:
            print(f"Eroare cu clientul {adresa}: {e}")
            break

    if scor_jucator == 2:
        client_socket.send("Game over! You win the match!".encode("utf-8"))
    else:
        client_socket.send("Game over! You lose the match!".encode("utf-8"))

    client_socket.close()
    with lock:
        numar_clienti -= 1
    print(f"Conexiunea cu clientul {adresa} s-a închis. Numar clienti activi: {numar_clienti}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(3)
print("Serverul a pornit și ascultă conexiuni...")

while True:
    client_socket, adresa = server.accept()
    with lock:
        if numar_clienti >= 3:
            print("Numar maxim de clienti atins. Refuzam conexiunea noua.")
            client_socket.send("Serverul este plin. Incearca mai tarziu.".encode("utf-8"))
            client_socket.close()
            print(f"Client de la {adresa} a fost refuzat deoarece serverul este plin.")
            continue

    thread = threading.Thread(target=gestioneaza_client, args=(client_socket, adresa))
    thread.start()
