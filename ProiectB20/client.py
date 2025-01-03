# client.py
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 1234))

print("Conectat la server. Introdu una dintre opțiuni: rock, paper, scissors, lizard, spock")
while True:
 
    optiune = input("Alege opțiunea ta: ").strip().lower()
    if optiune not in ["rock", "paper", "scissors", "lizard", "spock"]:
        print("Opțiune invalidă. Alege din: rock, paper, scissors, lizard, spock.")
        continue
    client.send(optiune.encode("utf-8"))

 
    raspuns = client.recv(1024).decode("utf-8")
    print(raspuns)

    if "Result: lose" in raspuns:
        print("Ai pierdut! Jocul s-a încheiat.")
        break

client.close()
print("Conexiunea cu serverul s-a închis.")
