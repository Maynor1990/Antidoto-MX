import streamlit as st
import pandas as pd
import time
from annotated_text import annotated_text

# =========================================================
# 0. ESTÉTICA HUD (IDENTICA A IMAGEN TACTICAL HUB)
# =========================================================
st.set_page_config(page_title="Antídoto MX | Tactical Hub", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    /* Fondo oscuro y tipografía técnica */
    .main { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; }
    
    /* Contenedores con borde fino estilo wireframe */
    .stMetric, .stTable, div[data-testid="stExpander"], .stTabs, .log-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 4px;
        padding: 10px;
    }

    /* Botón de Análisis Estilo Tactical */
    div.stButton > button {
        background: linear-gradient(180deg, #1f6feb 0%, #1158c7 100%);
        color: white; border: 1px solid #30363d;
        width: 100%; height: 45px; border-radius: 4px;
        font-weight: bold; text-transform: uppercase;
    }

    /* Mapa Mundial Estilizado */
    .map-container {
        width: 100%; height: 320px; background-color: #000;
        border: 1px solid #30363d; border-radius: 4px;
        position: relative; overflow: hidden;
        background-image: radial-gradient(circle, #1a2a1a 0%, #000 100%);
    }
    
    .threat-node {
        position: absolute; width: 8px; height: 8px;
        background-color: #ff3333; border-radius: 50%;
        box-shadow: 0 0 10px #ff3333; animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }

    /* Estilo para la Tabla de Servicios */
    .status-critical { color: #ff7b72; font-weight: bold; }
    .status-ok { color: #3fb950; }
    
    .log-box {
        font-family: 'Courier New', monospace; font-size: 0.85rem;
        color: #58a6ff; height: 100px; overflow-y: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 1. ENCABEZADO Y MÉTRICAS (IDENTICO A TOP ROW)
# =========================================
st.markdown("<h2 style='text-align: center; color: #ffffff;'>🛡️ ANTÍDOTO MX | TACTICAL HUB</h2>", unsafe_allow_html=True)

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Fiabilidad del Motor", "99.8%", delta="ÓPTIMO")
with col_m2:
    st.metric("Base de Datos", "+500k IPs", delta="ACTUALIZADO")
with col_m3:
    st.metric("Protección Global", "Activa 24/7", delta="SECURE")

st.write("---")

# =========================================================
# 2. CUERPO PRINCIPAL (MAPA + ACCIÓN)
# =========================================================
col_left, col_right = st.columns([1.8, 1])

with col_left:
    st.markdown("🌐 **WORLD THREAT MAP** <span style='float:right; color:#3fb950;'>ESTADO DEL SISTEMA: **OK**</span>", unsafe_allow_html=True)
    st.markdown("""
    <div class="map-container">
        <div class="threat-node" style="top: 30%; left: 20%;"></div>
        <div class="threat-node" style="top: 40%; left: 70%;"></div>
        <div class="threat-node" style="top: 65%; left: 45%;"></div>
        <div class="threat-node" style="top: 15%; left: 80%;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("🚦 **SERVICIOS CRÍTICOS BAJO ATAQUE (MÉXICO)**")
    # Tabla de servicios integrada debajo del mapa
    servicios_data = {
        "Servicio": ["Portal CFE (Phishing)", "SAT (Inyección SQL)", "Servidor Nómina MX", "SPEI (DDoS)"],
        "Origen": ["Rusia", "EE.UU.", "China", "Rumania"],
        "IP Atacante": ["190.115.x.x", "199.79.62.x", "120.55.x.x", "109.166.x.x"],
        "Estado": ["🔴 CRÍTICO", "🟡 ADVERTENCIA", "🟢 BLOQUEADO", "🔵 MONITOREO"]
    }
    st.table(pd.DataFrame(servicios_data))

with col_right:
    st.markdown("🛠️ **CONSOLA DE ACCIÓN**")
    tab_url, tab_img = st.tabs(["🔗 VERIFICAR LINK", "🖼️ IMÁGENES FORENSES"])
    
    with tab_url:
        st.text_input("URL sospechosa:", placeholder="https://", label_visibility="collapsed")
        
    with tab_img:
        st.file_uploader("Subir evidencia:", type=['jpg','png','jpeg'], label_visibility="collapsed")

    if st.button("⚡ INICIAR ANÁLISIS SEGURO"):
        with st.spinner("Ejecutando protocolos..."):
            time.sleep(1.5)
            st.success("Análisis Finalizado")

    st.write("")
    st.markdown("📟 **LIVE EVENT LOG**")
    st.markdown("""
    <div class="log-box">
        [SYS] Inicializando módulos tácticos...<br>
        [NET] Nodo CDMX activo (192.168.1.XX)<br>
        [SEC] Cortafuegos en modo interceptación.<br>
        [WRN] Tráfico inusual detectado en puerto 8080.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("💡 **CONSEJOS DE CIBERSEGURIDAD**")
    st.caption("• Revisa remitentes oficiales en correos.")
    st.caption("• Desactiva el GPS en fotos antes de compartirlas.")

# =========================================================
# 3. FOOTER
# =========================================================
st.write("---")
f_left, f_right = st.columns([1, 1])
with f_left:
    annotated_text(("SISTEMA", "PROTEGIDO BY MAYNOR", "#238636"))
with f_right:
    st.markdown("<p style='text-align: right; color: #8b949e; font-size: 0.8rem;'>[ID SESIÓN: AMX-992-TX] [BY MAYNOR: Verified Specialist]</p>", unsafe_allow_html=True)
