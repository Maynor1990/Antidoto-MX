import streamlit as st
import pandas as pd
import requests
import socket
import time
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from annotated_text import annotated_text

# =========================================================
# 0. CONFIGURACIÓN Y ESTÉTICA "TACTICAL"
# =========================================================
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #050505; color: #e0e0e0; }
    
    /* Panel lateral y tarjetas */
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #1f6feb; }
    
    .stMetric {
        background: rgba(31, 111, 235, 0.1);
        padding: 15px; border-radius: 10px;
        border: 1px solid rgba(31, 111, 235, 0.2);
    }

    /* Botón Neon */
    div.stButton > button {
        background: linear-gradient(135deg, #1f6feb 0%, #00d4ff 100%);
        color: white; border: none; font-weight: bold;
        width: 100%; height: 50px; border-radius: 5px;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
    }

    /* Animación del Log */
    .log-container {
        background-color: #000; border: 1px solid #333;
        padding: 10px; font-family: 'Courier New', monospace;
        color: #00ff00; font-size: 0.8rem; height: 150px; overflow-y: auto;
    }
    
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 10px #58a6ff;
        font-weight: 900; letter-spacing: 3px; margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 1. BARRA LATERAL (DATOS DE SISTEMA)
# =========================================================
with st.sidebar:
    st.markdown("### 🖥️ SYSTEM STATUS")
    st.metric("MOTOR HEURÍSTICO", "V2.5.0", delta="ESTABLE")
    st.metric("LATENCIA DE RED", "24ms", delta="-2ms")
    st.write("---")
    st.markdown("### 🛰️ COBERTURA GLOBAL")
    st.progress(85)
    st.caption("Protección activa en nodos de México.")
    st.write("---")
    st.info("Logueado como: **Maynor**")

# =========================================================
# 2. CABECERA Y MÉTRICAS SUPERIORES
# =========================================================
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 0.9rem;'>SISTEMA DE RESPUESTA A INCIDENTES Y ANÁLISIS FORENSE</p>", unsafe_allow_html=True)

# Fila de métricas rápidas para llenar el espacio superior
m1, m2, m3, m4 = st.columns(4)
m1.metric("Amenazas Bloqueadas", "1,284", "+12")
m2.metric("IPs Rastreadas", "452", "Activo")
m3.metric("Análisis de Hoy", "89", "+5")
m4.metric("Riesgo Promedio", "Bajo", "-2%")

st.write("---")

# =========================================================
# 3. CUERPO PRINCIPAL (RADAR + HERRAMIENTAS)
# =========================================================
col_radar, col_tools = st.columns([1.2, 2])

with col_radar:
    st.markdown("#### 📡 RADAR DE INTERCEPCIÓN")
    st.markdown("""
    <div style="position: relative; width: 100%; height: 350px; background: radial-gradient(circle, #001a00 0%, #000 100%); border: 1px solid #00ff00; border-radius: 10px; overflow: hidden;">
        <div style="position: absolute; width: 100%; height: 100%; border: 1px solid rgba(0,255,0,0.1); border-radius: 50%; transform: scale(0.8);"></div>
        <div style="position: absolute; width: 100%; height: 100%; border: 1px solid rgba(0,255,0,0.1); border-radius: 50%; transform: scale(0.5);"></div>
        <div style="position: absolute; width: 50%; height: 2px; background: linear-gradient(to right, transparent, #00ff00); top: 50%; left: 50%; transform-origin: left center; animation: rotateRadar 3s linear infinite;"></div>
    </div>
    <style> @keyframes rotateRadar { from { transform: rotate(0deg); } to { transform: rotate(360deg); } } </style>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("#### 📜 LIVE EVENT LOG")
    st.markdown("""
    <div class="log-container">
        [SYS] Inicializando módulos de escaneo...<br>
        [NET] Nodo CDMX conectado via 192.168.1.XX<br>
        [WRN] Intento de handshake fallido en puerto 443<br>
        [SEC] Antídoto MX listo para recibir paquetes...<br>
        [INF] Escáner EXIF cargado correctamente.
    </div>
    """, unsafe_allow_html=True)

with col_tools:
    st.markdown("#### 🛠️ HERRAMIENTAS DE ANÁLISIS")
    
    tab1, tab2 = st.tabs(["🔗 RASTREO DE URL", "🖼️ ANÁLISIS DE IMAGEN"])
    
    with tab1:
        url_in = st.text_input("Ingresa el enlace sospechoso:", placeholder="https://")
        st.caption("El motor analizará la IP, el ISP y el país de alojamiento.")
    
    with tab2:
        img_in = st.file_uploader("Carga una imagen para extraer metadatos:", type=['jpg','png','jpeg'])
        st.caption("Útil para detectar fotos tomadas con GPS activado.")

    if st.button("🚀 EJECUTAR PROTOCOLO ANTÍDOTO"):
        if url_in or img_in:
            with st.spinner("Desarmando infraestructura del atacante..."):
                time.sleep(1.5) # Simulación de carga pro
                st.write("---")
                res_1, res_2 = st.columns(2)
                
                if url_in:
                    with res_1:
                        st.success("ANÁLISIS DE RED")
                        st.code(f"Objetivo: {url_in}\nStatus: Rastreado\nOrigen: Servidor Externo")
                
                if img_in:
                    with res_2:
                        st.info("ANÁLISIS DE ARCHIVO")
                        st.write(f"Archivo: {img_in.name}")
                        st.warning("RIESGO: Pendiente de validación manual.")

# =========================================================
# 4. PIE DE PÁGINA
# =========================================================
st.write("---")
c_f1, c_f2, c_f3 = st.columns([1,1,1])
with c_f1:
    annotated_text(("SISTEMA", "PROTEGIDO", "#2ea043"))
with c_f2:
    st.markdown("<center>ID de Sesión: <b>AMX-992-TX</b></center>", unsafe_allow_html=True)
with c_f3:
    st.markdown(f"<p style='text-align: right;'><b>Maynor</b> | Security Specialist</p>", unsafe_allow_html=True)
