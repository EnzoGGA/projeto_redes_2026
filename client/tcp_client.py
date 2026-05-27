import socket
import json
import random
import time

HOST = '127.0.0.1'
PORT = 5000
while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    payload = {
        "device": "enzo-pc",
        "cpu": random.randint(0, 100),
        "ram": random.randint(0, 100),
        "timestamp": time.time()
    }
    inicio = time.time()
    client.send(json.dumps(payload).encode())
    ack = client.recv(1024)
    fim = time.time()
    rtt = (fim - inicio) * 1000
    print("ACK:", ack.decode())
    print(f"RTT Cliente TCP: {rtt:.2f} ms")
    client.close()
    time.sleep(2)