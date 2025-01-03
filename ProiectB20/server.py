import socket
import threading
import random

def verifica_castigator(opt_jucator, opt_server):
    reguli = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    if opt_jucator == opt_server:
        return "draw"
    elif opt_server in reguli[opt_jucator]:
        return "win"
    else:
        return "lose"


def optiune_random():
    return random.choice(["rock", "paper", "scissors", "lizard", "spock"])


def gestioneaza_client(client_socket, adresa, id_jucator):
    print(f"Jucător {id_jucator} conectat de la {adresa}")
    while True:
        try:
       
            opt_jucator = client_socket.recv(1024).decode("utf-8")
            if not opt_jucator:
                break

            if opt_jucator not in ["rock", "paper", "scissors", "lizard", "spock"]:
                client_socket.send("Invalid option. Choose from: rock, paper, scissors, lizard, spock".encode("utf-8"))
                continue

            opt_server = optiune_random()
            rezultat = verifica_castigator(opt_jucator, opt_server)

            mesaj = f"Player {id_jucator}: You chose {opt_jucator}, server chose {opt_server}. Result: {rezultat}"
            client_socket.send(mesaj.encode("utf-8"))

            if rezultat == "lose":
                print(f"Jucător {id_jucator} a pierdut.")
                break

        except Exception as e:
            print(f"Eroare cu jucător {id_jucator}: {e}")
            break

    client_socket.close()
    print(f"Conexiunea cu jucător {id_jucator} s-a închis.")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 1234))
server.listen(3)
print("Serverul a pornit și ascultă conexiuni...")


id_jucator = 0
while True:
    if threading.active_count() - 1 < 3: 
        client_socket, adresa = server.accept()
        id_jucator += 1
        thread = threading.Thread(target=gestioneaza_client, args=(client_socket, adresa, id_jucator))
        thread.start()
