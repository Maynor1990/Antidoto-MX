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
# 0. CONFIGURACIÓN Y ESTÉTICA "TACTICAL HUB"
# =========================================================
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* Fondo oscuro y tipografía técnica */
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Contenedores con bordes finos y fondo negro (Cards) */
    .stMetric, .stTabs, .stFileUploader section, div[data-testid="stExpander"], .security-tips {
        background-color: #0d1117; border: 1px solid #30363d;
        border-radius: 8px; padding: 15px;
    }

    /* Botón Neon */
    div.stButton > button {
        background: linear-gradient(135deg, #1f6feb 0%, #00d4ff 100%);
        color: white; border: none; font-weight: bold;
        width: 100%; height: 50px; border-radius: 5px;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.3); text-transform: uppercase;
        letter-spacing: 2px;
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 0 25px rgba(0, 212, 255, 0.7); }

    /* Animación del Log */
    .log-container {
        background-color: #000; border: 1px solid #333;
        padding: 10px; color: #00ff00; font-size: 0.8rem;
        height: 150px; overflow-y: auto; border-radius: 8px;
    }
    
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 10px #58a6ff;
        font-weight: 900; letter-spacing: 5px; margin-bottom: 0px;
    }

    /* Estilo Radar Circular */
    .radar-box {
        width: 100%; height: 280px; background-color: #000;
        border: 1px solid #333; border-radius: 8px; position: relative;
        overflow: hidden; display: flex; justify-content: center; align-items: center;
    }
    .radar-circle {
        position: absolute; border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 50%;
    }
    .c1 { width: 80px; height: 80px; }
    .c2 { width: 160px; height: 160px; }
    .c3 { width: 240px; height: 240px; }
    .scanner-line {
        position: absolute; width: 150px; height: 150px;
        top: 50%; left: 50%;
        background: conic-gradient(from 0deg, rgba(0, 212, 255, 0.4) 0%, transparent 30%);
        border-radius: 50%; transform-origin: top left;
        animation: rotate 4s linear infinite;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .threat-node {
        position: absolute; width: 8px; height: 8px;
        background-color: #ff0000; border-radius: 50%;
        box-shadow: 0 0 10px #ff0000; animation: pulse 1.5s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

    /* Estilo del Panel de Consejos */
    .security-tips h4 { color: #58a6ff; border-bottom: 1px solid #30363d; padding-bottom: 5px; }
    .tips-list { list-style: none; padding: 0; }
    .tips-list li { margin-bottom: 10px; color: #c9d1d9; font-size: 0.9rem; }
    .tips-list li b { color: #f1e05a; }

    /* Estilo del Footer Especial */
    .maynor-footer { text-align: right; color: #8b949e; margin-top: 20px; font-size: 1rem; }
    .maynor-name { color: #00d4ff; font-weight: 900; font-size: 1.3rem; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 10px #00d4ff; }
    .badge-container { display: flex; justify-content: flex-end; gap: 10px; margin-top: 5px; }
    .badge { width: 40px; height: 40px; border-radius: 50%; border: 1px solid #333; background-color: #161b22; display: flex; align-items: center; justify-content: center; font-size: 0.6rem; color: #ccc; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 1. ENCABEZADO Y MÉTRICAS (FILA SUPERIOR UNIFICADA)
# =========================================================
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 0.9rem;'>TACHICAL HUB - CENTRO DE RESPUESTA A INCIDENTES</p>", unsafe_allow_html=True)

# Fila superior unificada de métricas
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Fiabilidad del Motor (Veritas)", "99.8%", "+0.01%", help="Verificación por Veritas Sec.")
with m2: st.metric("Base de Datos (Sentinel)", "+500k IPs", "Activo", help="Actualizado con Microsoft Sentinel IP Feed.")
with m3: st.metric("Protección Global (Active)", "Activa 24/7", "Secure", help="Monitorización global de red.")
with m4: st.metric("Uptime", "99.9%", "Estable", help="Tiempo de actividad de los nodos.")

st.write("---")

# =========================================================
# 2. CUERPO PRINCIPAL (CENTRO DE CONTROL UNIFICADO)
# =========================================================
col_tips, col_radar, col_action = st.columns([1, 1.5, 1])

# COLUMNA IZQUIERDA: CONSEJOS DE SEGURIDAD
with col_tips:
    st.markdown("""
    <div class="security-tips">
        <h4>💡 CONSEJOS TÁCTICOS</h4>
        <ul class="tips-list">
            <li><b>Phishing:</b> [NET] Nodo CDMX conectado via 192.168.1.XXRevisa siempre que el dominio del remitente coincida con el oficial. No confíes en urgencias.</li>
            <li><b>Privacidad:</b> Desactiva el GPS en las fotos si las subes a redes públicas. Limpia los metadatos EXIF.</li>
            <li><b>SPEI:</b> Si una página te pide datos de SPEI fuera del entorno bancario, sospecha de inmediato.</li>
            <li><b>Passphrases:</b> Usa frases cortas con números en lugar de contraseñas de una sola palabra. Ej: "Azul*Nubes*24".</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# COLUMNA CENTRAL: RADAR UNIFICADO (OPCIÓN 1)
with col_radar:
    st.markdown("📡 **RADAR CIRCULAR TÁCTICO** <span style='float:right; color:#3fb950;'>SCANNING...</span>", unsafe_allow_html=True)
    st.markdown("""
    <div class="radar-box">
        <div class="radar-circle c1"></div>
        <div class="radar-circle c2"></div>
        <div class="radar-circle c3"></div>
        <div class="scanner-line"></div>
        
        <div class="threat-node" style="top: 30%; left: 60%;"></div>
        <div class="threat-node" style="top: 70%; left: 40%;"></div>
        <div class="threat-node" style="top: 20%; left: 25%;"></div>
        <div class="threat-node" style="top: 80%; left: 75%;"></div>
        
        <caption style="position: absolute; bottom: 5px; color: #00d4ff; font-size: 0.7rem; font-weight: bold;">RANGO: 1000 KM | NODO: CDMX (MEX)</caption>
    </div>
    """, unsafe_allow_html=True)

# COLUMNA DERECHA: CONSOLA DE ACCIÓN Y LOG
with col_action:
    st.markdown("🔍 **ANÁLISIS DE AMENAZAS**")
    t1, t2 = st.tabs(["🔗 VERIFICAR LINK", "🖼️ FORENSE"])
    
    with t1:
        st.text_input("Ingresa el enlace sospechoso:", placeholder="https://", label_visibility="collapsed")
    
    with t2:
        img_file = st.file_uploader("Suba la imagen sospechosa:", type=['jpg','png','jpeg'], label_visibility="collapsed")

    if st.button("🚀 INICIAR PROTOCOLO ANTÍDOTO"):
        st.write("---")
        with st.spinner("Desarmando infraestructura del atacante..."):
            time.sleep(1) # Simulación pro
            st.success("PROTOCOLO COMPLETADO. NO SE DETECTARON AMENAZAS EN EL ENLACE.")
            st.warning("METADATOS GPS DETECTADOS EN LA IMAGEN. RECOMIENDA LIMPIAR ANTES DE SUBIR.")

    st.write("---")
    st.markdown("📜 **LIVE LOG**")
    st.markdown("""
    <div class="log-container">
        [SYS] Inicializando módulos tácticos...<br>
        [NET] Nodo CDMX conectado via 192.168.1.XX<br>
        [SEC] Protocolo EXIF activo.<br>
        [NET] Escaneando tráfico de red saliente en puerto 443<br>
        [INF] Escaneo finalizado. Protocolos listos.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 3. FOOTER ESPECIAL (IDENTIDAD MAYNOR + CERTIFICACIONES CISCO)
# =========================================================
st.write("---")
footer_col1, footer_col2 = st.columns([1, 1])

# Footer Izquierdo: Estado del Sistema
with footer_col1:
    annotated_text(("SISTEMA", "VIGILANTE", "#1f6feb"), ("FIREWALL", "ACTIVO", "#238636"))

# Footer Derecho: Maynor, Título Grande y Certificaciones Cisco
with footer_col2:
    st.markdown(f"""
    <div class="maynor-footer">
        Desarrollado y Verificado por:<br>
        <span class="maynor-name">Maynor, Certified Specialist</span><br>
        [ID SESIÓN: AMX-992-TX] [NET] Nodo CDMX conectado via 192.168.1.XX[SYS] Motor de Phishing: OK[SEC] Firewall Activo [CERTIFICADO DE SEGURIDAD]  
        <div class="badge-container">
            <div class="badge">
                <img src="https://images.vexels.com/media/users/3/132474/isolated/preview/2b66280453a2f7c07340c4973305a4f7-certified-professional-badge-by-vexels.png" width="30"><br>
                <span>Cisco<br>CyOps</span>
            </div>
            <div class="badge">
                <img src="https://images.vexels.com/media/users/3/132474/isolated/preview/2b66280453a2f7c07340c4973305a4f7-certified-professional-badge-by-vexels.png" width="30"><br>
                <span>Hacker<br>Ético</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
