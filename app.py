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
# 0. CONFIGURACIÓN Y ESTÉTICA "NEO-MILITAR" (HUD)
# =========================================================
st.set_page_config(page_title="Antídoto MX | Tactical HUD", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* Fondo y Tipografía */
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Contenedores con bordes finos (Wireframe) */
    .stMetric, .stTabs, .stFileUploader section, div[data-testid="stExpander"] {
        background-color: #0d1117; border: 1px solid #30363d;
        border-radius: 8px; padding: 15px;
    }

    /* Botón Neon */
    div.stButton > button {
        background: linear-gradient(135deg, #1f6feb 0%, #00d4ff 100%);
        color: white; border: none; font-weight: bold;
        width: 100%; height: 50px; border-radius: 5px;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.3); text-transform: uppercase;
    }

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

    /* Estilo para el Mapa Mundial */
    .map-container {
        width: 100%; height: 350px; background-color: #000;
        border: 1px solid #30363d; border-radius: 8px; position: relative;
        overflow: hidden;
    }
    
    /* Puntos de amenaza animados */
    .threat-dot {
        position: absolute; width: 6px; height: 6px;
        background-color: #ff0000; border-radius: 50%;
        animation: pulseThreat 1.5s infinite;
    }
    @keyframes pulseThreat { 0% { box-shadow: 0 0 0 0px rgba(255, 0, 0, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(255, 0, 0, 0); } 100% { box-shadow: 0 0 0 0px rgba(255, 0, 0, 0); } }

    /* Estilo para la Tabla de Servicios */
    .status-table { width: 100%; font-size: 0.9rem; margin-top: 10px; }
    .status-critical { color: #ff7b72; font-weight: bold; }
    .status-warning { color: #f1e05a; }
    .status-ok { color: #3fb950; }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 1. DATOS SIMULADOS (Mapeo de Servicios)
# =========================================================
def obtener_servicios_atacados():
    return [
        {"Servicio": "Portal CFE (Phishing)", "País Origen": "Rusia", "IP Atacante": "190.115.x.x", "Estado": "CRÍTICO"},
        {"Servicio": "SAT (Inyección SQL)", "País Origen": "EE.UU. (Mass.)", "IP Atacante": "199.79.62.x", "Estado": "ADVERTENCIA"},
        {"Servicio": "Servidor Nómina MX", "País Origen": "China", "IP Atacante": "120.55.x.x", "Estado": "INTENTO BLOQUEADO"},
        {"Servicio": "SPEI (Denegación de Servicio)", "País Origen": "Rumania", "IP Atacante": "109.166.x.x", "Estado": "MONITOREO"},
    ]

# =========================================================
# 2. CABECERA Y MÉTRICAS HUD
# =========================================================
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 0.9rem;'>SISTEMA DE RESPUESTA TÁCTICA Y ANÁLISIS FORENSE</p>", unsafe_allow_html=True)

# Métricas superiores unificadas
m1, m2, m3, m4 = st.columns(4)
m1.metric("Amenazas Bloqueadas", "1,284", "+12")
m2.metric("IPs Rastreadas", "452", "Activo")
m3.metric("Uptime del Motor", "99.9%", "Estable")
m4.metric("Nivel de Riesgo", "Medio", "Rastreado")

st.write("---")

# =========================================================
# 3. CUERPO PRINCIPAL (HUD DE CIBERGUERRA)
# =========================================================
col_map, col_action = st.columns([2, 1.2])

with col_map:
    st.markdown("#### 🛰️ MAPA MUNDIAL DE AMENAZAS NET")
    # Simulación visual del mapa mundial (HUD Style)
    st.markdown("""
    <div class="map-container">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, #001a00 0%, #000 100%);"></div>
        
        <div class="threat-dot" style="top: 30%; left: 70%;"></div> <div class="threat-dot" style="top: 40%; left: 30%; animation-delay: 0.5s;"></div> <div class="threat-dot" style="top: 50%; left: 80%; animation-delay: 1s;"></div> <div class="threat-dot" style="top: 80%; left: 60%; animation-delay: 1.5s;"></div> <caption style="position: absolute; bottom: 5px; left: 5px; color: #ff0000; font-size: 0.7rem;">🔴 Puntos Rojos: Amenazas Críticas Activas</caption>
    </div>
    """, unsafe_allow_html=True)
    
    # NUEVA SECCIÓN: Mapeo de Servicios Atacados (debajo del mapa)
    st.write("---")
    st.markdown("#### 🚦 SERVICIOS CRÍTICOS BAJO ATAQUE (MÉXICO)")
    
    servicios = obtener_servicios_atacados()
    # Generar tabla HTML personalizada para el estilo HUD
    html_table = "<table class='status-table'><thead><tr><th>Servicio</th><th>País</th><th>IP</th><th>Estado</th></tr></thead><tbody>"
    for s in servicios:
        status_class = "status-critical" if s['Estado'] == "CRÍTICO" else \
                       "status-warning" if s['Estado'] == "ADVERTENCIA" else \
                       "status-ok"
        html_table += f"<tr><td>{s['Servicio']}</td><td>{s['País Origen']}</td><td>{s['IP Atacante']}</td><td class='{status_class}'>{s['Estado']}</td></tr>"
    html_table += "</tbody></table>"
    
    st.markdown(html_table, unsafe_allow_html=True)

with col_action:
    st.markdown("#### 🔍 CONSOLA DE ACCIÓN")
    
    # Herramientas unificadas en tabs tácticos
    tab1, tab2 = st.tabs(["🔗 RASTREO URL", "🖼️ FORENSE FOTOGRÁFICO"])
    
    with tab1:
        url_in = st.text_input("Ingresa el enlace sospechoso:", placeholder="https://")
    
    with tab2:
        img_in = st.file_uploader("Carga una imagen para extraer metadatos:", type=['jpg','png','jpeg'])

    if st.button("🚀 EJECUTAR PROTOCOLO ANTÍDOTO"):
        st.write("---")
        with st.spinner("Desarmando infraestructura del atacante..."):
            time.sleep(1)
            st.success("Análisis completado. Revise los resultados en la consola táctica.")

    # Live Log Táctico
    st.write("---")
    st.markdown("#### 📜 LIVE EVENT LOG")
    st.markdown("""
    <div class="log-container">
        [SYS] Inicializando módulos de escaneo táctico...<br>
        [NET] Nodo CDMX conectado via 192.168.1.XX<br>
        [NET] Escaneando tráfico de red saliente en puerto 443<br>
        [SEC] Protocolo EXIF cargado correctamente.<br>
        [WRN] Intento de handshake fallido en IP de Rumania.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 4. FOOTER PROFESIONAL
# =========================================================
st.write("---")
annotated_text(("SISTEMA", "VIGILANTE", "#1f6feb"), ("FIREWALL", "ACTIVO", "#238636"))
st.markdown(f"<p style='text-align: right; color: #8b949e;'>Desarrollado por <b>Maynor</b> | Especialista Independiente en Seguridad Digital</p>", unsafe_allow_html=True)
