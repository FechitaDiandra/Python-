import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 1234))

print("Conectat la server! Scrie Rock, Paper, Scissors, Lizard sau Spock pentru a juca.")

while True:
   
    optiune = input("Alege opțiunea ta: ").capitalize()
    if optiune not in ["Rock", "Paper", "Scissors", "Lizard", "Spock"]:
        print("Opțiune invalidă. Alege din: Rock, Paper, Scissors, Lizard sau Spock.")
        continue

    
    client.send(optiune.encode("utf-8"))

   
    raspuns = client.recv(1024).decode("utf-8")
    print(raspuns)

    
    if "Game over!" in raspuns:
        break

client.close()
print("Conexiunea cu serverul s-a închis.")