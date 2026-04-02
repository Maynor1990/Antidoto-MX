import streamlit as st
import pandas as pd
import time
from datetime import datetime
from annotated_text import annotated_text

# =========================================================
# 0. CONFIGURACIÓN Y ESTÉTICA HUD (IDENTICO A IMAGEN 3)
# =========================================================
st.set_page_config(page_title="Antídoto MX | Tactical HUD", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Contenedores Estilo HUD */
    .stMetric { background-color: #161b22; border: 1px solid #30363d; border-radius: 4px; padding: 10px; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #161b22; border: 1px solid #30363d; border-radius: 4px 4px 0 0; padding: 10px 20px;
    }

    /* Botón Táctico */
    div.stButton > button {
        background-color: #1f6feb; color: white; border: none; font-weight: bold;
        width: 100%; border-radius: 4px; height: 45px;
    }

    /* Mapa HUD */
    .map-box {
        width: 100%; height: 280px; background-color: #000;
        border: 1px solid #30363d; border-radius: 4px; position: relative;
        background-image: radial-gradient(circle at center, #112211 0%, #000 100%);
    }
    
    .threat-dot {
        position: absolute; width: 8px; height: 8px;
        background-color: #ff0000; border-radius: 50%;
        box-shadow: 0 0 10px #ff0000; animation: blink 1.5s infinite;
    }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

    /* Log y Tablas */
    .log-box {
        background-color: #000; border: 1px solid #30363d;
        padding: 10px; color: #3fb950; font-family: monospace; font-size: 0.8rem;
        height: 120px; overflow-y: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 1. ENCABEZADO Y MÉTRICAS (FILA SUPERIOR)
# =========================================================
st.markdown("<h2 style='text-align: center; color: #58a6ff;'>🛡️ ANTÍDOTO MX | TACTICAL HUB</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-top: -15px;'>SISTEMA DE RESPUESTA TÁCTICA Y ANÁLISIS FORENSE</p>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Amenazas Bloqueadas", "1,284", "↑ 12")
m2.metric("IPs Rastreadas", "452", "Activo")
m3.metric("Uptime del Motor", "99.9%", "Estable")
m4.metric("Nivel de Riesgo", "Medio", "Rastreado")

st.write("---")

# =========================================================
# 2. CUERPO PRINCIPAL (LAYOUT 2 COLUMNAS)
# =========================================================
col_mapa, col_control = st.columns([1.8, 1])

with col_mapa:
    st.markdown("🌐 **WORLD THREAT MAP**")
    st.markdown("""
    <div class="map-box">
        <div class="threat-dot" style="top: 20%; left: 70%;"></div>
        <div class="threat-dot" style="top: 45%; left: 25%;"></div>
        <div class="threat-dot" style="top: 60%; left: 85%;"></div>
        <div class="threat-dot" style="top: 75%; left: 55%;"></div>
        <p style="position: absolute; bottom: 5px; right: 10px; color: #3fb950; font-size: 0.7rem;">ESTADO DEL SISTEMA: OK</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("🚦 **SERVICIOS CRÍTICOS BAJO ATAQUE (MÉXICO)**")
    servicios = {
        "Servicio": ["Portal CFE (Phishing)", "SAT (Inyección SQL)", "Servidor Nómina MX", "SPEI (DDoS)"],
        "País": ["Rusia", "EE.UU.", "China", "Rumania"],
        "IP": ["190.115.x.x", "199.79.62.x", "120.55.x.x", "109.166.x.x"],
        "Estado": ["🔴 CRÍTICO", "🟡 ADVERTENCIA", "🟢 BLOQUEADO", "🔵 MONITOREO"]
    }
    st.table(pd.DataFrame(servicios))

with col_control:
    st.markdown("🔍 **CONSOLA DE ACCIÓN**")
    t1, t2 = st.tabs(["🔗 VERIFICAR LINK", "🖼️ IMÁGENES FORENSES"])
    
    with t1:
        st.text_input("Ingresa URL:", placeholder="https://", label_visibility="collapsed")
    with t2:
        st.file_uploader("Subir imagen:", type=['jpg','png','jpeg'], label_visibility="collapsed")
        
    if st.button("⚡ INICIAR ANÁLISIS SEGURO"):
        with st.spinner("Analizando..."):
            time.sleep(1)
            st.toast("Escaneo completado")

    st.write("")
    st.markdown("📟 **LIVE EVENT LOG**")
    st.markdown("""
    <div class="log-box">
        [SYS] Inicializando módulos...<br>
        [NET] Nodo CDMX conectado (192.168.1.XX)<br>
        [NET] Escaneando puerto 443...<br>
        [SEC] Protocolo EXIF activo.<br>
        [WRN] Intento de handshake fallido.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 3. FOOTER
# =========================================================
st.write("---")
f1, f2 = st.columns([1, 1])
with f1:
    annotated_text(("SISTEMA", "PROTEGIDO BY MAYNOR", "#238636"))
with f2:
    st.markdown("<p style='text-align: right; color: #8b949e; font-size: 0.8rem;'>[ID SESIÓN: AMX-992-TX] [BY MAYNOR: Verified Specialist]</p>", unsafe_allow_html=True)True)
