import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8080))

    print("conectat la server! scrie rock, paper, scissors, lizard sau spock pentru a juca.")

    mesaj_initial = client.recv(1024).decode("utf-8")
    print(mesaj_initial)

    if "Serverul este plin" in mesaj_initial:
        client.close()
        exit()

    while True:
        optiune = input("alege optiunea ta: ").lower()
        if optiune not in ["rock", "paper", "scissors", "lizard", "spock"]:
            print("optiune invalida. alege din: rock, paper, scissors, lizard sau spock.")
            continue

        client.send(optiune.encode("utf-8"))

        raspuns = client.recv(1024).decode("utf-8")
        print(raspuns)

        if "game over!" in raspuns.lower():
            break

except ConnectionRefusedError:
    print("serverul a refuzat conexiunea. incearca mai tarziu.")
except Exception as e:
    print(f"eroare la client: {e}")
finally:
    try:
        client.close()
    except NameError:
        pass
    print("conexiunea cu serverul s-a inchis.")
