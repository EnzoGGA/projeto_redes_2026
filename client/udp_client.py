import socket
import json
import random
import time

HOST = '127.0.0.1' #mude o ip para o do servidor se não estiver rodando localmente
PORT = 5001
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
seq = 0
while True:
    seq += 1
    payload = {
        "seq": seq,
        "device": "enzo-pc",
        "cpu": random.randint(0, 100),
        "ram": random.randint(0, 100),
        "timestamp": time.time()
    }
    data = json.dumps(payload).encode()
    client.sendto(data, (HOST, PORT))
    print(f"Pacote UDP enviado | seq={seq}")
    time.sleep(2)