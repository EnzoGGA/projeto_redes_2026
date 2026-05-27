# Sistema Distribuído de Monitoramento de Rede — TCP e UDP

Projeto desenvolvido para a disciplina de Redes de Computadores da Universidade de Brasília (UnB).

O sistema implementa uma plataforma de monitoramento em tempo real utilizando comunicação cliente-servidor com os protocolos TCP e UDP. Os clientes enviam métricas simuladas de CPU e memória RAM para servidores responsáveis pelo processamento e armazenamento dos dados.

A aplicação foi desenvolvida em Python utilizando:

* sockets TCP/UDP;
* FastAPI;
* SQLite;
* Streamlit;
* Wireshark para análise de tráfego.

---

# Funcionalidades

* Comunicação TCP e UDP
* Dashboard em tempo real
* API REST
* Persistência em SQLite
* Medição de RTT
* Cálculo de throughput
* Captura e análise de pacotes com Wireshark
* Comparação prática entre TCP e UDP

---

# Estrutura do Projeto

* `tcp_client.py` → cliente TCP
* `udp_client.py` → cliente UDP
* `tcp_server.py` → servidor TCP
* `udp_server.py` → servidor UDP
* `api.py` → API FastAPI
* `app.py` → dashboard Streamlit
* `database.py` → gerenciamento do banco SQLite

---

# Tecnologias Utilizadas

* Python
* Socket Programming
* FastAPI
* SQLite
* Streamlit
* Pandas
* Wireshark

---

# Execução

## Iniciar servidores

```bash
python tcp_server.py
python udp_server.py
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
streamlit run app.py
```

## Iniciar clientes

```bash
python tcp_client.py
python udp_client.py
```

---

# Análise de Rede

Filtros utilizados no Wireshark:

```text
tcp.port == 5000
udp.port == 5001
```

ou

```text
tcp.port == 5000 or udp.port == 5001
```

---

# Disciplina

CIC0124 — Redes de Computadores
Universidade de Brasília (UnB)
