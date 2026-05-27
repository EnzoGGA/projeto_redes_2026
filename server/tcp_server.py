import socket
import json
import time
import threading
from database import get_connection

def salvar_log(texto):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(texto + "\n")


def handle_client(client_socket, addr):
    try:
        inicio = time.time()
        data = client_socket.recv(1024)
        if data:
            payload = json.loads(data.decode())
            fim = time.time()
            rtt = (fim - inicio) * 1000
            throughput = len(data)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO dados(
                device,
                cpu,
                ram,
                timestamp,
                protocolo,
                rtt,
                throughput,
                ip
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                payload["device"],
                payload["cpu"],
                payload["ram"],
                payload["timestamp"],
                "TCP",
                rtt,
                throughput,
                addr[0]
            ))
            conn.commit()
            conn.close()
            client_socket.send(b"ACK")
            log = f"TCP | {addr[0]} | RTT={rtt:.2f}ms"
            print(log)
            salvar_log(log)

    except Exception as e:
        print("ERRO TCP:", repr(e))

    finally:
        client_socket.close()

HOST = '0.0.0.0' #aceita conexões de qualquer IP
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
print(f"Servidor TCP ouvindo em {PORT}")

while True:

    client_socket, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, addr)
    )

    thread.start()