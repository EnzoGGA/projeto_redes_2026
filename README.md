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

Para a execução, siga os passos:

## Iniciar servidores

```bash
cd server
python database.py #cria o banco de dados
python server/tcp_server.py #inicia o servidor tcp
python server/udp_server.py #inicia o servidor udp
uvicorn api:app --host 0.0.0.0 --port 8000 --reload #inicia a API
```
Para iniciar o streamlit:
```bash
cd dashboard
streamlit run app.py #inicia o streamlit
```

## Iniciar clientes

```bash
cd client
python tcp_client.py #inicia o cliente tcp
python udp_client.py #inicia o cliente udp
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
 
# Vídeo de Demonstração

Clique na imagem abaixo para assistir ao vídeo:
[![Vídeo de demonstração](https://img.youtube.com/vi/SLpvlW2HVP0/0.jpg)](https://youtu.be/SLpvlW2HVP0)

# Disciplina

CIC0124 — Redes de Computadores
Universidade de Brasília (UnB)
