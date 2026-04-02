import streamlit as st
import pandas as pd
import requests
import socket
import time
from annotated_text import annotated_text

# =========================================================
# 0. CONFIGURACIÓN Y ESTÉTICA "TACTICAL HUD" (OPCIÓN 3)
# =========================================================
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# CSS para forzar los colores y texturas de la imagen 3
st.markdown("""
    <style>
    /* Fondo oscuro profundo */
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Contenedores con bordes finos estilo Wireframe */
    .stMetric, .stTabs, div[data-testid="stTable"], .log-container {
        background-color: #0d1117; border: 1px solid #30363d;
        border-radius: 4px; padding: 15px;
    }

    /* Título con resplandor Cian */
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 15px #58a6ff;
        font-weight: 900; letter-spacing: 5px; margin-bottom: 10px;
    }

    /* MAPA MUNDIAL CON TEXTURA DE REJILLA (WIREFRAME) */
    .map-container {
        width: 100%; height: 380px; background-color: #000;
        border: 1px solid #30363d; border-radius: 4px; position: relative;
        overflow: hidden;
        /* Textura de líneas cian muy sutiles */
        background-image: 
            linear-gradient(rgba(0, 212, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 212, 255, 0.05) 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    /* Puntos de amenaza Rojos Neón parpadeantes */
    .threat-dot {
        position: absolute; width: 10px; height: 10px;
        background-color: #ff0000; border-radius: 50%;
        box-shadow: 0 0 15px #ff0000;
        animation: pulseThreat 1.5s infinite;
        z-index: 10;
    }
    @keyframes pulseThreat { 
        0% { box-shadow: 0 0 0 0px rgba(255, 0, 0, 0.7); } 
        70% { box-shadow: 0 0 0 15px rgba(255, 0, 0, 0); } 
        100% { box-shadow: 0 0 0 0px rgba(255, 0, 0, 0); } 
    }

    /* Botón Táctico Cian */
    div.stButton > button {
        background: linear-gradient(135deg, #00d4ff 0%, #1f6feb 100%);
        color: white; border: none; font-weight: bold;
        width: 100%; height: 45px; border-radius: 4px;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }

    /* Tabla de servicios */
    .status-critical { color: #ff7b72; font-weight: bold; }
    .status-ok { color: #3fb950; }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 1. ENCABEZADO Y MÉTRICAS (FILA SUPERIOR)
# =========================================================
st.markdown("<h1 class='glow-header'>🛡️ ANTÍDOTO MX | TACTICAL HUB</h1>", unsafe_allow_html=True)

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("Fiabilidad del Motor", "99.8%", "ÓPTIMO")
col_m2.metric("Base de Datos", "+500k IPs", "ACTUALIZADO")
col_m3.metric("Protección Global", "Activa 24/7", "SECURE")
col_m4.metric("Amenazas Hoy", "1,284", "↑ 12")

st.write("---")

# =========================================================
# 2. CUERPO PRINCIPAL (MAPA + CONSOLA)
# =========================================================
col_left, col_right = st.columns([1.8, 1])

with col_left:
    st.markdown("🌐 **WORLD THREAT MAP (NET)** <span style='float:right; color:#3fb950; font-size:0.8rem;'>ESTADO DEL SISTEMA: OK</span>", unsafe_allow_html=True)
    
    # Renderizado del Mapa con puntos (Corregido para que no se vea como texto)
    st.markdown("""
    <div class="map-container">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.1; background-image: url('https://upload.wikimedia.org/wikipedia/commons/e/ec/World_map_blank_without_borders.svg'); background-size: cover; background-position: center;"></div>
        
        <div class="threat-dot" style="top: 25%; left: 70%;"></div>
        <div class="threat-dot" style="top: 40%; left: 25%;"></div>
        <div class="threat-dot" style="top: 55%; left: 80%;"></div>
        <div class="threat-dot" style="top: 15%; left: 50%;"></div>
        
        <caption style="position: absolute; bottom: 5px; left: 10px; color: #ff7b72; font-size: 0.7rem; font-weight: bold;">🔴 VECTORES DE ATAQUE DETECTADOS</caption>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("🚦 **SERVICIOS BAJO ATAQUE (MÉXICO)**")
    
    # Tabla de servicios integrada (Mapeo que hicimos)
    servicios = {
        "Servicio": ["Portal CFE (Phishing)", "SAT (SQL Injection)", "Servidor Nómina MX", "SPEI Gateway"],
        "País Origen": ["Rusia", "China", "EE.UU.", "Rumania"],
        "Estado": ["🔴 CRÍTICO", "🟡 ADVERTENCIA", "🟢 BLOQUEADO", "🔵 MONITOREO"]
    }
    st.table(pd.DataFrame(servicios))

with col_right:
    st.markdown("🛠️ **CONSOLA DE ACCIÓN**")
    tabs = st.tabs(["🔗 VERIFICAR LINK", "🖼️ IMÁGENES FORENSES"])
    
    with tabs[0]:
        st.text_input("Ingresa URL para auditoría:", placeholder="https://", label_visibility="collapsed")
    with tabs[1]:
        st.file_uploader("Subir evidencia:", type=['jpg','png','jpeg'], label_visibility="collapsed")

    if st.button("🚀 INICIAR PROTOCOLO ANTÍDOTO"):
        with st.spinner("Ejecutando contramedidas..."):
            time.sleep(1.5)
            st.success("Análisis completado satisfactoriamente.")

    st.write("")
    st.markdown("📟 **LIVE EVENT LOG**")
    st.markdown("""
    <div style="background-color: #000; border: 1px solid #333; padding: 10px; color: #3fb950; font-family: monospace; font-size: 0.8rem; height: 110px; overflow-y: auto;">
        [SYS] Módulos tácticos cargados.<br>
        [NET] Nodo CDMX activo (192.168.1.XX)<br>
        [SEC] Cortafuegos en modo interceptación.<br>
        [INF] Base de datos de amenazas actualizada.<br>
        [WRN] Intento de handshake bloqueado.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("💡 **CONSEJOS TÁCTICOS**")
    st.caption("• Revisa siempre que el dominio termine en .com.mx oficial.")
    st.caption("• No compartas capturas de pantalla con datos sensibles.")

# =========================================================
# 3. FOOTER (IDENTICO A IMAGEN)
# =========================================================
st.write("---")
f1, f2 = st.columns([1, 1])
with f1:
    annotated_text(("SISTEMA", "PROTEGIDO BY MAYNOR", "#238636"))
with f2:
    st.markdown("<p style='text-align: right; color: #8b949e; font-size: 0.7rem;'>[ID SESIÓN: AMX-992-TX] [BY MAYNOR: Verified Specialist]</p>", unsafe_allow_html=True)
