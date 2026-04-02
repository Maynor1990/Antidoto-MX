import streamlit as st
import pandas as pd
import time
from annotated_text import annotated_text

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS (Radar Animado y Colores Neón)
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Contenedores HUD */
    .stMetric, .stTabs, .log-container {
        background-color: #0d1117; border: 1px solid #30363d;
        border-radius: 4px; padding: 15px;
    }

    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 20px #58a6ff;
        font-weight: 900; letter-spacing: 5px; text-transform: uppercase;
    }

    /* CONTENEDOR DEL RADAR */
    .radar-box {
        width: 100%; height: 450px; background-color: #000;
        border: 1px solid #30363d; border-radius: 4px;
        position: relative; overflow: hidden;
        display: flex; justify-content: center; align-items: center;
    }

    /* CÍRCULOS DEL RADAR */
    .radar-circle {
        position: absolute; border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 50%;
    }
    .c1 { width: 100px; height: 100px; }
    .c2 { width: 200px; height: 200px; }
    .c3 { width: 300px; height: 300px; }
    .c4 { width: 400px; height: 400px; }

    /* LÍNEA GIRATORIA (EL SCANNER) */
    .scanner-line {
        position: absolute; width: 225px; height: 225px;
        top: 50%; left: 50%;
        background: conic-gradient(from 0deg, rgba(0, 212, 255, 0.5) 0%, transparent 25%);
        border-radius: 50%;
        transform-origin: top left;
        animation: rotate 4s linear infinite;
    }

    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* PUNTOS DE AMENAZA EN EL RADAR */
    .threat-point {
        position: absolute; width: 8px; height: 8px;
        background-color: #ff0000; border-radius: 50%;
        box-shadow: 0 0 10px #ff0000;
        animation: pulse 2s infinite;
    }

    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }

    /* BOTÓN TÁCTICO */
    div.stButton > button {
        background: linear-gradient(180deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold;
        width: 100%; height: 45px; border-radius: 4px;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
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

# 4. CUERPO PRINCIPAL (RADAR + CONSOLA)
col_radar, col_action = st.columns([1.5, 1])

with col_radar:
    st.markdown("📡 **SISTEMA DE RADAR ACTIVO** <span style='float:right; color:#3fb950;'>SCANNING...</span>", unsafe_allow_html=True)
    
    # RENDERIZADO DEL RADAR HTML
    st.markdown("""
    <div class="radar-box">
        <div class="radar-circle c1"></div>
        <div class="radar-circle c2"></div>
        <div class="radar-circle c3"></div>
        <div class="radar-circle c4"></div>
        <div class="scanner-line"></div>
        
        <div class="threat-point" style="top: 30%; left: 60%;"></div>
        <div class="threat-point" style="top: 70%; left: 40%;"></div>
        <div class="threat-point" style="top: 20%; left: 25%;"></div>
        <div class="threat-point" style="top: 80%; left: 75%;"></div>
        
        <div style="position: absolute; bottom: 10px; color: #00d4ff; font-size: 0.7rem; font-weight: bold;">RANGO DE ESCANEO: 500KM | NODO: CDMX</div>
    </div>
    """, unsafe_allow_html=True)

with col_action:
    st.markdown("🛠️ **CONSOLA DE ACCIÓN**")
    t1, t2 = st.tabs(["🔗 RASTREO URL", "🖼️ FORENSE"])
    with t1:
        st.text_input("URL:", placeholder="https://", label_visibility="collapsed")
    with t2:
        st.file_uploader("Evidencia:", label_visibility="collapsed")
    
    if st.button("🚀 INICIAR PROTOCOLO ANTÍDOTO"):
        with st.spinner("Analizando vectores..."):
            time.sleep(2)
            st.success("Análisis Finalizado")

    st.write("")
    st.markdown("📟 **LIVE EVENT LOG**")
    st.markdown("""
    <div style="background-color: #000; border: 1px solid #333; padding: 10px; color: #3fb950; font-family: monospace; font-size: 0.8rem; height: 180px; overflow-y: auto;">
        [SYS] Radar de proximidad activo.<br>
        [NET] Nodo CDMX sincronizado.<br>
        [SEC] Cortafuegos: Interceptando...<br>
        [INF] Escaneo de red al 85%.<br>
        [WRN] Señal sospechosa detectada en sector 4.<br>
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
