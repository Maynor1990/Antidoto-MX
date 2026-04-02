import streamlit as st
import pandas as pd
import requests
import socket
import re
from datetime import datetime
from difflib import SequenceMatcher

# =========================================================
# 1. MOTOR DE INTELIGENCIA (BACKEND)
# =========================================================

def similaridad(a, b):
    return SequenceMatcher(None, a, b).ratio()

def obtener_datos_forenses(url):
    """Rastrea la IP, País e ISP del servidor atacante"""
    try:
        # Extraer dominio (limpiar http/https)
        dominio = url.split('//')[-1].split('/')[0]
        ip = socket.gethostbyname(dominio)
        # API de Geolocalización (Gratuita para pruebas)
        geo = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()
        return {
            "ip": ip,
            "pais": geo.get('country', 'Desconocido'),
            "ciudad": geo.get('city', 'Desconocido'),
            "isp": geo.get('isp', 'Desconocido'),
            "dominio": dominio
        }
    except:
        return None

def analizar_ingenieria_social(mensaje):
    """Analiza tácticas de miedo o urgencia en el texto"""
    score = 0
    alertas = []
    patrones = {
        'URGENCIA': r'(urgente|bloqueo|inmediato|evite|corte|adeudo|multa)',
        'NÓMINA': r'(nomina|recibo|pago|cfdi|sueldo|deposito|ajuste)',
        'GANCHO': r'(premio|ganaste|bienestar|bono|sorteo|recompensa)'
    }
    for tipo, patron in patrones.items():
        if re.search(patron, mensaje.lower()):
            score += 30
            alertas.append(f"🚩 Detectada táctica de {tipo}")
    return score, alertas

# =========================================================
# 2. INTERFAZ DE USUARIO (FRONTEND)
# =========================================================

# Configuración visual de la App
st.set_page_config(page_title="Antídoto MX", page_icon="🛡️", layout="wide")

# Estilo Dark Mode Personalizado
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    h1 { color: #58a6ff; text-align: center; font-family: 'Courier New', monospace; }
    .stButton>button { background-color: #238636; color: white; border-radius: 8px; width: 100%; }
    .stTextInput>div>div>input { border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ANTÍDOTO MX")
st.write("### Sistema de Inteligencia contra Fraude Digital - México")
st.write("---")

# --- SECCIÓN DE ENTRADA ---
col_in, col_res = st.columns([1, 1])

with col_in:
    st.markdown("#### 🔍 Analizador de Enlaces")
    url_input = st.text_input("Pega el link sospechoso aquí:", placeholder="https://cfe-recibo-mex.xyz")
    
    st.markdown("#### ✉️ Analizador de Mensajes (Opcional)")
    msg_input = st.text_area("Pega el texto del mensaje recibido:", placeholder="Ej: Su recibo de nómina tiene un error...")
    
    boton_analizar = st.button("🚀 INICIAR RASTREO FORENSE")

# --- SECCIÓN DE RESULTADOS ---
with col_res:
    if boton_analizar:
        if url_input:
            with st.spinner('Desarmando infraestructura del atacante...'):
                datos = obtener_datos_forenses(url_input)
                score_msg, alertas_msg = analizar_ingenieria_social(msg_input) if msg_input else (0, [])
                
                if datos:
                    st.success(f"✅ Análisis Completado para: {datos['dominio']}")
                    
                    # Métricas clave
                    m1, m2 = st.columns(2)
                    m1.metric("País de Origen", datos['pais'])
                    m2.metric("IP detectada", datos['ip'])
                    
                    st.info(f"🏢 **Hosting (ISP):** {datos['isp']} | **Ciudad:** {datos['ciudad']}")
                    
                    # Lógica de Alerta Crítica (Ejemplo Massachusetts)
                    if "Mexico" not in datos['pais']:
                        st.error("🚨 ALERTA CRÍTICA: El servidor se encuentra fuera de México. Los servicios oficiales (CFE, SAT, Nómina MX) no operan desde el extranjero.")
                    
                    # Mostrar alertas de texto
                    for alerta in alertas_msg:
                        st.warning(alerta)
                    
                    # Botón de Denuncia
                    reporte = f"INCIDENTE DETECTADO POR ANTÍDOTO MX\n---\nURL: {url_input}\nIP: {datos['ip']}\nPAÍS: {datos['pais']}\nISP: {datos['isp']}\nFECHA: {datetime.now()}"
                    st.download_button("📩 Descargar Reporte para Policía Cibernética", reporte, file_name="denuncia_antidoto_mx.txt")
                else:
                    st.error("❌ No se pudo conectar con el servidor. Es probable que la URL sea falsa o el sitio ya haya sido dado de baja.")
        else:
            st.warning("⚠️ Por favor, ingresa al menos una URL para analizar.")

# --- FOOTER Y RADAR ---
st.write("---")
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.write("📡 **Radar de Amenazas (Activo):**")
    st.caption("🔴 [SANTANDER] Detectado en 190.115.x.x (Rusia)")
    st.caption("🔴 [CFE] Detectado en 199.79.62.144 (EE.UU. - Massachusetts)")
with col_f2:
    st.write("🔧 **Estatus del Sistema:**")
    st.success("Motor Heurístico: ONLINE")
    st.caption("Desarrollado por Mynor Vazquez | UnADM | Ciberseguridad Independiente")
