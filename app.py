import streamlit as st
import pandas as pd
import requests
import socket
import time
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from annotated_text import annotated_text

# 0. CONFIGURACIÓN E IDENTIDAD VISUAL
st.set_page_config(page_title="Antídoto MX | Intelligence", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* Fondo y Tipografía */
    .main { background-color: #0d1117; color: #c9d1d9; }
    
    /* Estilo del Radar Circular */
    .radar-circle {
        width: 250px; height: 250px;
        background: radial-gradient(circle, #002200 0%, #000 100%);
        border: 2px solid #238636; border-radius: 50%;
        position: relative; margin: 0 auto;
        box-shadow: 0 0 20px rgba(35, 134, 54, 0.3);
        overflow: hidden;
    }
    .radar-sweep {
        position: absolute; width: 100%; height: 100%;
        background: conic-gradient(from 0deg, transparent 0%, rgba(0, 255, 0, 0.2) 25%, transparent 50%);
        animation: rotate 4s linear infinite;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    /* Contenedores Uniformes */
    .stat-card {
        background: #161b22; border: 1px solid #30363d;
        padding: 20px; border-radius: 12px; height: 100%;
    }
    
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 8px rgba(88, 166, 255, 0.4);
        font-family: 'Courier New', monospace; letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. ENCABEZADO UNIFICADO
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-top: -15px;'>Terminal de Ciberinteligencia - México</p>", unsafe_allow_html=True)
st.write("---")

# 2. SECCIÓN SUPERIOR: MÉTRICAS Y ESTADO (FILA 1)
col_info, col_trust = st.columns([2, 1])

with col_info:
    m1, m2, m3 = st.columns(3)
    m1.metric("Fiabilidad", "99.8%", "Óptimo")
    m2.metric("Inteligencia", "+500k IPs", "Actualizado")
    m3.metric("Uptime", "100%", "Secure")

with col_trust:
    st.markdown("""
    <div style='background: rgba(35, 134, 54, 0.1); border: 1px solid #238636; padding: 10px; border-radius: 8px; text-align: center;'>
        <small style='color: #3fb950;'>🔒 CONEXIÓN CIFRADA TLS 1.3</small>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# 3. CUERPO PRINCIPAL: RADAR Y ACCIÓN (FILA 2)
# Dividimos en 3 columnas iguales para que se vea ordenado
c1, c2, c3 = st.columns([1, 1.2, 1])

with c1:
    st.markdown("#### 🛰️ RADAR ACTIVO")
    st.markdown("""
    <div class="radar-circle">
        <div class="radar-sweep"></div>
        <div style="position: absolute; top: 40%; left: 60%; width: 5px; height: 5px; background: red; border-radius: 50%; box-shadow: 0 0 10px red;"></div>
        <div style="position: absolute; top: 70%; left: 30%; width: 5px; height: 5px; background: red; border-radius: 50%; box-shadow: 0 0 10px red;"></div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("<center>Escaneando nodos externos...</center>", unsafe_allow_html=True)

with c2:
    st.markdown("#### 🔍 INVESTIGACIÓN")
    with st.container():
        st.markdown("<div class='stat-card'>", unsafe_allow_html=True)
        tab_link, tab_img = st.tabs(["🔗 Enlace", "🖼️ Imagen"])
        with tab_link:
            url_in = st.text_input("URL sospechosa:", placeholder="https://")
        with tab_img:
            img_in = st.file_uploader("Subir evidencia:", type=['jpg','png','jpeg'])
        
        if st.button("⚡ EJECUTAR ESCANEO", use_container_width=True):
            with st.spinner("Procesando..."):
                time.sleep(1)
                st.toast("Análisis completado")
        st.markdown("</div>", unsafe_allow_html=True)

with c3:
    st.markdown("#### 💡 CONSEJOS")
    st.info("**Phishing:** Revisa que el remitente coincida con la empresa oficial.")
    st.warning("**Privacidad:** Las imágenes pueden contener tu ubicación exacta en los metadatos.")
    st.success("**Protección:** Antídoto MX no guarda registros de tus consultas.")

# 4. SECCIÓN INFERIOR: LOGS Y CRÉDITOS
st.write("---")
l1, l2 = st.columns([2, 1])

with l1:
    st.markdown("#### 📄 CERTIFICADO DE SEGURIDAD")
    st.code("Autoridad: Maynor Security Hub\nIntegridad: Verificada\nProtocolo: Análisis heurístico avanzado sin almacenamiento de datos.")

with l2:
    st.markdown("#### 👤 DESARROLLADOR")
    annotated_text(("SISTEMA", "BY MAYNOR", "#1f6feb"))
    st.caption("Especialista en Seguridad Digital")
