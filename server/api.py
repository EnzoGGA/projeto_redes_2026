from fastapi import FastAPI
from database import get_connection
app = FastAPI()


@app.get("/")
def home():
    return {"status": "online"}


@app.get("/dados")
def dados():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
        device,
        cpu,
        ram,
        timestamp,
        protocolo,
        rtt,
        throughput,
        ip
    FROM dados
    ORDER BY id DESC
    LIMIT 500
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows