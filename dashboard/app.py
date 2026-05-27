import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Dashboard de Redes",
    layout="wide"
)
st.title("Dashboard de Redes")
st_autorefresh(interval=2000, key="dados")
try:

    response = requests.get(
        "http://127.0.0.1:8000/dados",
        timeout=5
    )
    dados = response.json()
    df = pd.DataFrame(
        dados,
        columns=[
            "device",
            "cpu",
            "ram",
            "timestamp",
            "protocolo",
            "rtt",
            "throughput",
            "ip"
        ]
    )

    if df.empty:
        st.warning("Nenhum dado recebido ainda.")
    else:
        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            unit="s"
        )
        df["rtt"] = pd.to_numeric(
            df["rtt"],
            errors="coerce"
        )
        df["throughput"] = pd.to_numeric(
            df["throughput"],
            errors="coerce"
        )
        # ===== KPIs =====
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(
            "Pacotes",
            len(df)
        )
        col2.metric(
            "Clientes",
            df["device"].nunique()
        )
        col3.metric(
            "RTT Médio TCP",
            f"{df[df['protocolo'] == 'TCP']['rtt'].mean():.2f} ms"
            if not df[df["protocolo"] == "TCP"].empty
            else "N/A"
        )
        col4.metric(
            "Throughput Médio",
            f"{df['throughput'].mean():.2f}"
        )
        st.subheader("Dados Recebidos")
        st.dataframe(
            df,
            use_container_width=True
        )
        st.subheader("Uso de CPU")
        st.line_chart(
            df.set_index("timestamp")["cpu"]
        )
        st.subheader("Uso de RAM")
        st.line_chart(
            df.set_index("timestamp")["ram"]
        )
        tcp_df = df[df["protocolo"] == "TCP"]
        if not tcp_df.empty:
            st.subheader("RTT TCP")
            st.line_chart(
                tcp_df.set_index("timestamp")["rtt"]
            )
        st.subheader("Throughput Médio por Protocolo")
        throughput = (
            df.groupby("protocolo")["throughput"]
            .mean()
        )
        st.bar_chart(throughput)
        st.subheader("Quantidade de Pacotes")
        pacotes = df.groupby("protocolo").size()
        st.bar_chart(pacotes)
        st.subheader("Distribuição por Protocolo")
        st.write(
            df["protocolo"].value_counts()
        )
        st.subheader("IPs conectados")
        st.write(
            df["ip"].unique()
        )
except Exception as e:
    st.error(str(e))