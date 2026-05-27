import socket
import json
from database import get_connection

HOST = '0.0.0.0' #aceita conexões de qualquer IP
PORT = 5001
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f"Servidor UDP ouvindo em {PORT}")


while True:
    try:
        data, addr = server.recvfrom(1024)
        payload = json.loads(data.decode())
        print("Recebido:", payload)
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
            "UDP",
            None,
            throughput,
            addr[0]
        ))
        conn.commit()
        conn.close()
        print("UDP salvo no banco")
    except Exception as e:
        print("ERRO UDP:", repr(e))