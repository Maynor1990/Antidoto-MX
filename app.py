import streamlit as st
import pandas as pd
import time
from annotated_text import annotated_text

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    .stMetric, .stTabs, .log-container {
        background-color: #0d1117; border: 1px solid #30363d;
        border-radius: 4px; padding: 15px;
    }
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 20px #58a6ff;
        font-weight: 900; letter-spacing: 5px; text-transform: uppercase;
    }
    /* Estilos del Radar */
    .radar-box {
        width: 100%; height: 420px; background-color: #000;
        border: 1px solid #30363d; border-radius: 4px;
        position: relative; overflow: hidden;
        display: flex; justify-content: center; align-items: center;
    }
    .radar-circle {
        position: absolute; border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 50%;
    }
    .scanner-line {
        position: absolute; width: 50%; height: 50%;
        top: 50%; left: 50%;
        background: conic-gradient(from 0deg, rgba(0, 212, 255, 0.4) 0%, transparent 30%);
        border-radius: 50%;
        transform-origin: top left;
        animation: rotate 4s linear infinite;
    }
    .threat-point {
        position: absolute; width: 10px; height: 10px;
        background-color: #ff0000; border-radius: 50%;
        box-shadow: 0 0 12px #ff0000; animation: pulse 2s infinite;
        z-index: 5;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
    
    div.stButton > button {
        background: linear-gradient(180deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold; width: 100%; height: 45px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO
st.markdown("<h1 class='glow-header'>🛡️ Antídoto MX | Tactical Hub</h1>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Fiabilidad", "99.8%", "ÓPTIMO")
m2.metric("Base de Datos", "+500k IPs", "ACTUALIZADO")
m3.metric("Protección", "Activa 24/7", "SECURE")
m4.metric("Amenazas Hoy", "1,284", "↑ 12")

st.write("---")

# 4. CUERPO (RADAR Y CONSOLA)
col_radar, col_action = st.columns([1.6, 1])

with col_radar:
    st.markdown("📡 **SISTEMA DE RADAR ACTIVO** <span style='float:right; color:#3fb950;'>SCANNING...</span>", unsafe_allow_html=True)
    
    # IMPORTANTE: Todo el HTML del radar en UN SOLO bloque
    st.markdown("""
    <div class="radar-box">
        <div class="radar-circle" style="width: 100px; height: 100px;"></div>
        <div class="radar-circle" style="width: 200px; height: 200px;"></div>
        <div class="radar-circle" style="width: 300px; height: 300px;"></div>
        <div class="radar-circle" style="width: 400px; height: 400px;"></div>
        <div class="scanner-line"></div>
        
        <div class="threat-point" style="top: 25%; left: 65%;"></div>
        <div class="threat-point" style="top: 60%; left: 35%;"></div>
        <div class="threat-point" style="top: 15%; left: 45%;"></div>
        <div class="threat-point" style="top: 75%; left: 70%;"></div>
        
        <div style="position: absolute; bottom: 10px; color: #00d4ff; font-size: 0.7rem; font-weight: bold; z-index: 10;">
            RANGO DE ESCANEO: 500KM | NODO: CDMX
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_action:
    st.markdown("🛠️ **CONSOLA DE ACCIÓN**")
    t1, t2 = st.tabs(["🔗 RASTREO URL", "🖼️ FORENSE"])
    with t1:
        st.text_input("URL:", placeholder="https://", label_visibility="collapsed")
    with t2:
        st.file_uploader("Evidencia:", label_visibility="collapsed")
    
    st.button("🚀 INICIAR PROTOCOLO ANTÍDOTO")

    st.write("")
    st.markdown("📟 **LIVE EVENT LOG**")
    st.markdown("""
    <div style="background-color: #000; border: 1px solid #333; padding: 10px; color: #3fb950; font-family: monospace; font-size: 0.8rem; height: 160px; overflow-y: auto;">
        [SYS] Radar de proximidad activo.<br>
        [NET] Nodo CDMX sincronizado.<br>
        [SEC] Cortafuegos: Interceptando...<br>
        [INF] Escaneo de red al 85%.<br>
        [WRN] Señal sospechosa detectada.<br>
        [SYS] Protocolos listos.
    </div>
    """, unsafe_allow_html=True)

# 5. FOOTER
st.write("---")
f1, f2 = st.columns([1, 1])
with f1:
    annotated_text(("SISTEMA", "PROTEGIDO BY MAYNOR", "#1f6feb"))
with f2:
    st.markdown("<p style='text-align: right; color: #8b949e; font-size: 0.7rem;'>[ID SESIÓN: AMX-992-TX] [BY MAYNOR: Verified Specialist]</p>", unsafe_allow_html=True)
