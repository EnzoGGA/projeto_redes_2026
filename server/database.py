from pathlib import Path
import sqlite3

def get_connection():
    conn = sqlite3.connect(banco)
    return conn


def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device TEXT,
        cpu INTEGER,
        ram INTEGER,
        timestamp REAL,
        protocolo TEXT,
        rtt REAL,
        throughput REAL,
        ip TEXT
    )
    """)
    conn.commit()
    conn.close()

diretorio = Path(__file__).resolve().parent.parent
data = diretorio / "data"
data.mkdir(exist_ok=True)
banco = data / "monitoramento.db"
criar_tabela()