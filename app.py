import streamlit as st
import pandas as pd
import time
from annotated_text import annotated_text

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

# 2. ESTILOS CSS AVANZADOS (Colores Cian y Textura Wireframe)
st.markdown("""
    <style>
    .main { background-color: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; }
    
    /* Contenedores Estilo HUD */
    .stMetric, .stTabs, div[data-testid="stTable"], .log-container {
        background-color: #0d1117; border: 1px solid #30363d;
        border-radius: 4px; padding: 15px;
    }

    /* Brillo Neón Cian para Títulos */
    .glow-header {
        color: #58a6ff; text-align: center; text-shadow: 0 0 20px #58a6ff;
        font-weight: 900; letter-spacing: 5px; text-transform: uppercase;
    }

    /* MAPA CON REJILLA TÁCTICA */
    .map-frame {
        width: 100%; height: 380px; background-color: #000;
        border: 1px solid #30363d; border-radius: 4px; position: relative;
        overflow: hidden;
        /* Rejilla cian */
        background-image: 
            linear-gradient(rgba(0, 212, 255, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 212, 255, 0.08) 1px, transparent 1px);
        background-size: 25px 25px;
    }

    /* Puntos Rojos Neón (Threat Dots) */
    .neon-dot {
        position: absolute; width: 10px; height: 10px;
        background-color: #ff0000; border-radius: 50%;
        box-shadow: 0 0 15px #ff0000, 0 0 5px #fff;
        animation: blink 1.5s infinite;
    }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

    /* Botón de Acción Táctica */
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

# 4. DASHBOARD PRINCIPAL
col_left, col_right = st.columns([1.8, 1])

with col_left:
    st.markdown("🌐 **WORLD THREAT MAP (NET)** <span style='float:right; color:#3fb950;'>ESTADO: OK</span>", unsafe_allow_html=True)
    
    # EL MAPA (Aquí es donde el HTML se renderiza correctamente)
    st.markdown("""
    <div class="map-frame">
        <div style="position: absolute; width: 100%; height: 100%; opacity: 0.15; background-image: url('https://upload.wikimedia.org/wikipedia/commons/e/ec/World_map_blank_without_borders.svg'); background-size: cover;"></div>
        
        <div class="neon-dot" style="top: 25%; left: 70%;"></div>
        <div class="neon-dot" style="top: 45%; left: 25%;"></div>
        <div class="neon-dot" style="top: 60%; left: 85%;"></div>
        <div class="neon-dot" style="top: 20%; left: 50%;"></div>
        
        <p style="position: absolute; bottom: 10px; left: 15px; color: #ff7b72; font-size: 0.75rem; font-weight: bold;">🔴 VECTORES DE ATAQUE DETECTADOS EN TIEMPO REAL</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("🚦 **SERVICIOS BAJO ATAQUE (MÉXICO)**")
    servicios_df = pd.DataFrame({
        "Servicio": ["Portal CFE", "SAT Inyección", "Nómina MX", "SPEI Gateway"],
        "Origen": ["Rusia", "China", "EE.UU.", "Rumania"],
        "Estado": ["🔴 CRÍTICO", "🟡 ADVERTENCIA", "🟢 BLOQUEADO", "🔵 MONITOREO"]
    })
    st.table(servicios_df)

with col_right:
    st.markdown("🛠️ **CONSOLA DE ACCIÓN**")
    t1, t2 = st.tabs(["🔗 RASTREO URL", "🖼️ FORENSE"])
    with t1:
        st.text_input("URL:", placeholder="https://", label_visibility="collapsed")
    with t2:
        st.file_uploader("Evidencia:", label_visibility="collapsed")
    
    st.button("🚀 EJECUTAR PROTOCOLO ANTÍDOTO")

    st.write("")
    st.markdown("📟 **LIVE EVENT LOG**")
    st.markdown("""
    <div style="background-color: #000; border: 1px solid #333; padding: 10px; color: #3fb950; font-family: monospace; font-size: 0.8rem; height: 120px; overflow-y: auto;">
        [SYS] Inicializando módulos tácticos...<br>
        [NET] Nodo CDMX activo (192.168.1.XX)<br>
        [SEC] Cortafuegos: Interceptación activa.<br>
        [INF] Base de datos de amenazas sincronizada.
    </div>
    """, unsafe_allow_html=True)

# 5. FOOTER
st.write("---")
f1, f2 = st.columns([1, 1])
with f1:
    annotated_text(("SISTEMA", "PROTEGIDO BY MAYNOR", "#1f6feb"))
with f2:
    st.markdown("<p style='text-align: right; color: #8b949e; font-size: 0.7rem;'>[ID SESIÓN: AMX-992-TX] [BY MAYNOR: Verified Specialist]</p>", unsafe_allow_html=True)
