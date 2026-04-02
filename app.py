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
# 0. CONFIGURACIÓN Y ESTÉTICA "TACTICAL HUD" (Cian y Neón)
# =========================================================
st.set_page_config(page_title="Antídoto MX | Tactical HUD", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* Fondo y Tipografía Monospace (Técnica) */
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Contenedores con bordes finos (Wireframe) y fondo negro */
    .stMetric, .stTabs, .stFileUploader section, div[data-testid="stExpander"] {
        background-color: #0d1117; border: 1px solid #30363d;
        border-radius: 8px; padding: 15px;
    }

    /* Botón Neon Cian */
    div.stButton > button {
        background: linear-gradient(135deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold;
        width: 100%; height: 50px; border-radius: 5px;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4); text-transform: uppercase;
        letter-spacing: 2px;
    }
    div.stButton > button:hover {
        transform: translateY(-2px); box-shadow: 0 0 25px rgba(0, 212, 255, 0.7);
    }

    /* Inputs Tácticos */
    .stTextInput>div>div>input {
        background-color: #0d1117 !important; color: #00d4ff !important;
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
    }

    /* Título con Neón Cian */
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 5px; margin-bottom: 0px;
    }

    /* Estilo para el Mapa Mundial con Textura Wireframe */
    .map-container {
        width: 100%; height: 400px; background-color: #000;
        border: 2px solid #30363d; border-radius: 8px; position: relative;
        overflow: hidden;
        /* Fondo con textura de wireframe (líneas) */
        background-image: repeating-linear-gradient(rgba(0,0,0,0) 0, rgba(0,0,0,0) 2px, rgba(0,255,255,0.03) 2px, rgba(0,255,255,0.03) 4px), repeating-linear-gradient(90deg, rgba(0,0,0,0) 0, rgba(0,0,0,0) 2px, rgba(0,255,255,0.03) 2px, rgba(0,255,255,0.03) 4px);
    }
    
    /* Puntos de amenaza animados Neón Rojo */
    .threat-dot {
        position: absolute; width: 8px; height: 8px;
        background-color: #ff0000; border-radius: 50%;
        animation: pulseThreat 1.5s infinite;
        box-shadow: 0 0 15px #ff0000;
    }
    @keyframes pulseThreat { 0% { box-shadow: 0 0 0 0px rgba(255, 0, 0, 0.8); } 70% { box-shadow: 0 0 0 15px rgba(255, 0, 0, 0); } 100% { box-shadow: 0 0 0 0px rgba(255, 0, 0, 0); } }

    /* Estilo para la Tabla de Servicios */
    .status-table { width: 100%; font-size: 0.9rem; margin-top: 10px; font-family: 'Courier New', monospace; border-collapse: collapse; }
    .status-table th { color: #58a6ff; border-bottom: 1px solid #30363d; padding: 10px; text-align: left; }
    .status-table td { border-bottom: 1px solid #1f1f1f; padding: 10px; }
    .status-critical { color: #ff7b72; font-weight: bold; }
    .status-warning { color: #f1e05a; }
    .status-ok { color: #3fb950; }
    </style>
    """, unsafe_allow_html=True)

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

def get_threats():
    # Simulación de servicios atacados
    return [
        {"Servicio": "CFE (Phishing)", "Origen": "Rusia", "IP": "190.115.x.x", "Estado": "CRÍTICO"},
        {"Servicio": "SAT (SQL Injection)", "Origen": "China", "IP": "120.55.x.x", "Estado": "ADVERTENCIA"},
        {"Servicio": "SPEI Gateway", "Origen": "Rumania", "IP": "109.166.x.x", "Estado": "INTENTO BLOQUEADO"},
    ]

# =========================================================
# 2. CABECERA Y MÉTRICAS HUD (COLORES CIAN)
# =========================================================
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>SISTEMA DE RESPUESTA TÁCTICA Y ANÁLISIS FORENSE</p>", unsafe_allow_html=True)

# Métricas superiores unificadas con fondo oscuro
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Amenazas Bloqueadas", "1,284", delta="↑ 12")
with m2: st.metric("IPs Rastreadas", "452", delta="Activo")
with m3: st.metric("Uptime", "99.9%", delta="Estable")
with m4: st.metric("Latencia", "12ms", delta="↓ 2ms")

st.write("---")

# =========================================================
# 3. CUERPO PRINCIPAL (HUD DE CIBERGUERRA)
# =========================================================
col_map, col_action = st.columns([1.8, 1])

with col_map:
    st.markdown("#### 🛰️ WORLD THREAT MAP (NET)")
    # Simulación visual del mapa mundial (HUD Style con texturas)
    st.markdown("""
    <div class="map-container">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.05; background-image: url('https://upload.wikimedia.org/wikipedia/commons/e/ec/World_map_blank_without_borders.svg'); background-size: cover; background-position: center;"></div>
        
        <div class="threat-dot" style="top: 25%; left: 70%;"></div> <div class="threat-dot" style="top: 40%; left: 25%; animation-delay: 0.5s;"></div> <div class="threat-dot" style="top: 50%; left: 85%; animation-delay: 1s;"></div> <div class="threat-dot" style="top: 10%; left: 50%; animation-delay: 1.5s;"></div> <caption style="position: absolute; bottom: 5px; left: 10px; color: #ff7b72; font-size: 0.7rem; font-weight: bold;">🔴 VECTORES DE ATAQUE CRÍTICOS (SIMULADOS)</caption>
    </div>
    """, unsafe_allow_html=True)
    
    # NUEVA SECCIÓN: Mapeo de Servicios Atacados (debajo del mapa)
    st.write("---")
    st.markdown("#### 🚦 SERVICIOS BAJO ATAQUE (MÉXICO)")
    
    threats_data = get_threats()
    # Generar tabla HTML personalizada para el estilo HUD
    html_table = "<table class='status-table'><thead><tr><th>Servicio</th><th>País</th><th>IP</th><th>Estado</th></tr></thead><tbody>"
    for t in threats_data:
        status_class = "status-critical" if t['Estado'] == "CRÍTICO" else \
                       "status-warning" if t['Estado'] == "ADVERTENCIA" else \
                       "status-ok"
        html_table += f"<tr><td>{t['Servicio']}</td><td>{t['Origen']}</td><td>{t['IP']}</td><td class='{status_class}'>{t['Estado']}</td></tr>"
    html_table += "</tbody></table>"
    
    st.markdown(html_table, unsafe_allow_html=True)

with col_action:
    st.markdown("#### 🔍 CONSOLA DE ACCIÓN")
    
    # Herramientas unificadas en tabs tácticos con fondo negro
    tab1, tab2 = st.tabs(["🔗 RASTREO URL", "🖼️ IMÁGENES FORENSES"])
    
    with tab1:
        url_in = st.text_input("Ingresa el enlace sospechoso:", placeholder="https://")
    
    with tab2:
        st.write("Suba la imagen para extraer metadatos GPS.")
        img_in = st.file_uploader("Arrastra aquí el archivo:", type=['jpg','png','jpeg'], key="file_hud")

    if st.button("🚀 EJECUTAR PROTOCOLO ANTÍDOTO"):
        st.write("---")
        if url_in:
            with st.spinner("Desarmando infraestructura del atacante..."):
                time.sleep(1.5) # Simulación pro
                res = scan_url(url_in)
                if res:
                    st.success(f"DOMINIO: {res['dom']}")
                    st.code(f"IP: {res['ip']}\nPaís: {res['pais']}\nISP: {res['isp']}")
                    if res['pais'] != "Mexico":
                        st.error("🚨 SERVIDOR FUERA DE MÉXICO DETECTADO")
                else: st.error("Link no rastreable.")
        if img_in:
            st.info("Análisis forense de imagen simulado. Sin metadatos detectados.")

    # Live Log Táctico
    st.write("---")
    st.markdown("#### 📜 LIVE EVENT LOG")
    st.markdown("""
    <div style="background-color: #000; border: 1px solid #333; padding: 10px; color: #00ff00; font-family: 'Courier New', monospace; font-size: 0.8rem; height: 150px; overflow-y: auto; border-radius: 8px;">
        [SYS] Inicializando módulos de escaneo táctico...<br>
        [NET] Nodo CDMX conectado via 192.168.1.XX<br>
        [SEC] Cortafuegos en modo interceptación activa.<br>
        [WRN] Intento de handshake fallido en IP de China.<br>
        [INF] Base de datos de amenazas actualizada.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 4. FOOTER PROFESIONAL
# =========================================================
st.write("---")
c_f1, c_f2 = st.columns([1, 1.2])
with c_f1:
    annotated_text(("SISTEMA", "PROTEGIDO BY MAYNOR", "#1f6feb"))
with c_f2:
    st.markdown(f"<p style='text-align: right; color: #8b949e; font-size: 0.8rem;'>[ID SESIÓN: AMX-992-TX] [BY MAYNOR: Verified Specialist]</p>", unsafe_allow_html=True)
