import streamlit as st
import pandas as pd
import time
from annotated_text import annotated_text

# 0. CONFIGURACIÓN HUD
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; }
    
    /* Contenedores Estilo Wireframe (Bordes finos) */
    .stMetric, .stTabs, .log-box, div[data-testid="stTable"] {
        background-color: #161b22; border: 1px solid #30363d; border-radius: 4px; padding: 10px;
    }

    /* MAPA MUNDIAL HUD (Imagen de fondo para que no se vea vacío) */
    .map-box {
        width: 100%; height: 260px; border: 1px solid #30363d; border-radius: 4px; position: relative;
        background-color: #000;
        /* Reemplazamos el fondo negro por un mapa estilizado de puntos */
        background-image: radial-gradient(#1f6feb 0.5px, transparent 0.5px);
        background-size: 15px 15px; 
    }
    
    /* Puntos de amenaza rojos parpadeantes */
    .threat-dot {
        position: absolute; width: 10px; height: 10px;
        background-color: #ff3333; border-radius: 50%;
        box-shadow: 0 0 12px #ff3333; animation: blink 2s infinite;
    }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }

    /* Botón Táctico Azul */
    div.stButton > button {
        background: linear-gradient(180deg, #1f6feb 0%, #1158c7 100%);
        color: white; border: 1px solid #30363d; border-radius: 4px;
        font-weight: bold; width: 100%; height: 40px;
    }

    .log-box { font-family: monospace; color: #58a6ff; font-size: 0.8rem; height: 100px; overflow-y: auto; }
    </style>
    """, unsafe_allow_html=True)

# 1. ENCABEZADO
st.markdown("<h2 style='text-align: center;'>🛡️ ANTÍDOTO MX | TACTICAL HUB</h2>", unsafe_allow_html=True)

# Fila de Métricas (Compactas)
m1, m2, m3 = st.columns(3)
m1.metric("Fiabilidad del Motor", "99.8%", "ÓPTIMO")
m2.metric("Base de Datos", "+500k IPs", "ACTUALIZADO")
m3.metric("Protección Global", "Activa 24/7", "SECURE")

st.write("---")

# 2. CUERPO PRINCIPAL (Layout exacto 2/3 y 1/3)
col_left, col_right = st.columns([1.7, 1])

with col_left:
    st.markdown("🌐 **WORLD THREAT MAP** <span style='float:right; color:#3fb950; font-size:0.8rem;'>ESTADO DEL SISTEMA: OK</span>", unsafe_allow_html=True)
    st.markdown("""
    <div class="map-box">
        <div class="threat-dot" style="top: 25%; left: 15%;"></div>
        <div class="threat-dot" style="top: 40%; left: 75%;"></div>
        <div class="threat-dot" style="top: 65%; left: 40%;"></div>
        <div class="threat-dot" style="top: 15%; left: 60%;"></div>
        <div style="position: absolute; width: 100%; height: 100%; border: 1px solid rgba(88,166,255,0.1); pointer-events: none;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("🚦 **SERVICIOS CRÍTICOS BAJO ATAQUE (MÉXICO)**")
    servicios = {
        "Servicio": ["Portal CFE (Phishing)", "SAT (Inyección SQL)", "Servidor Nómina MX", "SPEI (DDoS)"],
        "Origen": ["Rusia", "EE.UU.", "China", "Rumania"],
        "Estado": ["🔴 CRÍTICO", "🟡 ADVERTENCIA", "🟢 BLOQUEADO", "🔵 MONITOREO"]
    }
    st.table(pd.DataFrame(servicios))

with col_right:
    st.markdown("🛠️ **CONSOLA DE ACCIÓN**")
    t1, t2 = st.tabs(["🔗 VERIFICAR LINK", "🖼️ IMÁGENES"])
    with t1:
        st.text_input("URL:", placeholder="https://", label_visibility="collapsed")
    with t2:
        st.file_uploader("Evidencia:", label_visibility="collapsed")
    
    st.button("🚀 INICIAR ANÁLISIS SEGURO")

    st.write("")
    st.markdown("📟 **LIVE EVENT LOG**")
    st.markdown("""<div class="log-box">[SYS] Módulos cargados.<br>[NET] Nodo CDMX: 192.168.1.XX<br>[SEC] Firewall: Interceptando...</div>""", unsafe_allow_html=True)
    
    st.write("")
    st.markdown("💡 **CONSEJOS**")
    st.caption("• Revisa remitentes en correos oficiales.")
    st.caption("• Limpia metadatos GPS antes de subir fotos.")

# 3. FOOTER
st.write("---")
f1, f2 = st.columns([1, 1])
f1.markdown("✅ **SISTEMA PROTEGIDO POR MAYNOR**")
f2.markdown("<p style='text-align: right; color: #8b949e; font-size: 0.7rem;'>[ID SESIÓN: AMX-992-TX] [BY MAYNOR: Verified Specialist]</p>", unsafe_allow_html=True)
