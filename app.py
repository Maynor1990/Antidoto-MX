import streamlit as st
import pandas as pd
import requests
import socket
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from annotated_text import annotated_text

# =========================================================
# 0. CONFIGURACIÓN Y ESTÉTICA "CYBER-TECH"
# =========================================================
st.set_page_config(page_title="Antídoto MX | Security Hub", page_icon="🛡️", layout="wide")

# Estilo con CSS Avanzado (Glassmorphism & Neon)
st.markdown("""
    <style>
    .main { background-color: #050505; color: #e0e0e0; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    
    /* Efecto de Cristal para Contenedores */
    div.stButton > button {
        background: linear-gradient(135deg, #0052D4 0%, #4364F7 50%, #6FB1FC 100%);
        color: white; border: none; border-radius: 5px; font-weight: 800;
        padding: 15px; text-transform: uppercase; letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(0, 82, 212, 0.4); transition: 0.3s;
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 82, 212, 0.6); }

    /* Inputs Estilo Hacker */
    .stTextInput>div>div>input, .stFileUploader section {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(88, 166, 255, 0.3) !important;
        color: #58a6ff !important; border-radius: 8px !important;
    }

    /* Animación del Radar Mejorada */
    .radar-container {
        position: relative; width: 300px; height: 300px;
        background: radial-gradient(circle, #001a00 0%, #000000 100%);
        border: 2px solid #00ff00; border-radius: 50%;
        margin: 20px auto; box-shadow: 0 0 30px rgba(0, 255, 0, 0.2); overflow: hidden;
    }
    .radar-sweep {
        position: absolute; width: 50%; height: 100%;
        background: linear-gradient(90deg, rgba(0, 255, 0, 0.3) 0%, transparent 100%);
        top: 0; left: 50%; transform-origin: left center;
        animation: rotateRadar 3s linear infinite;
    }
    @keyframes rotateRadar { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .glow-text {
        text-align: center; color: #58a6ff; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='glow-text'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>TERMINAL DE INTELIGENCIA Y CONTRAMEDIDAS DIGITALES</p>", unsafe_allow_html=True)
st.write("---")

# =========================================================
# 1. LÓGICA DE ESCANEO (BACKEND)
# =========================================================

def scan_url(url):
    try:
        dom = url.split('//')[-1].split('/')[0]
        ip = socket.gethostbyname(dom)
        geo = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()
        return {"ip": ip, "pais": geo.get('country', '??'), "isp": geo.get('isp', 'N/A'), "dom": dom}
    except: return None

def scan_img(img_file):
    try:
        img = Image.open(img_file)
        exif = img._getexif()
        detalles = []
        riesgo = "BAJO"
        if exif:
            for tid, val in exif.items():
                tag = TAGS.get(tid, tid)
                if tag == 'GPSInfo': riesgo = "MEDIO"; detalles.append("📍 GPS Detectado")
                if tag == 'Model': detalles.append(f"📷 Dispositivo: {val}")
        return riesgo, detalles
    except: return "ERROR", []

# =========================================================
# 2. PANEL DE CONTROL (FRONTEND)
# =========================================================
col_radar, col_tools = st.columns([1, 2])

with col_radar:
    st.markdown("""
    <div class="radar-container">
        <div class="radar-sweep"></div>
        <div style="position: absolute; top: 30%; left: 70%; width: 6px; height: 6px; background: red; border-radius: 50%; box-shadow: 0 0 10px red;"></div>
        <div style="position: absolute; top: 60%; left: 20%; width: 6px; height: 6px; background: red; border-radius: 50%; box-shadow: 0 0 10px red;"></div>
    </div>
    """, unsafe_allow_html=True)
    st.info("📡 RADAR: Escaneando tráfico de red saliente...")

with col_tools:
    with st.expander("🌐 INVESTIGACIÓN DE ENLACES", expanded=True):
        url_in = st.text_input("URL Sospechosa:", placeholder="https://ejemplo-fraude.com")
    
    with st.expander("🖼️ ANÁLISIS FORENSE DE IMÁGENES", expanded=True):
        img_in = st.file_uploader("Arrastra aquí el archivo:", type=['jpg','png','jpeg'])

    if st.button("⚡ INICIAR PROTOCOLO DE ANÁLISIS"):
        st.write("---")
        r1, r2 = st.columns(2)
        
        if url_in:
            with r1:
                st.markdown("### 🔍 Resultado Link")
                res = scan_url(url_in)
                if res:
                    st.success(f"DOMINIO: {res['dom']}")
                    st.metric("UBICACIÓN", res['pais'])
                    st.metric("IP", res['ip'])
                    if res['pais'] != "Mexico":
                        st.error("🚨 SERVIDOR EXTRANJERO DETECTADO")
                else: st.error("Link no rastreable.")

        if img_in:
            with r2:
                st.markdown("### 🖼️ Resultado Imagen")
                riesgo, datos = scan_img(img_in)
                st.metric("NIVEL DE RIESGO", riesgo)
                for d in datos: st.write(d)
                if not datos: st.write("No se encontraron metadatos ocultos.")

# =========================================================
# 3. FOOTER PROFESIONAL
# =========================================================
st.write("---")
f1, f2 = st.columns(2)
with f1:
    annotated_text(("SISTEMA", "VIGILANTE", "#1f6feb"), ("FIREWALL", "ACTIVO", "#238636"))
with f2:
    st.markdown(f"<p style='text-align: right; color: #8b949e;'>Desarrollado por <b>Maynor</b> | Especialista en Seguridad</p>", unsafe_allow_html=True)
